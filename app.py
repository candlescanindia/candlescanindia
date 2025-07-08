# app.py

import streamlit as st
from ui.layout import render_header, render_top_controls
from ui.scan_card import render_scan_results
from scans.candlestick import run_candlestick_scan

def main():
    st.set_page_config(page_title="CandleScan India", layout="wide")

    render_header()
    duration, pattern_type, pattern, show_filters, scan_clicked = render_top_controls()

    matched_results = []
    if scan_clicked:
        matched_results = run_candlestick_scan(duration, pattern)

    render_scan_results(matched_results)

if __name__ == "__main__":
    main()
