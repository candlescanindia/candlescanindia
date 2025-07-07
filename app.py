import streamlit as st
from ui.layout import (
    render_header,
    render_top_controls,
    render_filters_panel,
    render_pattern_selector,
    render_highlights
)

# ------------------ Page Config ------------------
st.set_page_config(page_title="CandleScan India", layout="wide")

# ------------------ Header ------------------
render_header()

# ------------------ Top Controls ------------------
duration, show_filters = render_top_controls()
if show_filters:
    render_filters_panel()

# ------------------ Pattern Selector ------------------
selected_pattern = render_pattern_selector()

# ------------------ Placeholder for Scan Results ------------------
st.markdown("---")
render_highlights([], selected_pattern)
