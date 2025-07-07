import streamlit as st
from ui.layout import (
    render_header,
    render_pattern_selector,
    render_search_bar
)

# -------------------- Page Setup --------------------
st.set_page_config(page_title="CandleScan India", layout="wide")

# -------------------- UI Sections --------------------
render_header()

# Layout for search and pattern selector side by side
col1, col2 = st.columns([2, 1])
with col1:
    search_query = render_search_bar()

with col2:
    selected_pattern = render_pattern_selector()

# Optional: Display what user selected (for debugging/testing)
st.markdown("---")
st.write(f"🔍 Search Query: `{search_query}`")
st.write(f"📊 Selected Pattern: `{selected_pattern}`")
