import yfinance as yf
import pandas as pd

tickers = [
    "NVDA",
    "AMD",
    "MSFT",
    "AMZN",
    "GOOGL",
    "META",
    "TSM",
    "ASML"
]

data = yf.download(tickers, period="5d")

close = data["Close"]

returns = close.pct_change().iloc[-1] * 100

df = pd.DataFrame({
    "Price": close.iloc[-1],
    "Daily %": returns
})

print("\nAI TERACAP MONITOR\n")
print(df.round(2))
