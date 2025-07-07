# ui/layout.py

import streamlit as st

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


# ---------------- Pattern Selector ----------------
def render_pattern_selector():
    patterns = [
        "Bullish Engulfing",
        "Bearish Engulfing",
        "Doji",
        "Hammer",
        "Inverted Hammer",
        "Morning Star",
        "Evening Star"
    ]
    selected_pattern = st.selectbox("📊 Select Candlestick Pattern", patterns)
    return selected_pattern


# ---------------- Search Bar ----------------
def render_search_bar():
    search_query = st.text_input(
        "🔍 Search stock symbol",
        placeholder="Type stock symbol (e.g. RELIANCE)",
        label_visibility="collapsed"
    )
    return search_query
