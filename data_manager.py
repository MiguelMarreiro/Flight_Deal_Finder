import requests
import os

SHEET_NAME = "prices"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_url = os.environ["GOOGLE_SHEET"]
        self.endpoint = os.environ["SHEETY_ENDPOINT"]
        self.data = requests.get(url=self.endpoint).json()[SHEET_NAME]

