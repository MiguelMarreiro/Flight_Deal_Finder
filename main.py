#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
import requests
from flight_data import FlightData
from flight_search import FlightSearch

ORIGIN_CITY = "LIS"

# -------------------------------GETTING TOKEN-------------------------------
AMADEUS_KEY = os.environ["AMADEUS_KEY"]
AMADEUS_SECRET = os.environ["AMADEUS_SECRET"]
AMADEUS_TOKEN = ""

oauth_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
header = {
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "grant_type": "client_credentials",
    "client_id": AMADEUS_KEY,
    "client_secret": AMADEUS_SECRET,
}

response = requests.post(url=oauth_url, headers=header, data=data)
response.raise_for_status()
AMADEUS_TOKEN = response.json()["access_token"]

# -------------------------------GETTING FlightData-------------------------------
flight_data = FlightData(AMADEUS_TOKEN)
destination_codes = flight_data.city_codes



# -------------------------------GETTING FlightPrices-------------------------------
flight_search = FlightSearch(token=AMADEUS_TOKEN, origin=ORIGIN_CITY, destinations=destination_codes)