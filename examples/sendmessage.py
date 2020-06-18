from zoomconnect_sdk.client import Client

c = Client(api_token='api_token', account_email='account_email')
try:
    oldBalance = c.get_account_balance()
    message = c.send_sms("0000000000", "Welcome to ZoomConnect")
    newBalance = c.get_account_balance()
except Exception as e:
    print(e)
else:
    print(f"message sent {message}")
    print(f"{oldBalance.get('creditBalance', 0)} -> {newBalance.get('creditBalance', 0)}")