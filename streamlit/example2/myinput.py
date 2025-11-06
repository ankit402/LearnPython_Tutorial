import streamlit as st
passval=" "
newvalue =st.text_input('Password', type='password', value=passval)
st.write(newvalue)