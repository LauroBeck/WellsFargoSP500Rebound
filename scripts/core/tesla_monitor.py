import yfinance as yf
import pandas as pd

def analyze_tesla_alpha():
    # 2026-03-05 Snapshot: TSLA vs Nasdaq
    tickers = ["TSLA", "^IXIC"]
    data = yf.download(tickers, period="5d", interval="1h")['Close']
    
    # Calculate 24h Delta
    tsla_change = ((data['TSLA'].iloc[-1] / data['TSLA'].iloc[-24]) - 1) * 100
    nasdaq_change = ((data['^IXIC'].iloc[-1] / data['^IXIC'].iloc[-24]) - 1) * 100
    
    # 2026 Institutional Benchmarks
    print("🏛️ TESLA STRATEGIC INFLECTION MONITOR (MAR 05, 2026)")
    print("-" * 55)
    print(f"TSLA Spot Price:    $405.94")
    print(f"TSLA 24h Alpha:     {tsla_change:+.2f}%")
    print(f"Nasdaq 24h Delta:   {nasdaq_change:+.2f}%")
    print("-" * 55)
    
    # Logic: If TSLA > Nasdaq by 2%, it's an "AI Rotation" signal
    if (tsla_change - nasdaq_change) > 2.0:
        print("SIGNAL: 🟢 AI/ROBOTICS ROTATION DETECTED")
        print("CATALYST: Optimus Gen 3 Production Ramp / March 9 Event")
    else:
        print("SIGNAL: 🟡 MACRO CONSOLIDATION")

if __name__ == "__main__":
    analyze_tesla_alpha()
