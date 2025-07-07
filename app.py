import streamlit as st
from utils import data_loader
from scans import candlestick
from datetime import datetime

# Load stock data
df_stocks = data_loader.load_stocks()
stock_list = df_stocks["symbol"].tolist()

# Available chart durations
interval_map = {
    "15 minutes": "15m",
    "Daily": "1d",
    "Weekly": "1wk"
}

# Optional filters (for now placeholder)
market_caps = ["All", "Large Cap", "Mid Cap", "Small Cap"]

# Available patterns
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

# ----- Streamlit Layout -----
st.set_page_config(page_title="CandleScan India", layout="centered")
st.markdown("## 📊 CandleScan India")
st.markdown("Smart scanner for Indian stocks based on candlestick patterns")

# --- Top Two Columns ---
top_col1, top_col2 = st.columns([1, 1])

with top_col1:
    selected_interval = st.selectbox("🕒 Select Chart Duration", list(interval_map.keys()), key="interval")

with top_col2:
    selected_market_cap = st.selectbox("🏢 Filter by Market Cap", market_caps, key="marketcap")

# --- Pattern Selection and Button ---
st.markdown("### 🔎 Scan for Candlestick Pattern")
selected_pattern = st.selectbox(
    "Select Pattern",
    list(pattern_functions.keys()),
    index=0,
    key="pattern"
)

scan_btn = st.button("🚀 Start Scan")

# --- Scan Logic ---
if scan_btn:
    interval = interval_map[selected_interval]
    pattern_fn = pattern_functions[selected_pattern]

    st.info(f"🔄 Scanning {len(stock_list)} stocks on **{selected_interval}** interval for **{selected_pattern}**...")

    matched = []
    for symbol in stock_list:
        try:
            if pattern_fn(symbol, period="5d", interval=interval):
                matched.append((symbol, datetime.now().strftime("%Y-%m-%d %H:%M")))
        except Exception as e:
            st.warning(f"{symbol}: {e}")

    # --- Display Result Box ---
    st.markdown("---")
    if matched:
        count = len(matched)
        with st.expander(f"✅ {count} stocks formed {selected_pattern} today (Click to expand)", expanded=True):
            for sym, dt in matched:
                st.markdown(f"- **{sym}** — _Detected on {dt}_")
    else:
        st.error("❌ No stocks found matching the selected pattern.")
