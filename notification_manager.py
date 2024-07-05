import os

from twilio.rest import Client


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.my_number = os.environ["TWILIO_NUMBER"]
        self.account_sid = os.environ["TWILIO_SID"]
        self.auth_token = os.environ["TWILIO_TOKEN"]

    def send_notification(self, body):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body=body,
            from_='whatsapp:+14155238886',
            to='whatsapp:+351961568256',
        )