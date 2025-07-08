import streamlit as st

# Dummy precomputed insights — replace with real-time or scheduled data later
precomputed_insights = [
    {
        "pattern": "Doji",
        "count": 2,
        "timestamp": "08-07-2025 1:00 PM",
        "duration": "15m"
    },
    {
        "pattern": "Hammer",
        "count": 3,
        "timestamp": "08-07-2025",
        "duration": "EOD"
    },
    {
        "pattern": "Bullish Engulfing",
        "count": 1,
        "timestamp": "08-07-2025 10:15 AM",
        "duration": "15m"
    },
]


def render_insights():
    if not precomputed_insights:
        return

    with st.container():
        st.markdown("""
            <div style="border: 1px solid #ccc; padding: 1rem; border-radius: 10px; background-color: #f9f9f9;">
            <h4 style="color:#1f4e79">📊 Market-wide Candlestick Insights</h4>
        """, unsafe_allow_html=True)

        for item in precomputed_insights:
            st.markdown(
                f"🔹 **{item['count']} stock{'s' if item['count'] > 1 else ''}** formed **{item['pattern']}** "
                f"on **{item['timestamp']}** in **{item['duration']}** chart."
            )

        st.markdown("</div>", unsafe_allow_html=True)
