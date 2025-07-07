# ui/components/layout.py
import streamlit as st
from datetime import datetime
# from st_pages import add_indented_title  # optional, remove if unused

def header_section():
    st.markdown("""
        <div style='display: flex; align-items: center; justify-content: space-between;'>
            <div>
                <h1 style='margin-bottom: 0;'>📊 CandleScan India</h1>
                <p style='margin-top: 0; color: gray;'>Smart scanner for Indian stocks based on candlestick patterns</p>
            </div>
        </div>
    """, unsafe_allow_html=True)


def filter_section():
    with st.expander("⚙️ Filters", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            st.selectbox("Market Cap", ["All", "Large Cap", "Mid Cap", "Small Cap"], index=0)
        with col2:
            st.selectbox("Sector", ["All", "IT", "Banking", "Pharma", "Auto", "FMCG"], index=0)
    return True


def pattern_selector():
    pattern = st.selectbox(
        "Select Candlestick Pattern",
        [
            "Hammer", "Inverted Hammer", "Doji", "Bullish Engulfing", "Bearish Engulfing",
            "Morning Star", "Evening Star", "Shooting Star", "Hanging Man", "Spinning Top", "Marubozu"
        ],
        index=0
    )
    return pattern

