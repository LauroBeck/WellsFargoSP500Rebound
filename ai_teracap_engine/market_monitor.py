import yfinance as yf
import pandas as pd

indices = {
    "Dow Jones": "^DJI",
    "S&P 500": "^GSPC",
    "Nasdaq": "^IXIC",
    "FTSE 100": "^FTSE",
    "DAX": "^GDAXI",
    "Nikkei 225": "^N225",
    "Hang Seng": "^HSI",
    "Brazil Bovespa": "^BVSP"
}

def global_market_monitor():

    data = {}

    for name, ticker in indices.items():

        hist = yf.download(ticker, period="5d", progress=False)

        last = hist["Close"].iloc[-1]
        prev = hist["Close"].iloc[-2]

        change = ((last - prev) / prev) * 100

        data[name] = [last, change]

    df = pd.DataFrame(data, index=["Price", "Daily % Change"]).T

    print("\nGLOBAL MARKET MONITOR\n")

    print(df.round(2))


if __name__ == "__main__":
    global_market_monitor()
