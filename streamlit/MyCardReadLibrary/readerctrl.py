
import time
from library import *
import streamlit as st
def ConnectionReader(reader,selected_aid):
    if reader is None:
        return
    try:
        connection = reader.createConnection()
        progress = st.progress(0)
        connection.connect()
        st.success(f"Connected to card using: {reader}")
        time.sleep(0.2)
        progress.progress(30)  # after connect
        # Show ATR (Answer to Reset)
        atr = connection.getATR()
        st.success(f"ATR:{toHexString(atr)}")
        time.sleep(0.2)
        progress.progress(70)  # after ATR
        SendApduCommand(connection,selected_aid)
        time.sleep(0.2)
        connection.disconnect()
        progress.progress(100)  # after APDU
        st.warning(f"Note Read Communication Closed Press Connect")
    except Exception as e:
        st.error(f"Failed to connect: {e}")

def Get_ListofReader():
    r= readers()
    print("Available readers:", r)
    return st.selectbox("Readers Name", r)







