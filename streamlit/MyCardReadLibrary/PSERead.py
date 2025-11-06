from library import *
def ReadPSE(connection):
    # SELECT PSE: 00 A4 04 00 0E 315041592E5359532E4444463031
    st.write("****************Start Reading PSE****************")
    pse = [0x31, 0x50, 0x41, 0x59, 0x2E, 0x53, 0x59, 0x53,
           0x2E, 0x44, 0x44, 0x46, 0x30, 0x31]
    pSEApdu = [0x00, 0xA4, 0x04, 0x00, len(pse)] + pse + [0x00]
    # Transmit APDU
    response, sw1, sw2 = connection.transmit(pSEApdu)
    st.write(f"Sending APDU PSE: {toHexString(pSEApdu)}")
    GetDataCommand(connection, sw2)
    st.write("****************End Reading PSE****************")