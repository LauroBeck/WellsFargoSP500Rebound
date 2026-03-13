![Python](https://img.shields.io/badge/python-3.11+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Streamlit](https://img.shields.io/badge/dashboard-streamlit-red)
![Nasdaq](https://img.shields.io/badge/NASDAQ-AI%20TeraCap-blue)
![S&P500](https://img.shields.io/badge/S&P%20500-Market%20Tracked-green)
![Semiconductors](https://img.shields.io/badge/Semiconductors-AI%20Infrastructure-orange)
![NVDA](https://img.shields.io/badge/NVDA-AI%20Compute-darkgreen)
![AMD](https://img.shields.io/badge/AMD-GPU%20Acceleration-red)
![TSM](https://img.shields.io/badge/TSM-Semiconductor%20Fabrication-blue)
![ASML](https://img.shields.io/badge/ASML-Lithography-purple)
![Python](https://img.shields.io/badge/python-3.11+-blue)
![Streamlit](https://img.shields.io/badge/dashboard-streamlit-red)
![Nasdaq API](https://img.shields.io/badge/data-nasdaq%20api-lightblue)
![Bloomberg](https://img.shields.io/badge/data-bloomberg-black)
# AI TeraCap Market Intelligence Engine

Institutional-grade **AI financial analytics platform** designed to monitor and model the world's largest **AI and semiconductor mega-cap companies**.

The system aggregates market data from **Nasdaq / Yahoo Finance / Bloomberg-style feeds**, computes momentum indicators, detects macro regimes, and estimates long-term **AI TeraCap revenue expansion**.

---

# Core Coverage Universe

Primary companies monitored by the engine:

* **NVDA** — NVIDIA
* **AMD** — Advanced Micro Devices
* **MSFT** — Microsoft
* **AMZN** — Amazon
* **GOOGL** — Alphabet
* **META** — Meta Platforms
* **TSM** — Taiwan Semiconductor Manufacturing
* **ASML** — ASML Holding

These firms represent the **global AI compute and semiconductor infrastructure layer**.

---

# System Architecture

```
ai_teracap_engine
│
├── nasdaq_feed.py
│   Market data ingestion layer
│   (Nasdaq / Yahoo Finance APIs)
│
├── bloomberg_feed.py
│   Institutional-style market data abstraction
│
├── indicators.py
│   Financial indicators
│   - returns
│   - volatility
│   - momentum
│
├── teracap_regime.py
│   Macro AI cycle detection
│   - momentum scoring
│   - bull/bear regime classification
│   - revenue projection model
│
├── ai_teracap_monitor.py
│   CLI monitoring system
│
└── dashboard.py
    Interactive Streamlit dashboard
```

---

# Quant Models Included

### Momentum Engine

Computes cross-asset returns and identifies **AI capital rotation**.

### Regime Detection

Classifies the market into:

* **AI Expansion**
* **Neutral Consolidation**
* **AI Contraction**

### AI TeraCap Index

Synthetic index composed of:

NVDA • AMD • MSFT • AMZN • GOOGL • META • TSM • ASML

Designed to represent the **global AI compute stack**.

### Revenue Projection Model

Projects **16-month forward revenue trajectory** for the AI sector based on momentum regime.

---

# Installation

Clone repository

```
git clone https://github.com/LauroBeck/AI-TeraCap-Engine.git
cd AI-TeraCap-Engine
```

Create environment

```
python -m venv venv
source venv/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

---

# Run CLI Monitor

```
python ai_teracap_monitor.py
```

Example output:

```
AI TERACAP MONITOR

Momentum Score: 0.78
Market Regime: AI Expansion

Projected AI Revenue (16 months):
$1.95 TRILLION
```

---

# Run Dashboard

Launch interactive analytics interface:

```
streamlit run dashboard.py
```

The dashboard provides:

* Live AI TeraCap index
* Momentum analysis
* Market regime classification
* Forward revenue projections

---

# Roadmap

Future modules planned:

* Bloomberg API integration
* Nvidia AI infrastructure metrics
* GPU supply chain modeling
* Macro liquidity indicators
* Institutional portfolio allocation signals

---

# Author

**Lauro Beck**

Financial systems research combining:

* AI analytics
* Capital markets modeling
* Global semiconductor economics
