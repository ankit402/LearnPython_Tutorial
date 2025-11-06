from library import *

def GetDataCommand(connection ,sw2):
    try:
        apdu = apdu = [0x00, 0xC0, 0x00, 0x00, sw2]
        response, sw1, sw2 = connection.transmit(apdu)
        #st.write(f"Response Data: {toHexString(response)}")
        st.success(f"Status Words: SW1={hex(sw1)} SW2={hex(sw2)}")
        if sw1 == 0x90 and sw2 == 0x00:
            st.success(f"Response AID: {toHexString(response).replace(" ", "")}")
        elif sw1 == 0x6d and sw2 == 0x0:
            st.warning("AID not found ❌ (falling back to PSE)")
    except Exception as e:
        st.error(f"Failed to transmit GetDataCommand: {e}")