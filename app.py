import streamlit as st
from ui.layout import render_header, render_top_controls
from ui.scan_card import render_scan_results
from scans.candlestick import run_candlestick_scan  # Backend scanning logic

def main():
    st.set_page_config(page_title="CandleScan India", layout="wide")

    # Header
    render_header()

    # Controls
    duration, pattern_type, pattern_selected, show_filters, scan_clicked = render_top_controls()

    # Run scan if scan button clicked
    matched_results = []
    if scan_clicked and pattern_selected:
        matched_results = run_candlestick_scan(duration=duration, pattern=pattern_selected)

    # Scan result section (always visible)
    render_scan_results(matched_results, scan_clicked)


if __name__ == "__main__":
    main()
