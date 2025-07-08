# ui/layout.py

import streamlit as st
import pandas as pd
from datetime import datetime
from utils.nse_stock_list import fetch_nse_stock_list

# ---------------- Pattern Maps ----------------
pattern_type_map = {
    "Bullish Reversal": [
        "Bullish Engulfing", "Hammer", "Inverted Hammer", "Morning Star", "Piercing Line",
        "Three White Soldiers", "Tweezer Bottom", "Inverted Hammer", "Bullish Harami"
    ],
    "Bearish Reversal": [
        "Bearish Engulfing", "Evening Star", "Hanging Man", "Shooting Star", "Dark Cloud Cover",
        "Three Black Crows", "Tweezer Top", "Bearish Harami"
    ],
    "Neutral": [
        "Doji", "Dragonfly Doji", "Gravestone Doji", "Spinning Top"
    ]
}

pattern_to_type = {
    pattern: ptype
    for ptype, patterns in pattern_type_map.items()
    for pattern in patterns
}

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
    st.session_state.setdefault("pattern_selected", "")
    st.session_state.setdefault("pattern_type", "Show All")

    show_filters = False

    # Filter icon
    top_row = st.columns([10, 1])
    with top_row[1]:
        if st.button("🧰", help="Add Filters"):
            show_filters = True

    # Control panel
    col1, col2, col3, col4 = st.columns([1.5, 2, 3, 1])

    with col1:
        st.markdown("**⏱️ Duration**")
        duration = st.selectbox(
            "", ["15m", "30m", "1d", "1wk"],
            index=2, key="duration", label_visibility="collapsed"
        )

    with col2:
        st.markdown("**🧭 Pattern Type**")
        selected_type = st.selectbox(
            "", ["Show All"] + list(pattern_type_map.keys()),
            index=(["Show All"] + list(pattern_type_map.keys())).index(st.session_state.pattern_type),
            key="pattern_type_input", label_visibility="collapsed"
        )
        st.session_state.pattern_type = selected_type

    with col3:
        st.markdown("**📊 Pattern**")
        available_patterns = (
            pattern_type_map.get(selected_type, list(pattern_to_type.keys()))
            if selected_type != "Show All" else list(pattern_to_type.keys())
        )

        selected_pattern = st.selectbox(
            "", sorted(available_patterns), key="pattern_dropdown", label_visibility="collapsed"
        )

        if selected_pattern != st.session_state.pattern_selected:
            st.session_state.pattern_selected = selected_pattern
            st.session_state.pattern_type = pattern_to_type.get(selected_pattern, "Show All")

    with col4:
        st.markdown("**&nbsp;**")
        scan_clicked = st.button("🔎 Scan Now", use_container_width=True)

    # Stock list preview with new NSE fetcher
   with st.expander("🔍 Preview NSE Stock List"):
        stock_list = fetch_nse_stock_list()
        if stock_list:
            df = pd.DataFrame(stock_list)
            st.success(f"✅ Fetched {len(df)} stocks from CSV")
            st.dataframe(df.head(50), use_container_width=True)
        else:
            st.error("⚠️ Could not load stock data. Please check the CSV format.")
    return duration, st.session_state.pattern_type, st.session_state.pattern_selected, show_filters, scan_clicked
