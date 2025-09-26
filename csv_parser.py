import csv  # built-in module for reading/writing CSV files

# Open the CSV file
with open("data.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)  # reads rows into dictionaries

    # Loop through each row
    for row in reader:
        name = row["name"]
        age = row["age"]
        city = row["city"]

        # Print it nicely
        print(f"Name: {name} | Age: {age} | City: {city}")
