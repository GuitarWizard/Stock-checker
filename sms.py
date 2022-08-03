import requests, json
from twilio.rest import Client


def send_alert(body):
    # Twilio SMS details
    account_sid = "***SID Redacted******"
    auth_token = "******TOKEN REDACTED*******"
    client = Client(account_sid, auth_token)


    message = client.messages \
        .create(
        body=body,
        from_='***REDACTED*****',
        to='+****REDACTED*****'
    )
