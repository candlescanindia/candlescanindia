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
    show_filters = False
    with st.container():
        # Filter Icon
        col_icon, col_space = st.columns([0.1, 0.9])
        with col_icon:
            if st.button("⚙️", help="Add Filters"):
                show_filters = True

        # Main scan controls in a row
        col1, col2, col3 = st.columns([1.5, 2, 1])
        with col1:
            duration = st.selectbox("Duration", ["15m", "30m", "1d", "1wk"], index=2, label_visibility="collapsed")
        with col2:
            pattern = st.selectbox("Candlestick Pattern", [
                "Bullish Engulfing", "Bearish Engulfing", "Doji", "Hammer",
                "Inverted Hammer", "Morning Star", "Evening Star"
            ], label_visibility="collapsed")
        with col3:
            st.markdown("###")  # Push button down slightly
            scan_clicked = st.button("🔎 Scan Now", use_container_width=True)

    return duration, pattern, show_filters, scan_clicked


# ---------------- Optional Filters Section ----------------
def render_filters():
    with st.expander("🧰 Advanced Filters"):
        st.info("Filter options coming soon (e.g. market cap, price, volume, sector, etc.)")


# ---------------- Section Heading ----------------
def render_scan_heading():
    st.markdown("### 🔍 Scan Results")


# ---------------- Highlights ----------------
def render_highlights(matched_stocks, selected_pattern):
    st.markdown("### 🟢 Highlights")
    if matched_stocks:
        st.success(f"🕒 As of {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — Pattern: **{selected_pattern}**")
        st.markdown(f"**{len(matched_stocks)} stocks** formed this pattern today:")
        st.write(", ".join(matched_stocks))
    else:
        st.info("No matching stocks found for this pattern.")


# ---------------- Results ----------------
def render_results(matched_stocks, selected_pattern):
    st.markdown("### 🧾 Matched Stocks")
    if matched_stocks:
        for stock in matched_stocks:
            st.success(f"✅ {stock} formed **{selected_pattern}** pattern.")
    else:
        st.warning("No matching stocks found.")
