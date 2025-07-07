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


# ---------------- Scan Controls ----------------
def render_top_controls():
    show_filters = st.session_state.get("show_filters", False)

    # Top line: Heading + Filter icon (right-aligned)
    top = st.columns([10, 1])
    with top[0]:
        st.markdown("#### 🔎 Market Scanner")
        st.caption("Quickly scan Indian stocks for classic candlestick patterns")
    with top[1]:
        if st.button("🧰", key="filter_toggle", help="Add Filters"):
            st.session_state["show_filters"] = not show_filters
            show_filters = not show_filters

    # Floating filter container
    if show_filters:
        st.markdown("""
            <style>
                .floating-filter {
                    background-color: #f9f9f9;
                    border: 1px solid #ddd;
                    padding: 10px;
                    border-radius: 10px;
                    box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
                    position: fixed;
                    top: 90px;
                    right: 16px;
                    width: 220px;
                    font-size: 0.85rem;
                    z-index: 1000;
                }
                @media only screen and (max-width: 600px) {
                    .floating-filter {
                        right: 10px;
                        top: 80px;
                        width: 85%;
                    }
                }
            </style>
            <div class="floating-filter">
        """, unsafe_allow_html=True)
        with st.container():
            st.markdown("**🔧 Filter Options**")
            st.checkbox("NSE only", key="filter_nse")
            st.checkbox("BSE only", key="filter_bse")
            st.checkbox("Price > 100", key="filter_price")
            st.checkbox("Volume > 1L", key="filter_volume")
        st.markdown("</div>", unsafe_allow_html=True)

    # Second line: Duration + Pattern + Button (in same line)
    col1, col2, col3 = st.columns([1.5, 2.5, 1])
    with col1:
        st.markdown("**⏱️ Chart Duration**")
        duration = st.selectbox(
            "", ["15m", "30m", "1d", "1wk"],
            index=2,
            label_visibility="collapsed"
        )

    with col2:
        st.markdown("**📊 Pattern**")
        pattern = st.selectbox(
            "", [
                "Bullish Engulfing", "Bearish Engulfing", "Doji", "Hammer",
                "Inverted Hammer", "Morning Star", "Evening Star"
            ],
            label_visibility="collapsed"
        )

    with col3:
        st.markdown("**&nbsp;**")  # for vertical spacing
        scan_clicked = st.button("🔎 Scan Now", use_container_width=True)

    return duration, pattern, show_filters, scan_clicked


# ---------------- Highlights Section ----------------
def render_highlights(matched_stocks, selected_pattern):
    st.markdown("### 🟢 Highlights")
    if matched_stocks:
        st.success(f"🕒 As of {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — Pattern: **{selected_pattern}**")
        st.markdown(f"**{len(matched_stocks)} stocks** formed this pattern today:")
        st.write(", ".join(matched_stocks))
    else:
        st.info("No stocks matched the selected candlestick pattern.")


# ---------------- Results Table ----------------
def render_results_table(results):
    st.markdown("### 📋 Matched Stocks Table")
    if results and isinstance(results, list):
        st.dataframe(results, use_container_width=True)
    else:
        st.warning("No matching results to display.")
