# ui/layout.py

import streamlit as st
from datetime import datetime

# ---------------- Mapping ----------------
PATTERN_MAP = {
    "Bullish Engulfing": "Bullish Reversal",
    "Morning Star": "Bullish Reversal",
    "Hammer": "Bullish Reversal",
    "Bearish Engulfing": "Bearish Reversal",
    "Evening Star": "Bearish Reversal",
    "Inverted Hammer": "Bearish Reversal",
    "Doji": "Neutral"
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

    # First Row: Title + Filter Icon
    top = st.columns([10, 1])
    with top[0]:
        st.markdown("#### 🔎 Market Scanner")
        st.caption("Quickly scan Indian stocks for classic candlestick patterns")
    with top[1]:
        if st.button("🧰", help="Add Filters"):
            show_filters = True

    # Sync State Initialization
    if "selected_pattern" not in st.session_state:
        st.session_state.selected_pattern = list(PATTERN_MAP.keys())[0]
    if "selected_type" not in st.session_state:
        st.session_state.selected_type = PATTERN_MAP[st.session_state.selected_pattern]

    # Second Row: Duration, Pattern Type, Pattern, Scan Button
    col1, col2, col3, col4 = st.columns([1.5, 2, 2.5, 1])
    with col1:
        st.markdown("**⏱️ Duration**")
        duration = st.selectbox("", ["15m", "30m", "1d", "1wk"], index=2, label_visibility="collapsed")

    with col2:
        st.markdown("**📂 Pattern Type**")
        type_options = list(REVERSE_PATTERN_MAP.keys())
        selected_type = st.selectbox(
            "", type_options,
            index=type_options.index(st.session_state.selected_type),
            key="type_select", label_visibility="collapsed"
        )
        st.session_state.selected_type = selected_type

    with col3:
        st.markdown("**📊 Pattern**")
        filtered_patterns = REVERSE_PATTERN_MAP[st.session_state.selected_type]
        selected_pattern = st.selectbox(
            "",
            options=filtered_patterns,
            index=filtered_patterns.index(st.session_state.selected_pattern) if st.session_state.selected_pattern in filtered_patterns else 0,
            key="pattern_select",
            label_visibility="collapsed"
        )
        st.session_state.selected_pattern = selected_pattern
        st.session_state.selected_type = PATTERN_MAP[selected_pattern]

    with col4:
        st.markdown("**&nbsp;**")  # spacing
        scan_clicked = st.button("🔎 Scan Now", use_container_width=True)

    return duration, st.session_state.selected_type, st.session_state.selected_pattern, show_filters, scan_clicked


# ---------------- Highlights ----------------
def render_highlights(matched_stocks, selected_pattern, duration):
    st.markdown("### 🟢 Highlights")
    if matched_stocks:
        st.success(f"🕒 {len(matched_stocks)} stocks matched **{selected_pattern}** pattern on **{duration}** chart.")
        st.markdown(f"⏰ As of {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        st.info("No matching stocks found.")


# ---------------- Results ----------------
def render_results_table(df):
    if not df.empty:
        st.markdown("### 📋 Matched Stocks")
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("No matching results to display.")
