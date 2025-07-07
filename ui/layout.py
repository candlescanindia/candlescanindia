# ui/layout.py

import streamlit as st
from datetime import datetime
from streamlit_extras.stylable_container import stylable_container

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


# ---------------- Top Controls ----------------
def render_top_controls():
    col_icon, col1, col2 = st.columns([0.4, 2.5, 3])
    
    # Filter icon toggle (top-left)
    with col_icon:
        show_filters = st.toggle("🔽", label_visibility="collapsed", key="filter_toggle")

    # Chart duration
    with col1:
        duration = st.selectbox("Chart Duration", ["15m", "30m", "1d", "1wk"], index=2)

    # Candlestick pattern
    with col2:
        patterns = [
            "Bullish Engulfing",
            "Bearish Engulfing",
            "Doji",
            "Hammer",
            "Inverted Hammer",
            "Morning Star",
            "Evening Star"
        ]
        selected_pattern = st.selectbox("Candlestick Pattern", patterns)

    return duration, selected_pattern, show_filters


# ---------------- Filters ----------------
def render_filters():
    with st.expander("⚙️ Advanced Filters"):
        st.info("More filters coming soon (e.g. sector, volume, market cap, etc.)")


# ---------------- Scan Section Heading ----------------
def render_scan_heading():
    st.markdown("## 🔎 Scan Results")


# ---------------- Highlights Section ----------------
def render_highlights(matched_stocks, selected_pattern):
    st.markdown("### 🟢 Highlights")
    if matched_stocks:
        st.success(f"🕒 As of {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — Pattern: **{selected_pattern}**")
        st.markdown(f"**{len(matched_stocks)} stocks** formed this pattern today:")
        st.write(", ".join(matched_stocks))
    else:
        st.info("No stocks matched the selected pattern.")


# ---------------- Results Section ----------------
def render_results(matched_stocks, selected_pattern):
    st.markdown("### 🧾 Matched Stocks")
    if matched_stocks:
        for stock in matched_stocks:
            st.success(f"✅ {stock} formed **{selected_pattern}** pattern.")
    else:
        st.warning("No matching stocks found.")
