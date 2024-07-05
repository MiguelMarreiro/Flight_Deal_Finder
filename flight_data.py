import os
import requests

AMADEUS_ENDPOINT = "https://test.api.amadeus.com/v1"


class FlightData:
    def __init__(self, token, keywords):
        #This class is responsible for structuring the flight data.
        header = {
            "Authorization": "Bearer " + token
        }
        self.city_codes = []
        for keyword in keywords:
            params = {
                "keyword": keyword,
            }
            response = requests.get(url=AMADEUS_ENDPOINT+"/reference-data/locations/cities",
                                    headers=header, params=params)
            response.raise_for_status()
            self.city_codes.append(response.json()["data"][0]["iataCode"])