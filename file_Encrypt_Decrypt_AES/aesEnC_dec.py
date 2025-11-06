# from Crypto.Cipher import AES
# from Crypto.Util.Padding import unpad
#
# def decrypt_aes_ecb(encrypted_file_path, hex_key, output_file_path):
#     key = bytes.fromhex(hex_key)
#     # Ensure key is bytes and valid AES length (16, 24, or 32 bytes)
#     if not isinstance(key, bytes):
#         raise ValueError("Key must be bytes.")
#
#     # Read encrypted data
#     with open(encrypted_file_path, 'rb') as f:
#         ciphertext = f.read()
#
#     # Create AES cipher in ECB mode
#     cipher = AES.new(key, AES.MODE_ECB)
#     # Decrypt and unpad
#     plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
#
#     # Write plaintext to output
#     with open(output_file_path, 'wb') as f:
#         f.write(plaintext)
#
#     print(f"Decryption complete. File saved to: {output_file_path}")
#
#
# hex_key = "0178C86213D7957554BF23DF4EE24B3A"
# encrypted_file = "Inst_Card_Batch_6500531101_sm_25022025_131958.csv"
# decrypted_output = "decrypted_output.csv"
#
# decrypt_aes_ecb(encrypted_file, hex_key, decrypted_output)

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os
import csv
import io

def decrypt_aes_file(encrypted_file_path, hex_key, hex_iv, mode, output_file_path):
    try:
        key = bytes.fromhex(hex_key)
        if len(key) not in [16, 24, 32]:
            raise ValueError("Key must be 16, 24, or 32 bytes long.")

        with open(encrypted_file_path, 'rb') as f:
            ciphertext = f.read()

        if mode == "ECB":
            cipher = AES.new(key, AES.MODE_ECB)
        elif mode == "CBC":
            if not hex_iv:
                raise ValueError("IV is required for CBC mode.")
            iv = bytes.fromhex(hex_iv)
            if len(iv) != 16:
                raise ValueError("IV must be 16 bytes for CBC mode.")
            cipher = AES.new(key, AES.MODE_CBC, iv)
        else:
            raise ValueError("Unsupported mode selected.")

        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

        with open(output_file_path, 'wb') as f:
            f.write(plaintext)

        messagebox.showinfo("Success", f"Decryption complete.\nSaved to: {output_file_path}")

        # Display decrypted data in table
        display_decrypted_data(plaintext.decode('utf-8', errors='replace'))

    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed:\n{str(e)}")

def display_decrypted_data(text_data):
    # Clear previous table if exists
    for widget in table_frame.winfo_children():
        widget.destroy()

    try:
        # Attempt to parse CSV from decrypted text
        csv_reader = csv.reader(io.StringIO(text_data))
        rows = list(csv_reader)

        if not rows:
            raise ValueError("No data to display")

        # Create Treeview widget
        tree = ttk.Treeview(table_frame, show='headings')
        tree.pack(expand=True, fill='both')

        # Setup columns
        columns = [f"Data {i+1}" for i in range(len(rows[0]))]
        tree["columns"] = columns
        for i, col in enumerate(columns):
            tree.heading(col, text=col)
            tree.column(col, anchor='center')

        # Insert rows into the tree
        for row in rows:
            tree.insert("", tk.END, values=row)

    except Exception as e:
        # If CSV parsing fails, just show raw text in a Text widget
        text_widget = tk.Text(table_frame, wrap='word')
        text_widget.insert('1.0', text_data)
        text_widget.pack(expand=True, fill='both')
        messagebox.showwarning("Display Warning", f"Failed to parse as table, displaying raw text.\n{e}")

def select_input_file():
    path = filedialog.askopenfilename(title="Select Encrypted File")
    input_file_var.set(path)

def select_output_file():
    path = filedialog.asksaveasfilename(title="Save Decrypted File As")
    output_file_var.set(path)

def toggle_iv_entry(*args):
    mode = mode_var.get()
    if mode == "CBC":
        iv_label.pack()
        iv_entry.pack()
    else:
        iv_label.pack_forget()
        iv_entry.pack_forget()

def submit():
    input_file = input_file_var.get()
    output_file = output_file_var.get()
    key = key_var.get().strip()
    iv = iv_var.get().strip()
    mode = mode_var.get()

    if not os.path.isfile(input_file):
        messagebox.showerror("Input Error", "Invalid input file.")
        return
    if not key:
        messagebox.showerror("Key Error", "Key cannot be empty.")
        return
    if mode == "CBC" and not iv:
        messagebox.showerror("IV Error", "IV is required for CBC mode.")
        return
    if not output_file:
        messagebox.showerror("Output Error", "Please specify an output file path.")
        return

    decrypt_aes_file(input_file, key, iv, mode, output_file)

# --- GUI Setup ---
root = tk.Tk()
root.title("AES File Decryption (ECB / CBC) with Table Display")
root.geometry("700x600")
root.resizable(True, True)

input_file_var = tk.StringVar()
output_file_var = tk.StringVar()
key_var = tk.StringVar(value="0178C86213D7957554BF23DF4EE24B3A")
iv_var = tk.StringVar()
mode_var = tk.StringVar(value="ECB")

tk.Label(root, text="Encrypted File:").pack(pady=5)
tk.Entry(root, textvariable=input_file_var, width=80).pack()
tk.Button(root, text="Browse", command=select_input_file).pack(pady=5)

tk.Label(root, text="Output File:").pack(pady=5)
tk.Entry(root, textvariable=output_file_var, width=80).pack()
tk.Button(root, text="Save As", command=select_output_file).pack(pady=5)

tk.Label(root, text="AES Key (Hex):").pack(pady=5)
tk.Entry(root, textvariable=key_var, width=80).pack()

tk.Label(root, text="Mode:").pack(pady=5)
tk.OptionMenu(root, mode_var, "ECB", "CBC", command=toggle_iv_entry).pack()

iv_label = tk.Label(root, text="IV (Hex, for CBC mode):")
iv_entry = tk.Entry(root, textvariable=iv_var, width=80)
toggle_iv_entry()

tk.Button(root, text="Submit", command=submit, bg="blue", fg="white", height=2, width=20).pack(pady=10)

tk.Label(root, text="Decrypted Data Preview:").pack(pady=5)

table_frame = tk.Frame(root, relief=tk.SUNKEN, borderwidth=2)
table_frame.pack(expand=True, fill='both', padx=10, pady=10)

root.mainloop()
