from dotenv import load_dotenv
import os

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

load_dotenv()

API_KEY = os.getenv("ALPACA_API_KEY")
SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")

if not API_KEY or not SECRET_KEY:
    raise ValueError("Missing ALPACA_API_KEY or ALPACA_SECRET_KEY in .env")

# paper=True tells alpaca-py to use the paper trading environment
client = TradingClient(API_KEY, SECRET_KEY, paper=True)

# 1) connection/auth test
account = client.get_account()
print("Connected successfully.")
print("Account status:", account.status)
print("Buying power:", account.buying_power)

# 2) tiny paper order test
order_request = MarketOrderRequest(
    symbol="SPY",
    qty=1,
    side=OrderSide.BUY,
    time_in_force=TimeInForce.DAY
)

order = client.submit_order(order_data=order_request)
print("Order submitted successfully.")
print("Order ID:", order.id)
print("Order symbol:", order.symbol)
print("Order status:", order.status)