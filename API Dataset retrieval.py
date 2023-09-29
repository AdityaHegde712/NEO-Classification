import requests
import csv
print("Imports complete")

# Define the base URL for the API
base_url = "https://ssd-api.jpl.nasa.gov/cad.api"
print("Base URL defined")

# Define the parameters for the API request
params = {
    "dist-max": "0.2",  # Maximum distance in au
    "fullname": "true",  # Include full name/designation of the object
    "body": "Earth",  # Only include close approaches to Earth
    "date-min": "1900-01-01",  # Start date for close approaches
    "date-max": "2100-01-01",  # End date for close approaches
    "sort": "dist",  # Sort by distance
    "limit": 37915,  # Limit to 37915 entries
}
print("Parameters defined")

# Send a GET request to the API
response = requests.get(base_url, params=params)
print("GET request sent")

counter = 0

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    print("JSON response parsed")

    # Open a CSV file for writing
    with open("close_approaches.csv", "w", newline="") as f:
        writer = csv.writer(f)

        # Write the field names to the CSV file
        writer.writerow(data["fields"])
        print(f"Wrote row {counter}")
        counter += 1

        # Write each close approach to the CSV file
        for approach in data["data"]:
            writer.writerow(approach)
else:
    print(f"Failed to retrieve data: {response.status_code}")
