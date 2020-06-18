from zoomconnect_sdk.client import Client

c = Client(api_token='api_token', account_email='account_email')
try:
    recipients = ["0000000000","1111111111","2222222222"]
    messages = ["Hi Joe, Welcome to ZoomConnect", "Hi Jane, Welcome to ZoomConnect", "Hi John, Welcome to ZoomConnect"]
    message = c.send_sms_bulk(recipients, messages)
except Exception as e:
    print(e)
else:
    print(f"messages sent {message}")