import streamlit as st
import pandas as pd
from scans import candlestick

st.set_page_config(page_title="CandleScan India", layout="centered")

st.markdown(
    "<h2 style='text-align:center;'>🕯️ CandleScan India</h2>", 
    unsafe_allow_html=True
)
st.markdown("<p style='text-align:center;'>Smart scanner for Indian stocks based on candlestick patterns</p>", unsafe_allow_html=True)

# Load stocks from CSV
try:
    df_stocks = pd.read_csv("data/nse_stock_list.csv")
    stock_list = df_stocks["Symbol"].dropna().tolist()
except FileNotFoundError:
    st.error("Stock list not found. Please add 'data/nse_stock_list.csv'.")
    st.stop()

# Pattern list from candlestick module
pattern_map = {
    "Hammer": candlestick.scan_hammer,
    "Inverted Hammer": candlestick.scan_inverted_hammer,
    "Doji": candlestick.scan_doji,
    "Bullish Engulfing": candlestick.scan_bullish_engulfing,
    "Bearish Engulfing": candlestick.scan_bearish_engulfing,
    "Morning Star": candlestick.scan_morning_star,
    "Shooting Star": candlestick.scan_shooting_star,
    "Evening Star": candlestick.scan_evening_star,
    "Hanging Man": candlestick.scan_hanging_man,
    "Spinning Top": candlestick.scan_spinning_top,
}

st.markdown("### 🔍 Select a Candlestick Pattern")
selected_pattern = st.selectbox(
    "Start typing to search...",
    options=list(pattern_map.keys()),
    index=0
)

# Optional: date range or duration for candle
st.markdown("### 📅 Select Candle Duration")
duration = st.radio("Select time range", ["5d", "10d", "1mo"], horizontal=True)

st.markdown("---")
st.markdown("### 📊 Scan Results")

scanner_function =_
