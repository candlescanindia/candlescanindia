# ui/insight_box.py

import streamlit as st
from collections import defaultdict
from datetime import datetime

def render_insights(matched_results):
    if not matched_results:
        return

    # Group by pattern and duration
    grouped = defaultdict(list)
    for item in matched_results:
        key = (item['pattern'], item['duration'], item['timestamp'])
        grouped[key].append(item)

    with st.container():
        st.markdown("""
            <div style="border: 1px solid #ccc; padding: 1rem; border-radius: 10px; background-color: #f9f9f9;">
            <h4 style="color:#1f4e79">📊 Insights Summary</h4>
        """, unsafe_allow_html=True)

        for (pattern, duration, timestamp), stocks in grouped.items():
            readable_time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M").strftime("%d-%m-%Y %I:%M %p")
            if "1d" in duration.lower() or "1wk" in duration.lower():
                readable_time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M").strftime("%d-%m-%Y") + " EOD"

            stock_count = len(stocks)
            pattern_display = f"{pattern} pattern"
            msg = f"🔹 **{stock_count} stock{'s' if stock_count > 1 else ''}** formed **{pattern_display}** on **{readable_time}** in **{duration}** chart."
            st.markdown(msg)

        st.markdown("</div>", unsafe_allow_html=True)
