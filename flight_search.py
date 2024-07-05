import requests
from datetime import datetime, timedelta

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, token, origin, target_data):
        header = {
            "Authorization": "Bearer " + token
        }
        base_url = "https://test.api.amadeus.com/v2"
        url = base_url + "/shopping/flight-offers"

        date = datetime.now()

        for row in target_data:
            destination = row[0]
            lowest_price = row[1]
            for _ in range(3):

                params = {
                    "originLocationCode": origin,
                    "destinationLocationCode": destination,
                    "departureDate": date.strftime('%Y-%m-%d'),
                    "adults": 2,
                    "currencyCode": "EUR",
                    "max": 1
                }
                response = requests.get(url=url, headers=header, params=params)
                response.raise_for_status()
                data = response.json()["data"][0]
                if float(data["price"]["total"]) < lowest_price:
                    print("SEND MESSAGE")
                    print(date.strftime('%Y-%m-%d'), data["itineraries"][0]["segments"][0]["departure"]["at"])
                    print(origin + "-" + destination)
                    print(data["price"]["total"] + "€")

                date += timedelta(days=1)
