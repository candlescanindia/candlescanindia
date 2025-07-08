# app.py

import streamlit as st
from ui.layout import render_header, render_top_controls
from ui.scan_card import render_scan_results
from ui.insight_box import render_insight_box
from scans.candlestick import run_candlestick_scan


def main():
    st.set_page_config(page_title="CandleScan India", layout="wide")

    render_header()

    # Top control section
    duration, pattern_type, pattern, _, scan_clicked = render_top_controls()

    # Run scan logic on button click
    matched_results = []
    if scan_clicked and pattern:
        matched_results = run_candlestick_scan(duration=duration, pattern=pattern)

    # Always-visible scan results section
    st.markdown("## 🧾 Scan Results")
    render_scan_results(matched_results, scan_clicked)

    # Always-visible insight box with no logic (placeholder)
    st.markdown("## 💡 Live Insights")
    render_insight_box([])  # empty list for now


if __name__ == "__main__":
    main()
