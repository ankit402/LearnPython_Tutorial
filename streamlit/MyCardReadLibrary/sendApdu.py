from library import *
import streamlit as st
def SendApduCommand(connection,AID):
    try:
        ReadAID(connection, AID)
        ReadPSE(connection)
        ReadPPSE(connection)
        #st.toast("Data transmitted Failed!", icon="✅")
    except Exception as e:
        st.error(f"Failed to send APDU: {e}")
        #st.toast("Data transmitted Failed!", icon="✅")