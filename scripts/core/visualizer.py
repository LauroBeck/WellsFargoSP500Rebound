import yfinance as yf
import matplotlib.pyplot as plt

# Professional Bloomberg-style Dark Mode
plt.style.use('dark_background')

def generate_energy_impact_chart():
    print("🚀 Analyzing Energy vs. Tech Dynamics (2026)...")
    
    # Fetching Nasdaq and Crude Oil futures (BZ=F is Brent, CL=F is NYMEX)
    nasdaq = yf.download("^IXIC", period="1mo")
    brent = yf.download("BZ=F", period="1mo")

    fig, ax1 = plt.subplots(figsize=(14, 7))

    # Plot Nasdaq on primary Y-axis
    ax1.set_xlabel('Date (March 2026)')
    ax1.set_ylabel('Nasdaq Composite', color='#00d4ff')
    ax1.plot(nasdaq.index, nasdaq['Close'], color='#00d4ff', linewidth=2, label='Nasdaq')
    ax1.tick_params(axis='y', labelcolor='#00d4ff')
    ax1.grid(color='#333333', linestyle='--', alpha=0.5)

    # Create secondary Y-axis for Brent Crude
    ax2 = ax1.twinx()
    ax2.set_ylabel('Brent Crude ($/bbl)', color='#ff9900')
    ax2.plot(brent.index, brent['Close'], color='#ff9900', linewidth=2, linestyle='--', label='Brent Crude >$80')
    ax2.tick_params(axis='y', labelcolor='#ff9900')

    plt.title('Market Intelligence: Energy Surge vs. Tech Equity Performance', loc='left', fontsize=14)
    fig.tight_layout()
    
    # Save to your research folder
    save_path = 'research/energy_impact_2026.png'
    plt.savefig(save_path, dpi=300)
    print(f"📈 Strategic insight saved to {save_path}")

if __name__ == "__main__":
    generate_energy_impact_chart()
