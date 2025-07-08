# ui/layout.py

import streamlit as st
from datetime import datetime

# ---------------- Candlestick Pattern Mapping ----------------
pattern_type_map = {
    "Bullish Reversal": [
        "Bullish Engulfing", "Hammer", "Inverted Hammer", "Morning Star"
    ],
    "Bearish Reversal": [
        "Bearish Engulfing", "Evening Star", "Hanging Man", "Shooting Star"
    ],
    "Neutral": [
        "Doji", "Spinning Top"
    ]
}

# Inverse mapping for auto-selecting type when pattern is selected
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


# ---------------- Scan Controls ----------------
def render_top_controls():
    show_filters = False

    # Filter icon on right
    filter_col = st.columns([10, 1])
    with filter_col[1]:
        if st.button("🧰", help="Add Filters"):
            show_filters = True

    # Duration + Pattern Type + Pattern + Scan
    col1, col2, col3, col4 = st.columns([1.5, 2, 3, 1])
    
    with col1:
        st.markdown("**⏱️ Duration**")
        duration = st.selectbox("", ["15m", "30m", "1d", "1wk"], index=2, label_visibility="collapsed")

    with col2:
        st.markdown("**🧭 Pattern Type**")
        pattern_type = st.selectbox(
            "", [""] + list(pattern_type_map.keys()),
            index=0, key="pattern_type", label_visibility="collapsed"
        )

    with col3:
        st.markdown("**📊 Pattern**")
        # Filter patterns if type is selected
        if pattern_type:
            available_patterns = pattern_type_map.get(pattern_type, [])
        else:
            # Show all
            available_patterns = list(pattern_to_type.keys())

        pattern = st.selectbox(
            "",
            available_patterns,
            key="pattern", label_visibility="collapsed",
            index=0 if available_patterns else None
        )

        # Auto-select pattern_type if pattern was chosen
        if pattern and not pattern_type:
            detected_type = pattern_to_type.get(pattern)
            if detected_type:
                st.session_state["pattern_type"] = detected_type

    with col4:
        st.markdown("**&nbsp;**")
        scan_clicked = st.button("🔎 Scan Now", use_container_width=True)

    return duration, st.session_state.get("pattern_type", ""), pattern, show_filters, scan_clicked


# ---------------- Highlights ----------------
def render_highlights(matched_stocks, selected_pattern):
    st.markdown("### 🟢 Highlights")
    if matched_stocks:
        st.success(f"🕒 As of {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — Pattern: **{selected_pattern}**")
        st.markdown(f"**{len(matched_stocks)} stocks** formed this pattern today:")
        st.write(", ".join(matched_stocks))
    else:
        st.info("No stocks matched the selected candlestick pattern.")


# ---------------- Results Table ----------------
def render_results_table(data):
    st.markdown("### 📋 Matched Stocks")
    if data and not data.empty:
        st.dataframe(
            data[["Stock Name", "Symbol", "LTP", "Exchange", "Pattern Formed On", "Pattern Duration"]],
            use_container_width=True,
            hide_index=True
        )
    else:
        st.warning("No matching stocks found.")
