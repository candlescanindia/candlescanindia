import streamlit as st
from ui.layout import render_header, render_top_controls
from scans.candlestick import run_candlestick_scan
from ui.scan_card import render_scan_results
from ui.insight_box import show_insight_box

def main():
    st.set_page_config(page_title="CandleScan India", layout="wide")

    # Header section
    render_header()

    # Top controls
    duration, pattern_type, pattern_selected, show_filters, scan_clicked = render_top_controls()

    # General rotating insights
    show_insight_box()

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

    # Show scan results (even if empty, logic is inside render_scan_results)
    render_scan_results(results, scan_clicked)

if __name__ == "__main__":
    main()
