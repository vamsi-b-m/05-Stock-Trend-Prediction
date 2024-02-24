import yfinance as yf
import pandas as pd

stock_symbol = "TATAMOTORS.NS"
stock_data = yf.Ticker(stock_symbol)
live_data = stock_data.history(period='20y', interval='1d')
df = pd.DataFrame(live_data)

df.to_csv("TATAMOTORS.csv")
print(live_data)