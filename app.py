# app.py

import streamlit as st
from ui.layout import render_header, render_top_controls
from ui.scan_card import render_scan_results

# Placeholder function to simulate pattern scan
def perform_scan(duration, pattern_type, pattern):
    # Mock data
    if not pattern:
        return []

    return [
        {
            "stock_name": "Reliance Industries",
            "symbol": "RELIANCE",
            "ltp": 2748.35,
            "exchange": "NSE",
            "pattern_time": "2025-07-08 14:15",
            "duration": duration
        },
        {
            "stock_name": "Infosys Ltd",
            "symbol": "INFY",
            "ltp": 1502.20,
            "exchange": "BSE",
            "pattern_time": "2025-07-08 14:15",
            "duration": duration
        },
        {
            "stock_name": "Tata Motors",
            "symbol": "TATAMOTORS",
            "ltp": 982.55,
            "exchange": "NSE",
            "pattern_time": "2025-07-08 14:15",
            "duration": duration
        }
    ]

def main():
    st.set_page_config(page_title="CandleScan India", layout="wide")
    render_header()

    duration, pattern_type, pattern, show_filters, scan_clicked = render_top_controls()

    matched_results = []
    if scan_clicked and pattern:
        matched_results = perform_scan(duration, pattern_type, pattern)

    render_scan_results(matched_results)

if __name__ == "__main__":
    main()
