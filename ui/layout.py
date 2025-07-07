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


# ---------------- Filters ----------------
def render_filters():
    with st.expander("➕ Add Optional Filters"):
        st.info("Filter options coming soon (e.g. market cap, price, volume, sector, etc.)")
    return True  # Placeholder return


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


# ---------------- Search Bar ----------------
def render_search_bar():
    return st.text_input(
        "🔍 Search stock symbol",
        placeholder="Type stock symbol (e.g. RELIANCE)",
        label_visibility="collapsed"
    )


# ---------------- Results Display ----------------
def render_results(matched_stocks, selected_pattern):
    st.markdown("### 🧾 Matched Stocks")
    if matched_stocks:
        for stock in matched_stocks:
            st.success(f"✅ {stock} formed **{selected_pattern}** pattern.")
    else:
        st.warning("No matching stocks found.")


# ---------------- Highlights Section ----------------
def render_highlights(matched_stocks, selected_pattern):
    st.markdown("### 🟢 Highlights")
    if matched_stocks:
        st.success(f"🕒 As of {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — Pattern: **{selected_pattern}**")
        st.markdown(f"**{len(matched_stocks)} stocks** formed this pattern today:")
        st.write(", ".join(matched_stocks))
    else:
        st.info("
