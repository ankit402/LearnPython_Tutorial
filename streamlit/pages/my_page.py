import streamlit as st
import base64

file = st.file_uploader("Upload PDF file", type=["pdf"])

if file is not None:
    # Read file bytes
    pdf_bytes = file.read()

    # Encode to base64 string
    b64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')

    # Embed PDF in HTML iframe
    pdf_display = (f'<iframe src="data:application/pdf;base64,{b64_pdf}" '
                   f'width="700" height="400" type="application/pdf">'
                   f'</iframe>')

    st.markdown(pdf_display, unsafe_allow_html=True)
