import os
from dotenv import load_dotenv
from services.db import get_city_info

load_dotenv()

API_NINJA_KEY = os.getenv("API_NINJA_KEY")

def get_address_data(address):
    print(f"🔎 Searching database for: {address}")
    return get_city_info(address)