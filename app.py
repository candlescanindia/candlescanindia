import streamlit as st
import pandas as pd

st.set_page_config(page_title="CandleScanIndia", layout="wide")
st.title("📊 CandleScanIndia - NSE Candlestick Pattern Scanner")

# Show error details in UI
st.set_option('client.showErrorDetails', True)

# Load CSV
try:
    df = pd.read_csv("nse_stocks.csv")
    st.write(f"✅ Loaded {len(df)} stock symbols.")
except Exception as e:
    st.error(f"❌ Could not load nse_stocks.csv: {e}")
    st.stop()

# Patterns dropdown
pattern_list = [
    "Hammer",
    "Doji",
    "Inverted Hammer",
    "Shooting Star",
    "Bullish Engulfing",
    "Bearish Engulfing",
    "Morning Star",
    "Evening Star",
    "Marubozu",
    "Hanging Man",
    "Spinning Top"
]

# UI dropdown
selected_pattern = st.selectbox("🔎 Select a Candlestick Pattern", pattern_list)

# Trigger button
if st.button("🔍 Run Scan"):
    st.success(f"Scanning {len(df)} sto
