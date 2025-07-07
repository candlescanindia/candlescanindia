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
    col1, col2, col3 = st.columns([2, 1, 1])

    with col1:
        duration = st.selectbox("Chart Duration", ["15m", "30m", "1d", "1wk"], index=2, label_visibility="collapsed")
    with col2:
        show_filters = st.button("🧰", help="Add Filters", use_container_width=True)
    with col3:
        selected_pattern = st.selectbox("Pattern", [
            "Bullish Engulfing", "Bearish Engulfing", "Doji",
            "Hammer", "Inverted Hammer", "Morning Star", "Evening Star"
        ], label_visibility="collapsed")

    return duration, selected_pattern, show_filters

# ---------------- Filters Section ----------------
def render_filters():
    with st.expander("🔽 Add Filters", expanded=True):
        st.text("⚙️ Filter options coming soon (market cap, sector, volume, etc.)")

# ---------------- Highlights Section ----------------
def render_highlights(matched_stocks, selected_pattern):
    st.markdown("### 🟢 Highlights")
    if matched_stocks:
        st.success(f"🕒 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — Pattern: **{selected_pattern}**")
        st.markdown(f"**{len(matched_stocks)} stocks** formed this pattern today:")
        st.write(", ".join(matched_stocks))
    else:
        st.info("No candlestick patterns detected at this time.")

# ---------------- Results Section ----------------
def render_results(matched_stocks, selected_pattern):
    st.markdown("### 🧾 Matched Stocks")
    if matched_stocks:
        for stock in matched_stocks:
            st.success(f"✅ {stock} formed **{selected_pattern}**")
    else:
        st.warning("No matching stocks found.")
