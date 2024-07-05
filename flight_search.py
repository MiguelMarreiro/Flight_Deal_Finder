import requests
from datetime import datetime, timedelta
from notification_manager import NotificationManager


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, token, origin, target_data, notification_manager):
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


                    body = (f"Price alert!\n"
                            f"Itinerary: {origin + "-" + destination}\n"
                            f"Date: {date.strftime('%Y-%m-%d'),
                            data["itineraries"][0]["segments"][0]["departure"]["at"]}\n"
                            f"Price: {data["price"]["total"] + "€"}")

                    print(body)
                    notification_manager.send_notification(body)

                date += timedelta(days=1)
