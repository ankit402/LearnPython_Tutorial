from library import *
import streamlit as st

def ReadAID(connection,AID):
    # APDU: CLA INS P1 P2 Lc Data
    st.write("****************Start Reading Application Applet****************")
    aid = ''
    if AID in "MASTERCARD":
        aid = [0xA0, 0x00, 0x00, 0x00, 0x04, 0x10, 0x10]
    elif AID in "VISA":
        aid = [0xA0, 0x00, 0x00, 0x00, 0x03, 0x10, 0x10]
    apdu = [0x00, 0xA4, 0x04, 0x00, len(aid)] + aid + [0x00]  # Le
    # st.write(f"Sending APDU: {toHexString(apdu)}")
    st.markdown(f"Sending Command {toHexString(apdu)}")
    response, sw1, sw2 = connection.transmit(apdu)
    GetDataCommand(connection, sw2)
    st.write("****************End Reading AID****************")