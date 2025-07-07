import streamlit as st
from datetime import datetime
from streamlit_extras.stylable_container import stylable_container  # Optional if you want custom styling

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
        .dropdown-row > div {
            display: inline-block;
            margin-right: 1rem;
        }
        .filter-icon {
            font-size: 1.5rem;
            cursor: pointer;
        }
        </style>
        <div class="main-title">📈 CandleScan India</div>
        <div class="sub-title">Scan the entire Indian market for live candlestick patterns</div>
    """, unsafe_allow_html=True)
    st.markdown("---")


# ---------------- Top Controls: Duration + Filter Icon ----------------
def render_top_controls():
    col1, col2 = st.columns([4, 1])
    with col1:
        duration = st.selectbox("⏱️", ["15m", "30m", "1h", "1d", "1wk"], index=3, label_visibility="collapsed")
    with col2:
        filter_clicked = st.button("⚙️", help="Click to open filters", use_container_width=True)
    return duration, filter_clicked


# ---------------- Filters Panel ----------------
def render_filters_panel():
    with st.expander("⚙️ Filters", expanded=True):
        st.checkbox("Market Cap: Large Cap Only")
        st.checkbox("Volume: Above 1M")
        st.checkbox("Price: Above ₹500")
        st.info("More filters will be added soon.")


# ---------------- Pattern Selector ----------------
def render_pattern_selector():
    patterns = [
        "Bullish Engulfing",
        "Bearish Engulfing",
        "Doji",
        "Hammer",
        "Inverted Hammer",
        "Morning Star",
        "Evening Star"
    ]
    return st.selectbox("📊 Select Candlestick Pattern", patterns)


# ---------------- Highlights Box ----------------
def render_highlights(matched_stocks, selected_pattern):
    st.markdown("### 🟢 Highlights")
    if matched_stocks:
        st.success(f"🕒 As of {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — Pattern: **{selected_pattern}**")
        st.markdown(f"**{len(matched_stocks)} stocks** formed this pattern today:")
        st.write(", ".join(matched_stocks))
    else:
        st.info("No matching stocks found yet.")
