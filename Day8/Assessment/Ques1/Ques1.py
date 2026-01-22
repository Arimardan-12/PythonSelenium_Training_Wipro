"""
Write a Python program that:
1. Uses the requests library to send a GET request to a public REST API (e.g., users or posts API)
2. Sends custom headers with the request
3. Parses the JSON response and extracts specific fields
4. Serializes the extracted data and saves it into a JSON file
5. Handles HTTP errors using proper exception handling
"""

import requests
import json
url = "https://jsonplaceholder.typicode.com/users"  # Sample public API
headers = headers = {
    "User-Agent": "Python-App",
    "Accept": "application/json",
}
# Make the GET request with error handling
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
else:

    users = response.json()
# Extract specific fields
    extracted_data = []
    for user in users:
        extracted_data.append({
            "id": user["id"],
            "name": user["name"],
            "username": user["username"],
            "email": user["email"]
        })

# Save extracted data to a JSON file
    with open("users_data.json", "w") as f:
        json.dump(extracted_data, f, indent=4)

    print("Data saved successfully to users_data.json")
#to see the data printed on the console
    print(json.dumps(extracted_data, indent=4))

