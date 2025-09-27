"""
api_fetcher.py

A script to fetch Pokémon data from the PokeAPI (https://pokeapi.co/).

Current behavior:
- Asks the user for a Pokémon name
- Calls the PokeAPI with that name
- If found, prints details (name, ID, height, weight, and types)
- If not found, shows a friendly error message

Usage:
    python api_fetcher.py

Notes:
- Requires the `requests` library (install with `pip install requests`)
- Demonstrates basic API requests and JSON handling in Python
"""

import requests # for API calls

# Ask the user for a pokemon name
pokemon = input("Enter a pokemon name: ").strip().lower()

# Build the API URL
URL = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

# Make the GET request
response = requests.get(URL)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # convert JSON response into a python dictionary

    # Extract key information
    name = data["name"]
    poke_id = data["id"]
    height = data["height"]
    weight = data["weight"]
    types = [t["type"]["name"] for t in data["types"]]

    # Print the information
    print(f"Name: {name}")
    print(f"ID: {poke_id}")
    print(f"Height: {height}")
    print(f"Weight: {weight}")
    print(f"Types: {', '.join(types)}")

else:
    print("Pokemon not found. Please check the name and try again.")