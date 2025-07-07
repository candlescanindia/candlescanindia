import streamlit as st
from datetime import datetime
from st_pages import add_indented_title

def header_section():
    st.markdown(
        """
        <div style='text-align: center; padding: 10px 0;'>
            <h1 style='margin-bottom: 0;'>📊 CandleScan India</h1>
            <p style='color: gray; font-size: 18px;'>Smart scanner for Indian stocks based on candlestick patterns</p>
        </div>
        """,
        unsafe_allow_html=True
    )

def filter_section():
    with st.expander("⚙️ Add Filters"):
        market_cap = st.selectbox("Market Cap", ["All", "Large Cap", "Mid Cap", "Small Cap"], index=0)
        sector = st.selectbox("Sector", ["All", "IT", "Finance", "Pharma", "Auto", "Energy"], index=0)
        return {
            "market_cap": market_cap,
            "sector": sector
        }

def pattern_selector():
    patterns = [
        "Hammer", "Inverted Hammer", "Doji", "Bullish Engulfing",
        "Bearish Engulfing", "Morning Star", "Evening Star",
        "Shooting Star", "Hanging Man", "Spinning Top", "Marubozu"
    ]
    selected = st.selectbox(
        "Select Candlestick Pattern",
        options=patterns,
        index=0,
        help="Choose the pattern you want to scan for"
    )
    return selected

def result_display(matched_stocks, selected_pattern):
    if not matched_stocks:
        st.warning(f"No stocks found with pattern: {selected_pattern}")
        return

    now = datetime.now().strftime("%d %b %Y %I:%M %p")
    st.markdown(f"### 🟢 {len(matched_stocks)} stocks formed **{selected_pattern}** pattern as of {now}")

    for stock in matched_stocks:
        st.markdown(f"- `{stock}`")

def highlights_box(matched_stocks, selected_pattern):
    if matched_stocks:
        with st.container():
            st.markdown("---")
            st.markdown(
                f"""
                <div style='padding: 10px; border: 1px solid #ccc; border-radius: 10px; background-color: #f8f9fa;'>
                    <h4>📌 Highlights</h4>
                    <p><strong>{len(matched_stocks)} stocks</strong> formed <strong>{selected_pattern}</strong> pattern today.</p>
                    <details>
                        <summary>Click to view stocks</summary>
                        <ul>
                            {''.join(f'<li>{s}</li>' for s in matched_stocks)}
                        </ul>
                    </details>
                </div>
                """,
                unsafe_allow_html=True
            )
