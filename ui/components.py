
import streamlit as st

def header_section():
    st.markdown("""
    <div style='display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem;'>
        <div>
            <h1 style='margin-bottom: 0;'>📊 CandleScan India</h1>
            <p style='color: gray; margin-top: 0;'>Smart scanner for Indian stocks based on candlestick patterns</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

def filter_section(duration, filters_enabled):
    col1, col2 = st.columns([3, 1])
    with col1:
        duration_option = st.selectbox("Select Chart Duration", ["15 min", "30 min", "1 day", "1 week"], index=2)
    with col2:
        if st.button("🔍 Filters"):
            filters_enabled = not filters_enabled
    return duration_option, filters_enabled

def pattern_selector(patterns):
    selected_pattern = st.selectbox("Choose Candlestick Pattern", patterns, index=0)
    return selected_pattern

def result_display(pattern_name, results, scan_time):
    st.markdown(f"### 📅 Scan Results ({scan_time})")
    if results:
        for stock in results:
            st.markdown(f"- **{stock}** formed **{pattern_name}** pattern")
    else:
        st.info("No matching patterns found for the selected criteria.")

def highlights_box(pattern_name, results):
    if results:
        count = len(results)
        summary_text = f"{count} stocks formed **{pattern_name}** pattern today"
        if st.button(summary_text):
            st.markdown("### 🧾 Details")
            for stock in results:
                st.markdown(f"- {stock}")
