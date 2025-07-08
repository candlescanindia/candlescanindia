import streamlit as st
from ui.layout import (
    render_header,
    render_top_controls,
    render_highlights
)

# Temporary mock scanning logic
def scan_stocks(pattern, duration):
    # Replace this logic with your actual pattern-matching scan engine
    if pattern:
        return ["RELIANCE", "INFY", "TCS"]
    return []

def main():
    st.set_page_config(page_title="CandleScan India", layout="wide")
    
    render_header()

    duration, pattern_type, selected_pattern, show_filters, scan_clicked = render_top_controls()

    if scan_clicked and selected_pattern:
        matched_stocks = scan_stocks(selected_pattern, duration)
        render_highlights(matched_stocks, selected_pattern)

if __name__ == "__main__":
    main()
