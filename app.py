import streamlit as st
import pandas as pd

st.set_page_config(page_title="CandleScanIndia", layout="wide")
st.title("📊 CandleScanIndia - NSE Candlestick Pattern Scanner")

# Show detailed error messages
st.set_option('client.showErrorDetails', True)

# 🔧 Hardcoded NSE stock symbols
stock_symbols = [
    "RELIANCE.NS", "INFY.NS", "TCS.NS", "HDFCBANK.NS", "ICICIBANK.NS",
    "LT.NS", "SBIN.NS", "AXISBANK.NS", "HINDUNILVR.NS", "ITC.NS",
    "BAJFINANCE.NS", "BHARTIARTL.NS", "ASIANPAINT.NS", "KOTAKBANK.NS", "WIPRO.NS",
    "ONGC.NS", "HCLTECH.NS", "SUNPHARMA.NS", "ULTRACEMCO.NS", "POWERGRID.NS",
    "NTPC.NS", "TECHM.NS", "TITAN.NS", "JSWSTEEL.NS", "ADANIENT.NS",
    "COALINDIA.NS", "DIVISLAB.NS", "NESTLEIND.NS", "HDFCLIFE.NS", "TATAMOTORS.NS",
    "BPCL.NS", "CIPLA.NS", "BRITANNIA.NS", "HEROMOTOCO.NS", "GRASIM.NS"
]

# Create a DataFrame from hardcoded symbols
df = pd.DataFrame(stock_symbols, columns=["Symbol"])
st.write(f"✅ Loaded {len(df)} hardcoded stock symbols.")

# 🕯️ Candlestick pattern dropdown
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
    st.success(f"Scanning {len(df)} stocks for pattern: {selected_pattern}...")
    st.info("🔧 Pattern detection engine coming soon.")
