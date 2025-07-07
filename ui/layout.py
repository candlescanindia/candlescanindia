# ui/layout.py

import streamlit as st
from datetime import datetime

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


# ---------------- Chart Duration Selector ----------------
def render_chart_duration_selector():
    durations = ["15m", "30m", "1h", "1d", "1wk"]
    return st.selectbox("⏱️ Chart Duration", durations, index=3)


# ---------------- Filters ----------------
def render_filters():
    with st.expander("➕ Add Optional Filters"):
        st.checkbox("Market Cap: Large Cap Only")
        st.checkbox("Volume: Above 1M")
        st.checkbox("Price: Above ₹500")
        st.info("More filters will be added soon.")
    return True  # Placeholder return


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
    return st.selectbox("📊 Select Candlestick Pattern", patterns)


# ---------------- Highlights Section ----------------
def render_highlights(matched_stocks, selected_pattern):
    st.markdown("### 🟢 Highlights")
    if matched_stocks:
        st.success(f"🕒 As of {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — Pattern: **{selected_pattern}**")
        st.markdown(f"**{len(matched_stocks)} stocks** formed this pattern today:")
        st.write(", ".join(matched_stocks))
    else:
        st.info("No matching stocks found yet.")
