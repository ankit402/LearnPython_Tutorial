import streamlit as st

st.markdown("Page  2 ️❄️")
st.sidebar.markdown("Page 2 ❄️")

hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
st.write(hour_to_filter)