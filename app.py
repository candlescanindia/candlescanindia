# app.py

import streamlit as st
from ui.layout import render_header, render_top_controls
from ui.insight_box import render_insight_box
from ui.scan_card import render_scan_results
from scans.candlestick import run_candlestick_scan

def main():
    st.set_page_config(page_title="CandleScan India", layout="wide")
    render_header()

    # Top Controls
    duration, pattern_type, pattern_selected, show_filters, scan_clicked = render_top_controls()

    # Additional Filters
    filters = {}
    if show_filters:
        with st.expander("🔧 Advanced Filters", expanded=True):
            col1, col2, col3 = st.columns(3)

            with col1:
                filters["min_volume"] = st.number_input("Minimum Volume", min_value=0, value=100000)

            with col2:
                filters["min_price"] = st.number_input("Min Price", min_value=0.0, value=10.0)
                filters["max_price"] = st.number_input("Max Price", min_value=0.0, value=1000.0)

            with col3:
                filters["min_rsi"] = st.slider("Min RSI", 0, 100, 30)
                filters["max_rsi"] = st.slider("Max RSI", 0, 100, 70)

    # Run Scan
    results = []
    if scan_clicked:
        results = run_candlestick_scan(
            duration=duration,
            pattern=pattern_selected,
            min_volume=filters.get("min_volume", 0),
            min_price=filters.get("min_price", None),
            max_price=filters.get("max_price", None),
            min_rsi=filters.get("min_rsi", None),
            max_rsi=filters.get("max_rsi", None)
        )

    # Results
    render_scan_results(results, scan_clicked)

    # Insights
    render_insight_box([
        "Doji patterns are forming on mid-cap pharma stocks.",
        "Volume breakout seen in bullish engulfing setups.",
        "Watch RSI > 60 with bullish hammer in small caps."
    ])

if __name__ == "__main__":
    main()
