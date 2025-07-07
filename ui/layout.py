# ui/layout.py

import streamlit as st
from datetime import datetime
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.emoji_icons import emoji

# ---------------- Header ----------------
def render_header():
    st.markdown("""
        <style>
        .main-title {
            font-size: 2.2rem;
            font-weight: 800;
            color: #1f4e79;
        }
        .sub-title {
            font-size: 1rem;
            color: #666;
        }
        </style>
        <div class="main-title">📈 CandleScan India</div>
        <div class="sub-title">Scan the entire Indian market for live candlestick patterns</div>
    """, unsafe_allow_html=True)
    st.markdown("---")


# ---------------- Controls Row ----------------
def render_top_controls():
    col_icon, _, _ = st.columns([0.3, 4, 2])
    with col_icon:
        show_filters = st.toggle("🧰", label_visibility="collapsed", key="filter_toggle")

    col1, col2 = st.columns([2, 3])
    with col1:
        duration = st.selectbox("Duration", ["15m", "30m", "1d", "1wk"], index=2)

    with col2:
        patterns = [
            "Bullish Engulfing",
