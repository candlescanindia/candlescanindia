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


# ---------------- Scan Controls (Top Row) ----------------
def render_top_controls():
    show_filters = False

    # Top-right Filter Icon
    filter_col = st.columns([10, 1])
    with filter_col[1]:
        if st.button("🧰", help="Add Filters"):
            show_filters = True

    # Scan Line: Duration + Pattern + Scan Button
    col1, col2, col3 = st.columns([1.2, 2.2, 1])
    with col1:
        duration = st.selectbox("⏱️", ["15m", "30m", "1d", "1wk"], index=2, label_visibility="collapsed")
    with col2:
        pattern = st.selectbox(
            "📊",
            [
                "Bullish Engulfing", "Bearish Engulfing", "Doji", "Hammer",
                "Inverted Hammer", "Morning Star", "Evening Star"
            ],
            label_visibility="collapsed"
        )
    with col3:
        st.markdown("<div style='padding-top: 10px'></div>", unsafe_allow_html=True)
        scan_clicked = st.button("🔎 Scan Now", use_container_width=True)

    return duration, pattern, show_filters, scan_clicked


# ---------------- Optional Filters ----------------
def render_filters():
    with st.expander("⚙️ Advanced Filters"):
        st.info("Filter options coming soon (e.g. price, volume, sector, etc.)")


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
