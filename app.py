# app.py
import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

st.set_page_config(page_title="CandleScanIndia – NSE Candlestick Pattern Scanner", layout="wide")

# Header
st.markdown("""
# 📈 CandleScanIndia
### Discover NSE Stocks Forming Popular Candlestick Patterns
Select a candlestick pattern to view live stocks from NIFTY 50 that match the formation.
""")

# Sidebar Info
with st.sidebar:
    st.markdown("## 🛠 Features")
    st.markdown("- Real-time stock scanning")
    st.markdown("- Top NSE stocks")
    st.markdown("- Over 12 candlestick patterns")
    st.markdown("- Lightweight & responsive UI")
    st.markdown("---")
    st.markdown("© 2025 CandleScanIndia")

# Pattern list
pattern_list = [
    "Doji", "Hammer", "Inverted Hammer", "Bullish Engulfing", "Bearish Engulfing",
    "Morning Star", "Evening Star", "Shooting Star", "Hanging Man", "Spinning Top",
    "Marubozu", "Piercing Line", "Dark Cloud Cover"
]

# Searchable pattern dropdown
selected_pattern = st.selectbox("🔍 Search & Select Pattern", options=pattern_list)

# Stock symbols
ni
