from zoomconnect_sdk.client import Client

c = Client(api_token='api_token', account_email='account_email')
try:
    balance = c.get_account_balance()
except Exception as e:
    print(e)
else:
    print(f"Balance: {balance.get('creditBalance', 0)}")