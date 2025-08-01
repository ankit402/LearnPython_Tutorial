import tkinter as tk
from tkinter import messagebox


def show_message():
    name = entry.get()
    surname = entry2.get()
    messagebox.showinfo("Message", f"{name} {surname}")

root = tk.Tk()
root.title("first App")
root.geometry("300x300")

#Add label
label = tk.Label(root, text="Enter Name")
label.pack(pady=5)

#Add textbox
entry = tk.Entry(root)
entry.pack(pady=5)

#Add label
label2 = tk.Label(root, text="Enter LastName")
label2.pack(pady=5)

#Add textbox
entry2 = tk.Entry(root)
entry2.pack(pady=5)

#button Add
button = tk.Button(root, text="Show Message", command=show_message).pack(pady=10)


root.mainloop()



