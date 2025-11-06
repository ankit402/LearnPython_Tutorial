from binascii import hexlify
import tkinter as tk
from tkinter import messagebox

# start main or init tkinter
root = tk.Tk()
root.title("Validate App")
root.geometry("500x400")

# --- Labels and Textboxes (created once) ---
modulus_label = tk.Label(root, text="Enter Modulus")
modulus_label.pack(pady=5)
modulus_entry = tk.Entry(root, width=60)
modulus_entry.pack(pady=5)

cipher_label = tk.Label(root, text="Enter Cipher Text")
cipher_label.pack(pady=5)
cipher_entry = tk.Entry(root, width=60)
cipher_entry.pack(pady=5)

# --- Output area ---
output = tk.Text(root, height=6, width=60)
output.pack(pady=10)

# --- Function Definitions ---
def ConvertHextoInt(a, b):
    try:
        n = int(a, 16)
        e = 3  # exponent
        c = int(b, 16)
        # Perform RSA modular exponentiation (no padding)
        m = pow(c, e, n)
        # Convert decrypted integer to bytes
        key_len = (n.bit_length() + 7) // 8
        plaintext = m.to_bytes(key_len, byteorder="big")
        result = hexlify(plaintext).decode().upper()
        output.delete("1.0", tk.END)
        output.insert(tk.END, "Decrypted (hex):\n" + result)
    except ValueError as e:
        output.delete("1.0", tk.END)
        output.insert(tk.END, f"Exception in ConvertHextoInt: {e}")
    except Exception as e:
        output.delete("1.0", tk.END)
        output.insert(tk.END, f"Unexpected error: {e}")

def show_message():
    a = modulus_entry.get().strip()
    b = cipher_entry.get().strip()
    if not a or not b:
        messagebox.showwarning("Input Missing", "Please enter both Modulus and Cipher Text.")
        return
    ConvertHextoInt(a, b)

# --- Button ---
button = tk.Button(root, text="Decrypt", command=show_message)
button.pack(pady=10)

# --- Start GUI ---
root.mainloop()

#2D22902CDB0FA4196C453448B55B7886A57D6CD9CB50E63AC642EE57BA1EC4CC03C3705C6E7CCD9403B2F88710E7ACE61CF49FEDAF9CF38DAB3906AAAA6C4ACFD0B1193C0C757668D40C53F16FD662E8B5ECA465CCBF707A6DCDB44BBCA2BCB353F4B07BE3761F730A66F5F905CAD1221F406DB1DA3AC8C22F817C7543AE53017D41345038546CEC9071F36959DF399303F6CFD5B6E3C12DC58EA79E87FFD54A6AC6BAC97C8BA12A2311B89FEAD2DB2946DA898938D0059B10A7BCE23F6D06EA4132466CD9121C515741FFAF142E2C608E6C24C2CF55225D23C2FBC1BBD0498105D42B66E980E9AECCA1B5E7AE851BA89FBD2E29218EBAF5

#key C7FB954E2BD10EB17D9E31C25E30F18C97CF0810C9F9B9FF67E2190CE211AFA2D292493D4F8ACC8B3F48E69B6190583D8C93C463DED116042EDD0DA79A37B0D56DB865B6F56F806A13BF26AFB38F457E1B38D803FADB631BB2CE738624DA35306DB306828A908B63D66C7AEC988DCE0CB47821C3F3298A4ABA243F9E5C76551D0E8685117942DDBF0547D342D62EC81E912F1889AF007AD6B2ACEC94145AD43C68B03C2DD8888583E5118250A5E60A0682122B9B9F20C581C830B155D20D3360ABBAD122A019D218749340B280BD0D9ED44A570E65FDABA08454FDF0DB770C4055957390D60939758580E62AFAECEEFCE85CC09009DA94A3