import requests


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, token, origin, destinations):
        header = {
            "Authorization": "Bearer " + token
        }
        base_url = "https://test.api.amadeus.com/v2"
        url = base_url + "/shopping/flight-offers"

        for destination in destinations:
            params = {
                "originLocationCode": origin,
                "destinationLocationCode": destination,
                "departureDate": "2024-08-05",
                "adults": 2,
                "currencyCode": "EUR",
                "max": 1
            }
            response = requests.get(url=url, headers=header, params=params)
            response.raise_for_status()
            print(response.json()["data"][0]["price"])
