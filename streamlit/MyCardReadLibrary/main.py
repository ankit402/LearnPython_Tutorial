import pandas as pd
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from library import *
import streamlit as st, requests
import re
from smartcard.System import readers
# Streamlit UI
def Fetchkeys():
    #API Call for Get Response
    myrequest = requests.get("http://172.22.0.144:83/KMUService.asmx/findAllKeys")
    allkeysplit = myrequest.text.split("~")
    saveintuple = ()
    myfilter = "</string>"
    counter = 0
    for i in allkeysplit:
            if counter != 0:
                if i in myfilter:
                    pass
                else:
                    saveintuple = saveintuple + (i,)
            else:
                 saveintuple = tuple(s.replace("^CKK_DES2", "") for s in saveintuple)
                 counter += 1
    selectbox_key = st.selectbox('Key', saveintuple)
    ClearComponent(selectbox_key)

def ClearComponent(keyname):
    mycomponent=''
    keynamedata = keyname.split("^CKK_DES2")
    hex_pattern = re.compile(r'^[0-9A-F]+$', re.IGNORECASE)
    for s in keynamedata:
        params = {"KeyName": s}
        mycomponent = requests.get("http://172.22.0.144:83/KMUService.asmx/GetClearComponent", params=params)
        # Extract the value inside <string>...</string>
        # Extract string content from <string>...</string>
        if "<string" in mycomponent.text:
            first_string = mycomponent.text.split("<string", 1)[1]
            value = first_string.split(">", 1)[1].split("<", 1)[0].strip()
            # Check if it's hex and display once
            if hex_pattern.fullmatch(value):
                st.success(value)  # Will print only once
            else:
               pass

st.title("🏠 Home Page")
st.subheader("Welcome to the Smart Card Reader App")
page = st.sidebar.radio(
    "Go to",
    ["🏠 Home", "💳 MasterCard", "💳 Visa", "Technical VPA"]  # emojis as icons
)
st.write(page)

def MyFileRead():
    uploaded_file = st.file_uploader("Upload an HTML file", type=['html', 'htm'])
    try:
        if uploaded_file is not None:
            html_content = uploaded_file.read().decode("utf-8")
            # Parse HTML
            soup = BeautifulSoup(html_content, "html.parser")
            # Extract all tables from HTML as list of DataFrames
            tables = pd.read_html(html_content)

            if tables:
                st.write(f"Found {len(tables)} table(s) in the HTML file:")
                for i, table in enumerate(tables):
                    #table = table.applymap(lambda x: x.replace(" ", "") if isinstance(x, str) else x)
                    st.dataframe(table)

            else:
                st.write("No tables found in the HTML file.")
    except Exception as e:
        st.write(e)
if "Technical VPA" in page:
     MyFileRead()
     #treeview()

if "MasterCard" and "Visa" in page:
    reader = Get_ListofReader()
    select_aid = GiveOptionAID()
    Fetchkeys()
    # Keep track of button state
    if "btn_success" not in st.session_state:
        st.session_state.btn_success = False
    if st.button("Connect to Reader"):
        ConnectionReader(reader, select_aid)
        st.session_state.btn_success = True
# Change button style if success
        if st.session_state.btn_success:
            st.markdown(
                """
                <style>
                div.stButton > button:first-child {
                    background-color: #4CAF50; /* Green */
                    color: white;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
