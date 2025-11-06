import time as time

import streamlit as st

st.title("Hello")

name= st.text_input("Enter your name")
st.write(f"your name is {name}")
age = st.slider("Age", 0, 100, 25)
st.write(f"Your age is {age}")
options = st.selectbox("choose the option", ["Python", "Java", "C#" , "C++"])
st.write(f"Your option is {options}")

#choose file image to upload
browse = st.file_uploader("file")
if browse:
    st.write(f"Your file name is {browse.name}")

# Using object notation

