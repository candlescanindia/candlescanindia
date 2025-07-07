import streamlit as st
from datetime import datetime

# ---------------- Header Section ----------------
def header_section():
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


# ---------------- Filter Section ----------------
def filter_section():
    with st.expander("➕ Add Optional Filters"):
        st.info("Filter options coming soon (e.g. price, volume, sector, etc.)")
    return True  # Placeholder return


# ---------------- Pattern Selector ----------------
def pattern_selector():
    # You can expand this list later or load dynamically
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


# ---------------- Highlights Section ----------------
def highlights_box(matched_stocks, selected_pattern):
    st.markdown("### 🟢 Highlights")
    st.success(f"🕒 As of {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} — Pattern: **{selected_pattern}**")
    st.markdown(f"**{len(matched_stocks)} stocks** formed this pattern today:")
    st.write(", ".join(matched_stocks))
    st.markdown("---")

