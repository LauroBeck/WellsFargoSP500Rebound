import streamlit as st

from nasdaq_feed import get_market_data
from indicators import compute_returns
from teracap_regime import detect_regime, revenue_projection
from teracap_index import build_teracap_index


st.title("AI TERACAP TERMINAL")

# Load market data
data = get_market_data()

# Compute returns table
df = compute_returns(data)

# Detect AI market regime
regime, momentum = detect_regime(df)

# Revenue projection
future_rev = revenue_projection()

# Build TERACAP index
index_df = build_teracap_index(data)

st.subheader("Market Snapshot")
st.dataframe(df.round(2))

st.subheader("Momentum Signal")

st.write("Momentum:", round(momentum,2))
st.write("Regime:", regime)

st.subheader("Projected AI Revenue (16 months)")
st.write(f"${future_rev/1e12:.2f} TRILLION")

st.subheader("AI TERACAP INDEX")

st.line_chart(index_df["TERACAP_INDEX"])
