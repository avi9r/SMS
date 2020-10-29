import os
import json
from twilio.rest import Client

ACCOUNT_SID = os.getenv('ACf69a4020e336cb159bd4cebda28965b6')
AUTH_TOKEN = os.getenv('527aa1f8e4f9df4054f510364369cde5')
NOTIFY_SERVICE_SID = os.getenv('MG17a92e59d7a4e43c5f5f279ba5596b97')

client = Client(ACCOUNT_SID, AUTH_TOKEN)


def send_bulk_sms(numbers, body):
    bindings = list(map(lambda number: json.dumps({'binding_type': 'sms', 'address': number}), numbers))
    print("=====> To Bindings :>", bindings, "<: =====")
    notification = client.notify.services(NOTIFY_SERVICE_SID).notifications.create(
        to_binding=bindings,
        body=body
    )
    print(notification.body)