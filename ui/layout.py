# ui/layout.py

import streamlit as st
from datetime import datetime

# ---------------- Mapping ----------------
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

# Reverse map
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


# ---------------- Controls ----------------
def render_top_controls():
    # Ensure session vars exist
    if "pattern_selected" not in st.session_state:
        st.session_state.pattern_selected = None
    if "pattern_type" not in st.session_state:
        st.session_state.pattern_type = ""

    show_filters = False

    # Filter icon top-right
    top_row = st.columns([10, 1])
    with top_row[1]:
        if st.button("🧰", help="Add Filters"):
            show_filters = True

    # Main control line
    col1, col2, col3, col4 = st.columns([1.5, 2, 3, 1])
    
    with col1:
        st.markdown("**⏱️ Duration**")
        duration = st.selectbox("", ["15m", "30m", "1d", "1wk"], index=2, label_visibility="collapsed")

    with col2:
        st.markdown("**🧭 Pattern Type**")
        pattern_type_input = st.selectbox(
            "", [""] + list(pattern_type_map.keys()),
            index=0 if st.session_state.pattern_type == "" else list(pattern_type_map.keys()).index(st.session_state.pattern_type) + 1,
            key="pattern_type_input", label_visibility="collapsed"
        )
        st.session_state.pattern_type = pattern_type_input

    with col3:
        st.markdown("**📊 Pattern**")
        # Filter based on selected type
        available_patterns = (
            pattern_type_map.get(st.session_state.pattern_type, list(pattern_to_type.keys()))
            if st.session_state.pattern_type else list(pattern_to_type.keys())
        )

        pattern = st.selectbox(
            "", options=available_patterns, label_visibility="collapsed",
            key="pattern_dropdown"
        )

        # If user selects a pattern (manually), update the type
        if pattern != st.session_state.pattern_selected:
            st.session_state.pattern_selected = pattern
            inferred_type = pattern_to_type.get(pattern)
            if inferred_type:
                st.session_state.pattern_type = inferred_type

    with col4:
        st.markdown("**&nbsp;**")
        scan_clicked = st.button("🔎 Scan Now", use_container_width=True)

    return duration, st.session_state.pattern_type, st.session_state.pattern_selected, show_filters, scan_clicked


# ---------------- Highlights ----------------
def render_highlights(matched_stocks, selected_pattern):
    st.markdown("### 🟢 Highlights")
    if matched_stocks:
        st.success(f"🕒 As of {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — Pattern: **{selected_pattern}**")
        st.markdown(f"**{len(matched_stocks)} stocks** formed this pattern today:")
        st.write(", ".join(matched_stocks))
    else:
        st.info("No stocks matched the selected candlestick pattern.")


# ---------------- Results ----------------
def render_results_table(data):
    st.markdown("### 📋 Matched Stocks")
    if data is not None and not data.empty:
        st.dataframe(
            data[["Stock Name", "Symbol", "LTP", "Exchange", "Pattern Formed On", "Pattern Duration"]],
            use_container_width=True,
            hide_index=True
        )
    else:
        st.warning("No matching stocks found.")
