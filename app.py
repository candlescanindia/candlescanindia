import streamlit as st
from scans import candlestick, volume_scans, price_scans, trend_scans, combo_scanner
from utils import nse_data

st.set_page_config(page_title="CandleScan India", layout="wide")
st.title("📊 CandleScan India — All-In-One Stock Scanner")

df_stocks = nse_data.load_stocks()

# Sidebar filters
st.sidebar.header("Filter Options")
selected_pattern = st.sidebar.selectbox("Select Candlestick Pattern", candlestick.get_patterns())
market_cap_filter = st.sidebar.selectbox("Market Cap", ["All", "Large", "Mid", "Small"])
volume_threshold = st.sidebar.slider("Min Volume", min_value=0, max_value=10000000, value=100000)

# Main Scans
st.subheader("🔎 Candlestick Pattern Scan")
candlestick.render(df_stocks, selected_pattern)

st.subheader("📈 Price Action Scans")
price_scans.render(df_stocks)

st.subheader("📊 Volume Based Scans")
volume_scans.render(df_stocks, volume_threshold)

st.subheader("🔥 Trending Stocks")
trend_scans.render(df_stocks)

st.subheader("🧠 Combined Strategy Scan")
combo_scanner.render(df_stocks)
