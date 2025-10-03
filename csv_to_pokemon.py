"""
csv_to_pokemon.py (enhanced)

Reads Pokémon from a CSV (default: data.csv), fetches details from PokeAPI,
writes results to pokemon_data.csv and failures to pokemon_errors.csv.

Usage:
    python csv_to_pokemon.py --input data.csv --output pokemon_data.csv --errors pokemon_errors.csv

Notes:
- Keeps any extra input columns (e.g., nickname) in the output
- Handles network errors + 404s
"""

import csv
import argparse
import time
import requests
from typing import Dict, Optional

def fetch_pokemon(name: str, retries: int = 2, delay: float = 0.5) -> Optional[Dict]:
    """Fetch a Pokémon dict from PokeAPI; return None on failure."""
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower().strip()}"
    for attempt in range(retries + 1):
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                data = r.json()
                types = [t["type"]["name"] for t in data.get("types", [])]
                return {
                    "name": data.get("name", name),
                    "id": data.get("id", ""),
                    "height": data.get("height", ""),
                    "weight": data.get("weight", ""),
                    "types": ", ".join(types),
                }
            elif r.status_code == 404:
                return None
            # transient server error; retry
        except requests.RequestException:
            pass
        if attempt < retries:
            time.sleep(delay)
    return None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data.csv")
    parser.add_argument("--output", default="pokemon_data.csv")
    parser.add_argument("--errors", default="pokemon_errors.csv")
    args = parser.parse_args()

    successes = []
    failures = []

    with open(args.input, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if "name" not in (reader.fieldnames or []):
            print("ERROR: input CSV must contain a 'name' column.")
            return

        input_headers = reader.fieldnames  # keep any extra columns

        for row in reader:
            raw_name = (row.get("name") or "").strip()
            if not raw_name:
                continue
            info = fetch_pokemon(raw_name)
            if info:
                # merge API info with original row (pass-through extras)
                merged = {**row, **info}
                successes.append(merged)
                print(f"OK: {raw_name}")
            else:
                failures.append({"name": raw_name, "reason": "not found or network error"})
                print(f"MISS: {raw_name}")

    # Build output headers = pass-through input + guaranteed API fields (dedup)
    api_fields = ["name", "id", "height", "weight", "types"]
    out_headers = []
    seen = set()
    for h in (input_headers or []) + api_fields:
        if h not in seen:
            out_headers.append(h)
            seen.add(h)

    if successes:
        with open(args.output, "w", newline="", encoding="utf-8") as g:
            writer = csv.DictWriter(g, fieldnames=out_headers)
            writer.writeheader()
            writer.writerows(successes)
        print(f"Wrote {len(successes)} rows → {args.output}")
    else:
        print("No successful rows to write.")

    if failures:
        with open(args.errors, "w", newline="", encoding="utf-8") as e:
            writer = csv.DictWriter(e, fieldnames=["name", "reason"])
            writer.writeheader()
            writer.writerows(failures)
        print(f"Wrote {len(failures)} errors → {args.errors}")

if __name__ == "__main__":
    main()
