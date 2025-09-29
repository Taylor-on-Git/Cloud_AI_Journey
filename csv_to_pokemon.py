"""
csv_to_pokemon.py

A script that reads a list of Pokémon names from a CSV file,
queries the PokeAPI for details (ID, height, weight, and types),
and writes the enriched data into a new CSV.

Current behavior:
- Input: `data.csv` with at least a "name" column
- For each Pokémon name, call the PokeAPI
- Write results into `pokemon_data.csv` (includes name, ID, height, weight, and types)
- Print logs to track progress (OK or MISS)

Usage:
    python csv_to_pokemon.py

Notes:
- Requires the `requests` library (`pip install requests`)
- Demonstrates CSV file handling and API integration
"""

import csv
import requests

# Input and output CSV filenames
INPUT = "data.csv"
OUTPUT = "pokemon_data.csv"


def fetch_pokemon(name: str):
    """
    Fetch data about a Pokémon from the PokeAPI.

    Args:
        name (str): The Pokémon name (case-insensitive)

    Returns:
        dict or None: Dictionary with Pokémon details if found,
                      otherwise None
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower().strip()}"
    try:
        r = requests.get(url, timeout=10)  # make API call with timeout
        if r.status_code != 200:  # return None if Pokémon not found
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
    """
    Main function:
    - Read Pokémon names from `data.csv`
    - Call `fetch_pokemon` for each
    - Save results into `pokemon_data.csv`
    """
    rows_out = []  # store enriched Pokémon data here

    # Open the input CSV
    with open(INPUT, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        # Ensure there’s a 'name' column
        if "name" not in reader.fieldnames:
            print("ERROR: data.csv must have a 'name' column.")
            return

        # Loop through each row in data.csv
        for row in reader:
            poke = row.get("name", "").strip()
            if not poke:
                continue  # skip empty rows

            info = fetch_pokemon(poke)
            if info:
                print(f"OK: {poke}")  # log successful fetch
                rows_out.append(info)
            else:
                print(f"MISS: {poke} (not found)")

    # Write output file if results exist
    if rows_out:
        with open(OUTPUT, "w", newline="", encoding="utf-8") as g:
            writer = csv.DictWriter(
                g, fieldnames=["name", "id", "height", "weight", "types"]
            )
            writer.writeheader()
            writer.writerows(rows_out)
        print(f"Wrote {len(rows_out)} rows to {OUTPUT}")
    else:
        print("No results written.")


if __name__ == "__main__":
    main()
