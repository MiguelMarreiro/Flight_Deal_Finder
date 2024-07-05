#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager

data_manager = DataManager()

# test data_manager
# print(data_manager.sheet_url, "\n", data_manager.endpoint)
print(data_manager.data)