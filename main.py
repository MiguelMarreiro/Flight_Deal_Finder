# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
import os
import requests
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY = "LIS"
notification_manager = NotificationManager()

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

# -------------------------------GETTING SheetData-------------------------------
# data_manager = DataManager()
# print(data_manager.data)
sheet_data = [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 200, 'id': 2},
              {'city': 'Frankfurt', 'iataCode': 'FRA', 'lowestPrice': 300, 'id': 3}]
# -------------------------------GETTING FlightData-------------------------------
target_data = [[row["city"], row["lowestPrice"]] for row in sheet_data]
destinations = [row[0] for row in target_data]
flight_data = FlightData(AMADEUS_TOKEN, destinations)
destination_codes = flight_data.city_codes
print(destination_codes)

for index in range(0, len(target_data)):
    target_data[index][0] = destination_codes[index]

print(target_data)

# -------------------------------GETTING FlightPrices-------------------------------
flight_search = FlightSearch(token=AMADEUS_TOKEN, origin=ORIGIN_CITY, target_data=target_data,
                             notification_manager=notification_manager)
