import streamlit as st

with st.sidebar:
    st.title("Navigation Menu")
    st.page_link("my_page.py", label="Go to My Page")