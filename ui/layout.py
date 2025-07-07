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
    show_filters = False

    # First line: Heading + Filter Icon
    top = st.columns([10, 1])
    with top[0]:
        st.markdown("#### 🔎 Market Scanner")
        st.caption("Scan for classic candlestick patterns across Indian stocks")
    with top[1]:
        if st.button("🧰", help="Add Filters"):
            show_filters = True

    # Second line: Duration + Pattern Type + Pattern + Scan Button
    col1, col2, col3, col4 = st.columns([1.2, 2, 2, 1.2])

    with col1:
        st.markdown("**⏱️ Duration**")
        duration = st.selectbox(
            "", ["15m", "30m", "1d", "1wk"], index=2, label_visibility="collapsed"
        )

    with col2:
        st.markdown("**📂 Pattern Type**")
        pattern_type = st.selectbox(
            "", [
                "Bullish Reversal",
                "Bearish Reversal",
                "Bullish Continuation",
                "Bearish Continuation",
                "Neutral"
            ],
            label_visibility="collapsed"
        )

    with col3:
        st.markdown("**📊 Pattern**")
        pattern_options = {
            "Bullish Reversal": ["Bullish Engulfing", "Hammer", "Morning Star", "Inverted Hammer"],
            "Bearish Reversal": ["Bearish Engulfing", "Shooting Star", "Evening Star"],
            "Bullish Continuation": ["Rising Three", "Upside Tasuki Gap"],
            "Bearish Continuation": ["Falling Three", "Downside Tasuki Gap"],
            "Neutral": ["Doji", "Spinning Top"]
        }
        pattern = st.selectbox(
            "",
            pattern_options.get(pattern_type, []),
            label_visibility="collapsed"
        )

    with col4:
        st.markdown("**&nbsp;**")  # spacer
        scan_clicked = st.button("🔎 Scan Now", use_container_width=True)

    return duration, pattern_type, pattern, show_filters, scan_clicked


# ---------------- Highlights ----------------
def render_highlights(matched_stocks, selected_pattern, duration):
    st.markdown("### 🟢 Highlights")
    if matched_stocks:
        st.success(
            f"🕒 As of {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} "
            f"— Pattern: **{selected_pattern}** on **{duration}** chart"
        )
        st.markdown(f"**{len(matched_stocks)} stocks** formed this pattern today:")
        st.write(", ".join(matched_stocks))
    else:
        st.info("No stocks matched the selected candlestick pattern.")


# ---------------- Results ----------------
def render_results_table(matched_data):
    st.markdown("### 📋 Scan Results")
    if matched_data and not matched_data.empty:
        st.dataframe(
            matched_data,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Symbol": "🔠 Symbol",
                "Name": "🏷️ Stock Name",
                "LTP": "💰 Last Traded Price",
                "Exchange": "🏛️ NSE/BSE",
                "Pattern": "📊 Pattern",
                "Detected On": "⏱️ Chart Duration",
                "Detected At": "📆 Time/Date"
            }
        )
    else:
        st.warning("No results to display.")
