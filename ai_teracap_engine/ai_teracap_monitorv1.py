import yfinance as yf
import pandas as pd

# ---------------------------------
# AI TERACAP UNIVERSE
# ---------------------------------

TERACAPS = [
    "NVDA",
    "AMD",
    "MSFT",
    "AMZN",
    "GOOGL",
    "META",
    "TSM",
    "ASML"
]


# ---------------------------------
# MARKET DATA
# ---------------------------------

def download_market_data():

    data = yf.download(
        TERACAPS,
        period="5d",
        interval="1d",
        progress=False
    )

    return data["Close"]


# ---------------------------------
# INDICATORS
# ---------------------------------

def calculate_indicators(close):

    returns = close.pct_change() * 100

    latest_prices = close.iloc[-1]
    latest_returns = returns.iloc[-1]

    df = pd.DataFrame({
        "Price": latest_prices,
        "Daily % Change": latest_returns
    })

    return df


# ---------------------------------
# REGIME DETECTOR
# ---------------------------------

def regime_detector(df):

    momentum = df["Daily % Change"].mean()

    if momentum > 2:
        regime = "AI SUPER BULL"

    elif momentum > 0.5:
        regime = "AI EXPANSION"

    elif momentum > -1:
        regime = "NEUTRAL"

    else:
        regime = "RISK OFF"

    return regime, momentum


# ---------------------------------
# REVENUE MODEL
# ---------------------------------

def revenue_projection():

    current_revenue = 1.56e12
    growth = 0.18
    months = 16/12

    future = current_revenue * (1 + growth) ** months

    return future


# ---------------------------------
# MAIN
# ---------------------------------

def main():

    close = download_market_data()

    df = calculate_indicators(close)

    regime, momentum = regime_detector(df)

    revenue_future = revenue_projection()

    print("\nAI TERACAP MARKET PANEL\n")

    print(df.round(2))

    print("\nMomentum Score:", round(momentum, 2))

    print("Market Regime:", regime)

    print("\nProjected AI Ecosystem Revenue (16 months):")

    print(f"${revenue_future/1e12:.2f} TRILLION\n")


if __name__ == "__main__":
    main()
