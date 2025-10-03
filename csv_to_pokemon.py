"""
csv_to_pokemon.py (with error logging)

A script that reads a list of Pokémon names from a CSV file,
queries the PokeAPI for details (ID, height, weight, and types),
and writes the enriched data into a new CSV.

Enhancements:
- Successful Pokémon go into `pokemon_data.csv`
- Failed lookups (e.g. typos or not found) go into `pokemon_errors.csv`
- Console shows progress (OK or MISS)

Usage:
    python csv_to_pokemon.py

Notes:
- Input file must have a "name" column (default: data.csv)
- Requires the `requests` library (`pip install requests`)
- Demonstrates CSV handling, API calls, and error logging in Python
"""

import csv
import requests

# Input and output CSV filenames
INPUT = "data.csv"
OUTPUT = "pokemon_data.csv"
ERRORS = "pokemon_errors.csv"   # new file for failed lookups


def fetch_pokemon(name: str):
    """
    Fetch data about a Pokémon from the PokeAPI.

    Args:
        name (str): Pokémon name (case-insensitive)

    Returns:
        dict or None: Pokémon details if found, otherwise None
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower().strip()}"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code != 200:
            return None
        data = r.json()
        types = [t["type"]["name"] for t in data.get("types", [])]
        return {
            "name": data.get("name", name),
            "id": data.get("id", ""),
            "height": data.get("height", ""),
            "weight": data.get("weight", ""),
            "types": ", ".join(types),
        }
    except requests.RequestException:
        return None


def main():
    rows_out = []    # store successful Pokémon data
    errors_out = []  # store failed Pokémon lookups

    with open(INPUT, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        if "name" not in reader.fieldnames:
            print("ERROR: data.csv must have a 'name' column.")
            return

        for row in reader:
            poke = row.get("name", "").strip()
            if not poke:
                continue

            info = fetch_pokemon(poke)
            if info:
                print(f"OK: {poke}")
                rows_out.append(info)
            else:
                print(f"MISS: {poke} (not found)")
                errors_out.append({"name": poke, "reason": "not found"})

    # Write successes
    if rows_out:
        with open(OUTPUT, "w", newline="", encoding="utf-8") as g:
            writer = csv.DictWriter(
                g, fieldnames=["name", "id", "height", "weight", "types"]
            )
            writer.writeheader()
            writer.writerows(rows_out)
        print(f"Wrote {len(rows_out)} rows to {OUTPUT}")

    # Write errors
    if errors_out:
        with open(ERRORS, "w", newline="", encoding="utf-8") as h:
            writer = csv.DictWriter(h, fieldnames=["name", "reason"])
            writer.writeheader()
            writer.writerows(errors_out)
        print(f"Wrote {len(errors_out)} errors to {ERRORS}")


if __name__ == "__main__":
    main()
