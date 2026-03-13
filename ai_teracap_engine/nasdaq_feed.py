import yfinance as yf

# AI Teracap universe
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


def get_market_data():
    """
    Download market prices for AI Teracap companies
    """

    data = yf.download(
        TERACAPS,
        period="5d",
        interval="1d",
        progress=False
    )

    return data["Close"]
