# ui/layout.py

import streamlit as st

# ---------------- Pattern Maps ----------------
pattern_type_map = {
    "Bullish Reversal": ["Bullish Engulfing", "Hammer", "Inverted Hammer", "Morning Star"],
    "Bearish Reversal": ["Bearish Engulfing", "Evening Star", "Hanging Man", "Shooting Star"],
    "Neutral": ["Doji", "Spinning Top"]
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

# ---------------- Controls ----------------
def render_top_controls():
    if "pattern_selected" not in st.session_state:
        st.session_state.pattern_selected = ""
    if "pattern_type" not in st.session_state:
        st.session_state.pattern_type = "Show All"

    col1, col2, col3, col4 = st.columns([1.5, 2, 3, 1])

    with col1:
        st.markdown("**⏱️ Duration**")
        duration = st.selectbox("", ["15m", "30m", "1d", "1wk"], index=2, label_visibility="collapsed")

    with col2:
        st.markdown("**🧭 Pattern Type**")
        pattern_type_input = st.selectbox(
            "", ["Show All"] + list(pattern_type_map.keys()),
            index=(["Show All"] + list(pattern_type_map.keys()]).index(st.session_state.pattern_type),
            key="pattern_type_input", label_visibility="collapsed"
        )
        st.session_state.pattern_type = pattern_type_input

    with col3:
        st.markdown("**📊 Pattern**")
        available_patterns = (
            pattern_type_map.get(st.session_state.pattern_type, list(pattern_to_type.keys()))
            if st.session_state.pattern_type != "Show All" else list(pattern_to_type.keys())
        )

        pattern = st.selectbox(
            "", options=sorted(available_patterns), key="pattern_dropdown", label_visibility="collapsed"
        )

        if pattern and pattern != st.session_state.pattern_selected:
            st.session_state.pattern_selected = pattern
            st.session_state.pattern_type = pattern_to_type.get(pattern, "Show All")

    with col4:
        st.markdown("**&nbsp;**")
        scan_clicked = st.button("🔎 Scan Now", use_container_width=True)

    return duration, st.session_state.pattern_type, st.session_state.pattern_selected, False, scan_clicked
