import yfinance as yf

def get_portfolio_pulse():
    # 2026 Strategic Stack: Banks + McLaren Partners
    stack = {
        "Mastercard (Title)": "MA",
        "Google (AI/Cloud)": "GOOGL",
        "Dell (Hardware)": "DELL",
        "Apple (F1 Broadcast)": "AAPL",
        "JPMorgan (JPM)": "JPM",
        "Wells Fargo (WFC)": "WFC",
        "BNY Mellon (BK)": "BK"
    }
    
    print("--- 2026 Institutional & Partner Stack ---")
    for name, ticker in stack.items():
        try:
            # Fallback to yfinance (REST/HTTPS) to bypass Bloomberg firewall
            val = yf.Ticker(ticker).history(period="1d")['Close'].iloc[-1]
            print(f"{name:22}: ${val:,.2f}")
        except:
            print(f"{name:22}: [Handshake Pending]")

if __name__ == "__main__":
    get_portfolio_pulse()
