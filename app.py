import streamlit as st
from ui.layout import render_header, render_top_controls
from ui.scan_card import render_scan_results
from ui.insight_box import render_insights
from scans.candlestick import run_candlestick_scan  # Your scanning logic

def main():
    st.set_page_config(page_title="CandleScan India", layout="wide")

    render_header()
    duration, pattern_type, selected_pattern, _, scan_clicked = render_top_controls()

    matched_results = []
    if scan_clicked and selected_pattern:
        matched_results = run_candlestick_scan(duration, selected_pattern)

    render_scan_results(matched_results, scan_clicked)
    render_insights()

if __name__ == "__main__":
    main()
