# Nasdaq Intelligence & Market Dynamics Dashboard

![v2.4](https://img.shields.io/badge/version-2.4.0--pro-gold)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Status](https://img.shields.io/badge/market--status-open-green)

A professional-grade financial visualization and monitoring suite for the Nasdaq Composite and core tech equities.

## 📊 Dashboard Preview
> **Note:** High-fidelity visualization engine optimized for dark-mode terminals.

### Core Metrics Captured:
* **Alpha Generation:** Real-time variance tracking against ^IXIC baseline.
* **Volatility Analysis:** Intra-day standard deviation monitoring.
* **Institutional Data:** Deep-dive fundamentals via Bloomberg-style logic.

## 🛠️ System Architecture
The suite is divided into modular engines:
* `scripts/core/`: Production-ready monitoring dashboards.
* `scripts/legacy/`: Iterative research and experimental fetchers.
* `research/`: Historical CSV datasets and volatility logs.

## 🚀 Deployment
```bash
source venv/bin/activate
python3 scripts/core/nasdaq_lab_v4.py
---

---

### 3. Generate the "Visual" (The Dark Mode Chart)
To get that graph look from your screenshot, you can use **Matplotlib** with a dark-style sheet. Create `scripts/core/visualizer.py`:

```python
import yfinance as yf
import matplotlib.pyplot as plt

# Set the Bloomberg/Dark style
plt.style.use('dark_background')

def generate_pro_chart(ticker="^IXIC"):
    data = yf.download(ticker, period="1mo")
    
    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'], color='#00d4ff', linewidth=2, label=f'{ticker} Evolution')
    
    plt.fill_between(data.index, data['Close'], color='#00d4ff', alpha=0.1)
    plt.title(f'{ticker} Performance Scorecard', fontsize=14, color='white', loc='left')
    plt.grid(color='#333333', linestyle='--', linewidth=0.5)
    plt.legend()
    
    plt.savefig('research/dashboard_preview.png', bbox_inches='tight', dpi=300)
    print("📈 High-fidelity chart generated in research/dashboard_preview.png")

if __name__ == "__main__":
    generate_pro_chart()
*Developed by [LauroBeck](https://github.com/LauroBeck)*
