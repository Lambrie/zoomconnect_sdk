from zoomconnect_sdk.client import Client

c = Client(api_token='api_token', account_email='account_email')
try:
    contact = c.create_contact("John","Doe","00000000","Mnr")
except Exception as e:
    print(e)
else:
    print(f"contact created {contact}")