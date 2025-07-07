import streamlit as st
from datetime import datetime
from scans import candlestick
from utils import data_loader
from ui.components import header_section, filter_section, pattern_selector, result_display, highlights_box

# Load stock data
st.set_page_config(page_title="CandleScan India", layout="wide")
df_stocks = data_loader.load_stocks()

# 1. Header
header_section()

# 2. Duration and Filter section
col1, col2 = st.columns([2, 1])
with col1:
    selected_duration = st.selectbox(
        "Select Chart Duration",
        options=["15 min", "30 min", "1 day", "1 week"],
        index=2,
        format_func=lambda x: x.title(),
        key="chart_duration"
    )
with col2:
    filter_section()

# 3. Pattern selection
selected_pattern = pattern_selector()

# 4. Scan button and result
if st.button("🔍 Scan", use_container_width=True):
    matching_stocks = []
    current_time = datetime.now().strftime("%d-%b-%Y %I:%M %p")

    with st.spinner("Scanning stocks..."):
        for symbol in df_stocks["symbol"]:
            try:
                scan_func = getattr(candlestick, f"scan_{selected_pattern.lower().replace(' ', '_')}")
                if scan_func(symbol):
                    matching_stocks.append(symbol)
            except Exception as e:
                st.warning(f"Error scanning {symbol}: {e}")

    result_display(selected_pattern, matching_stocks, current_time)
    highlights_box(selected_pattern, matching_stocks)
else:
    st.markdown("<br>", unsafe_allow_html=True)
    highlights_box(None, [])
