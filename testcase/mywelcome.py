import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

class mainapp(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        root.title("Event Trigger")
        # Create Button
        button = tk.Button(root, text="Click Me", command=pressbutton)
        button.pack(pady=20)  # Add padding for better layout

def pressbutton():
    #Message Box
    messagebox.showinfo("Message", "Hello World")

if __name__ == "__main__":
    root = tk.Tk()
    app = mainapp(root)
    root.mainloop()
