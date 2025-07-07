# ui/layout.py

import streamlit as st
from datetime import datetime

# Sample pattern mapping (replace with your actual mappings)
PATTERN_MAP = {
    "Bullish Engulfing": "Bullish Reversal",
    "Bearish Engulfing": "Bearish Reversal",
    "Doji": "Neutral",
    "Hammer": "Bullish Reversal",
    "Inverted Hammer": "Bullish Reversal",
    "Morning Star": "Bullish Reversal",
    "Evening Star": "Bearish Reversal"
}

REVERSE_PATTERN_MAP = {}
for pattern, ptype in PATTERN_MAP.items():
    REVERSE_PATTERN_MAP.setdefault(ptype, []).append(pattern)

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

    # Top: Heading + Filter icon
    top = st.columns([10, 1])
    with top[0]:
        st.markdown("#### 🔎 Market Scanner")
        st.caption("Quickly scan Indian stocks for classic candlestick patterns")
    with top[1]:
        if st.button("🧰", help="Add Filters"):
            show_filters = True

    # Initialize session state
    if "selected_pattern" not in st.session_state:
        st.session_state.selected_pattern = list(PATTERN_MAP.keys())[0]
    if "selected_type" not in st.session_state:
        st.session_state.selected_type = PATTERN_MAP[st.session_state.selected_pattern]

    # Pattern change callback
    def on_pattern_change():
        st.session_state.selected_type = PATTERN_MAP[st.session_state.selected_pattern]

    # Type change callback
    def on_type_change():
        filtered_patterns = REVERSE_PATTERN_MAP[st.session_state.selected_type]
        if st.session_state.selected_pattern not in filtered_patterns:
            st.session_state.selected_pattern = filtered_patterns[0]

    # Controls row
    col1, col2, col3, col4 = st.columns([1.5, 2, 2.5, 1])

    with col1:
        st.markdown("**⏱️ Duration**")
        duration = st.selectbox("", ["15m", "30m", "1d", "1wk"], index=2, label_visibility="collapsed")

    with col2:
        st.markdown("**📂 Pattern Type**")
        st.selectbox(
            "",
            list(REVERSE_PATTERN_MAP.keys()),
            key="selected_type",
            on_change=on_type_change,
            label_visibility="collapsed"
        )

    with col3:
        st.markdown("**📊 Pattern**")
        st.selectbox(
            "",
            options=REVERSE_PATTERN_MAP[st.session_state.selected_type],
            key="selected_pattern",
            on_change=on_pattern_change,
            label_visibility="collapsed"
        )

    with col4:
        st.markdown("**&nbsp;**")
        scan_clicked = st.button("🔎 Scan Now", use_container_width=True)

    return (
        duration,
        st.session_state.selected_type,
        st.session_state.selected_pattern,
        show_filters,
        scan_clicked
    )


# ---------------- Highlights Section ----------------
def render_highlights(matched_stocks, selected_pattern):
    st.markdown("### 🟢 Highlights")
    if matched_stocks:
        st.success(f"🕒 As of {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — Pattern: **{selected_pattern}**")
        st.markdown(f"**{len(matched_stocks)} stocks** formed this pattern today:")
        st.write(", ".join(matched_stocks))
    else:
        st.info("No stocks matched the selected candlestick pattern.")


# ---------------- Results ----------------
def render_results_table(matched_stocks_info):
    st.markdown("### 📋 Results Table")
    if matched_stocks_info:
        st.dataframe(matched_stocks_info, use_container_width=True)
    else:
        st.warning("No results found for selected pattern.")
