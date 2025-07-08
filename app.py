import streamlit as st
from ui.layout import render_header, render_top_controls
from scans.candlestick import run_candlestick_scan
from ui.scan_card import render_scan_results
from ui.insight_box import render_insight_box

def main():
    st.set_page_config(page_title="CandleScan India", layout="wide")

    # Header section
    render_header()

    # Top controls
    duration, pattern_type, pattern_selected, show_filters, scan_clicked = render_top_controls()

    # General insights (can be static or updated periodically)
    static_insights = [
        "Hammer appeared 15 times today in NIFTY 500 stocks.",
        "Bearish Engulfing detected in large-cap pharma sector.",
        "Doji patterns increased in last 3 sessions."
    ]
    render_insight_box(static_insights)

    # Run scan only when button is clicked
    results = []
    if scan_clicked and pattern_selected:
        with st.spinner("🔍 Scanning the Indian market..."):
            results = run_candlestick_scan(
                duration=duration,
                pattern_type=pattern_type,
                pattern=pattern_selected,
                filters_enabled=show_filters
            )

    # Show results
    render_scan_results(results, scan_clicked)

if __name__ == "__main__":
    main()
