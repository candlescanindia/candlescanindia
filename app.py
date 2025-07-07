# app.py

import streamlit as st
from ui.layout import render_header, render_controls, render_highlights, render_results

# Page config
st.set_page_config(page_title="CandleScan India", layout="wide")

# --- Render UI Sections ---
render_header()

# Controls section with chart duration and filters
selected_duration, selected_filters, selected_pattern, search_query, trigger_scan = render_controls()

# If scan triggered, we will later call scan logic
if trigger_scan:
    st.info("Scan will be performed here in next step...")

# Placeholder for highlights and results section
render_highlights([])
render_results([], selected_pattern=None)
