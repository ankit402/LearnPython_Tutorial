from library import *

def DefineAIDTemplate(AID):
    if "A0 00 00 00 04 10 10 00" in AID:
        AID += " MASTERCARD"
    elif  "A0 00 00 00 03 10 10 00" in AID:
        AID += "VISA"
    return AID

def GiveOptionAID():
    listaid = ["MASTERCARD","VISA"]
    selectedone=st.selectbox("Choose Application ", listaid)
    data=DefineAIDTemplate(selectedone)
    return data