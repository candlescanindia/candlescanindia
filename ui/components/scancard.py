import streamlit as st
from datetime import datetime


def result_display(matched_stocks, pattern_name):
    st.markdown("---")
    st.subheader(f"📊 Scan Results for {pattern_name}")

    if not matched_stocks:
        st.info("No stocks matched the selected pattern.")
        return

    now = datetime.now().strftime("%d-%b-%Y %I:%M %p")

    for stock in matched_stocks:
        with st.container():
            st.markdown(f"**{stock}**")
            st.caption(f"Pattern: `{pattern_name}` | Identified on {now}")
            st.markdown("---")


def highlights_box(matched_stocks, pattern_name):
    if matched_stocks:
        with st.expander(f"✨ {len(matched_stocks)} stock(s) formed {pattern_name} today. Click to view list.", expanded=False):
            for stock in matched_stocks:
                st.write(f"- {stock}")
    else:
        st.info("No stocks highlighted today.")

