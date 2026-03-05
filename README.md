# 🏛️ IBM & Nasdaq Strategic Inflection Monitor (2026)

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintainer: LauroBeck](https://img.shields.io/badge/Maintainer-LauroBeck-cyan)](https://github.com/LauroBeck)

This engine utilizes **second-derivative acceleration analysis** to identify mathematical inflection points in equity trends. It specifically monitors the decoupling of **IBM (NYSE: IBM)** from the **Nasdaq Composite (^IXIC)** to detect "Value vs. Growth" rotations.

## 📊 Live Market Context (March 5, 2026)
As of today's market session, the system is tracking a critical **Tech-to-Value rotation** driven by global macro-pressure:

| Metric | Value | Status |
| :--- | :--- | :--- |
| **IBM Price** | **$259.16** | 🟢 Strong Recovery Signal |
| **Nasdaq Index** | **22,676.56** | 🔴 0.57% Intraday Decline |
| **S&P 500** | **6,803.19** | 🔴 0.98% Intraday Decline |
| **US 10-Yr Yield** | **4.12%** | ⚠️ Rising Bond Pressure |
| **Brent Crude** | **$83.00+** | ⚠️ Energy Supply Risk |

## 🛠️ Technology Stack
* **[yfinance](https://github.com/ranaroussi/yfinance)** - Real-time market data retrieval.
* **[SciPy](https://scipy.org/)** - Gaussian signal smoothing for noise reduction.
* **[Matplotlib](https://matplotlib.org/)** - Professional Bloomberg-style dark mode visualization.
* **[NumPy](https://numpy.org/)** - High-performance gradient calculations for inflection detection.

## 🚀 Getting Started

### Prerequisites
Ensure your environment is running Python 3.10 or higher.
```bash
pip install yfinance scipy matplotlib numpy
```

### Execution
Run the core monitor to generate the latest inflection map:
```bash
python3 scripts/core/ibm_monitor.py
```

---
**Developed by [LauroBeck](https://github.com/LauroBeck)**
