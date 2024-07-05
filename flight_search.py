import requests
from datetime import datetime, timedelta

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, token, origin, destinations):
        header = {
            "Authorization": "Bearer " + token
        }
        base_url = "https://test.api.amadeus.com/v2"
        url = base_url + "/shopping/flight-offers"

        date = datetime.now()

        for destination in destinations:
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
                print(date.strftime('%Y-%m-%d'))
                print(origin + "-" + destination)
                print(data["price"]["total"] + "€")

                date += timedelta(days=1)
