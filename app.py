import streamlit as st
from ui.layout import render_header, render_top_controls
from scans.candlestick import run_candlestick_scan
from ui.scan_card import display_scan_results
from ui.insight_box import show_insight_box

def main():
    st.set_page_config(page_title="CandleScan India", layout="wide")

    # Header section
    render_header()

    # Top controls (returns all user selections)
    duration, pattern_type, pattern_selected, show_filters, scan_clicked = render_top_controls()

    # Insight box (always visible)
    show_insight_box()

    # Run scan only when button clicked and a pattern is selected
    if scan_clicked and pattern_selected:
        with st.spinner("🔍 Scanning Indian market..."):
            results = run_candlestick_scan(
                duration=duration,
                pattern_type=pattern_type,
                pattern=pattern_selected,
                filters_enabled=show_filters
            )
        display_scan_results(results, pattern_selected)
    elif scan_clicked:
        st.warning("Please select a candlestick pattern before scanning.")

if __name__ == "__main__":
    main()
