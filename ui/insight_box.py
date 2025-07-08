# ui/insight_box.py

import streamlit as st

def render_insight_box(insight_data: list):
    with st.container():
        st.markdown("""
            <div style='border: 1px solid #ccc; border-radius: 10px; padding: 15px; background-color: #f9f9f9;'>
                <h4 style='margin-top: 0;'>📊 Recent Pattern Highlights</h4>
        """, unsafe_allow_html=True)

        if not insight_data:
            st.markdown("<i>No recent insights available. Stay tuned for live updates!</i>", unsafe_allow_html=True)
        else:
            for insight in insight_data:
                st.markdown(f"🔹 {insight}")

        st.markdown("</div>", unsafe_allow_html=True)
