from library import *

def ReadPPSE(connection):
    st.write("****************Start Reading PPSE****************")
    ppse = [0x32, 0x50, 0x41, 0x59, 0x2E, 0x53, 0x59, 0x53,
           0x2E, 0x44, 0x44, 0x46, 0x30, 0x31]
    ppSEApdu = [0x00, 0xA4, 0x04, 0x00, len(ppse)] + ppse + [0x00]
    response, sw1, sw2 = connection.transmit(ppSEApdu)
    st.write(f"Sending APDU PPSE: {toHexString(ppSEApdu)}")
    st.write(f"Response: {toHexString(response)} SW1={hex(sw1)} SW2={hex(sw2)}")
    if sw1 == 0x90 and sw2 == 0x00:
        st.success("PPSE Selected ✅")
    elif sw1 == 0x6A and sw2 == 0x82:
        st.warning("PPSE not found ❌ (falling back to PSE)")
    st.write("****************End Reading PPSE****************")