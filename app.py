# app.py

import streamlit as st
from ui.layout import render_header, render_top_controls, render_highlights
from ui.scan_card import render_scan_results

# Simulated scan function — replace with real logic later
def scan_stocks(duration, pattern):
    """
    Returns dummy scan results for the selected pattern.
    Replace this with actual stock scanning logic.
    """
    if not pattern:
        return []

    return [
        {
            "stock_name": "TCS",
            "symbol": "TCS",
            "ltp": 3892.55,
            "exchange": "NSE",
            "pattern_time": "2025-07-08 14:15",
            "duration": duration
        },
        {
            "stock_name": "Infosys",
            "symbol": "INFY",
            "ltp": 1450.10,
            "exchange": "BSE",
            "pattern_time": "2025-07-08 14:15",
            "duration": duration
        }
    ]

# ---------------- Main App ----------------
def main():
    st.set_page_config(page_title="CandleScan India", layout="wide")

    render_header()

    # Get user input
    duration, pattern_type, pattern, show_filters, scan_clicked = render_top_controls()

    matched_results = []
    if scan_clicked and pattern:
        matched_results = scan_stocks(duration, pattern)

    # Highlights
    if scan_clicked:
        render_highlights([stock["symbol"] for stock in matched_results], pattern)

    # Scan result cards
    if scan_clicked:
        render_scan_results(matched_results)


if __name__ == "__main__":
    main()
