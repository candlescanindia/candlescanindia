# app.py

import streamlit as st
from ui.layout import render_header, render_top_controls
from ui.scan_card import render_scan_results

# Simulated scan logic for demonstration (replace with real logic)
def perform_scan(duration, pattern):
    # Placeholder: Return dummy data
    if pattern:
        return [
            {
                "name": "Reliance Industries",
                "symbol": "RELIANCE",
                "price": 2850.50,
                "exchange": "NSE",
                "timestamp": "2025-07-08 15:30",
                "duration": duration
            },
            {
                "name": "Tata Consultancy Services",
                "symbol": "TCS",
                "price": 3755.75,
                "exchange": "BSE",
                "timestamp": "2025-07-08 15:30",
                "duration": duration
            }
        ]
    return []

def main():
    st.set_page_config(page_title="CandleScan India", layout="wide")
    
    render_header()

    duration, pattern_type, pattern, show_filters, scan_clicked = render_top_controls()

    matched_results = []
    if scan_clicked and pattern:
        matched_results = perform_scan(duration, pattern)

    render_scan_results(matched_results)

if __name__ == "__main__":
    main()
