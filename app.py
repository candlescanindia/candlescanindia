import streamlit as st
from utils import data_loader
from scans import candlestick
from datetime import datetime

# Load stock symbols
df_stocks = data_loader.load_stocks()
stock_list = df_stocks["symbol"].tolist()

# Supported intervals for yfinance
interval_map = {
    "15 minutes": "15m",
    "Daily": "1d",
    "Weekly": "1wk"
}

pattern_functions = {
    "Hammer": candlestick.scan_hammer,
    "Inverted Hammer": candlestick.scan_inverted_hammer,
    "Doji": candlestick.scan_doji,
    "Bullish Engulfing": candlestick.scan_bullish_engulfing,
    "Bearish Engulfing": candlestick.scan_bearish_engulfing,
    "Morning Star": candlestick.scan_morning_star,
    "Evening Star": candlestick.scan_evening_star,
    "Shooting Star": candlestick.scan_shooting_star,
    "Hanging Man": candlestick.scan_hanging_man,
    "Spinning Top": candlestick.scan_spinning_top,
    "Marubozu": candlestick.scan_marubozu
}

# --- UI ---
st.set_page_config(page_title="CandleScan India", layout="centered")
st.markdown("### 📈 CandleScan India")
st.markdown("_Smart scanner for Indian stocks based on candlestick patterns_")

col1, col2 = st.columns(2)
with col1:
    selected_interval = st.selectbox("Chart Duration", list(interval_map.keys()))
with col2:
    selected_pattern = st.selectbox("Select Candlestick Pattern", list(pattern_functions.keys()))

if st.button("🔍 Scan"):
    st.info(f"Scanning {len(stock_list)} stocks for **{selected_pattern}** pattern on **{selected_interval}** charts...")

    matched_stocks = []
    pattern_fn = pattern_functions[selected_pattern]
    interval = interval_map[selected_interval]

    for symbol in stock_list:
        try:
            result = pattern_fn(symbol, period="5d", interval=interval)
            if result:
                matched_stocks.append((symbol, datetime.now().strftime("%Y-%m-%d %H:%M")))
        except Exception as e:
            st.warning(f"{symbol}: {e}")

    if matched_stocks:
        count = len(matched_stocks)
        with st.expander(f"✅ {count} stocks formed {selected_pattern} pattern today. Click to view"):
            for symbol, timestamp in matched_stocks:
                st.markdown(f"**{symbol}** — Detected on `{timestamp}`")
    else:
        st.error(f"No stock found with {selected_pattern} pattern.")
