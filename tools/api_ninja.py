import os
from dotenv import load_dotenv

load_dotenv()

API_NINJA_KEY = os.getenv("API_NINJA_KEY")

def get_address_data(address):
    print(f"Mocking address data for: {address}")
    return {
        "latitude": 38.8977,
        "longitude": -77.0365,
        "city": "Washington",
        "state": "DC",
        "zip": "20500"
    }