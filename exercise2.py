import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pyodbc
import os
from datetime import datetime

# ---------------------- GLOBALS ----------------------
active_conn1 = None
active_conn2 = None

# ---------------------- DB CONNECTION ----------------------
def connect_db(server, database, username, password):
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};DATABASE={database};UID={username};PWD={password}"
    )
    return pyodbc.connect(conn_str)

def get_all_databases(server, username, password):
    try:
        conn = connect_db(server, "master", username, password)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sys.databases WHERE database_id > 4")
        dbs = [row[0] for row in cursor.fetchall()]
        conn.close()
        return dbs
    except Exception as e:
        messagebox.showerror("Connection Error", str(e))
        return []

# ---------------------- CONNECTION FUNCTIONS ----------------------
def connect_db1():
    global active_conn1
    server = entry_server1.get().strip()
    username = entry_user1.get().strip()
    password = entry_pass1.get().strip()
    database = combo_db1.get().strip()
    if not all([server, username, password, database]):
        messagebox.showwarning("Missing Info", "Please fill all connection details for DB1.")
        return
    try:
        active_conn1 = connect_db(server, database, username, password)
        messagebox.showinfo("Connected", f"Connected to DB1: {database}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def connect_db2():
    global active_conn2
    server = entry_server2.get().strip()
    username = entry_user2.get().strip()
    password = entry_pass2.get().strip()
    database = combo_db2.get().strip()
    if not all([server, username, password, database]):
        messagebox.showwarning("Missing Info", "Please fill all connection details for DB2.")
        return
    try:
        active_conn2 = connect_db(server, database, username, password)
        messagebox.showinfo("Connected", f"Connected to DB2: {database}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---------------------- COMPARE LOGIC ----------------------
def compare_databases():
    if not active_conn1 or not active_conn2:
        messagebox.showwarning("No Connection", "Connect both databases first.")
        return

    cur1 = active_conn1.cursor()
    cur2 = active_conn2.cursor()

    # Fetch stored procedures
    cur1.execute("SELECT name FROM sys.objects WHERE type='P'")
    sp1 = set(r[0] for r in cur1.fetchall())
    cur2.execute("SELECT name FROM sys.objects WHERE type='P'")
    sp2 = set(r[0] for r in cur2.fetchall())

    # Fetch tables
    cur1.execute("SELECT name FROM sys.objects WHERE type='U'")
    tbl1 = set(r[0] for r in cur1.fetchall())
    cur2.execute("SELECT name FROM sys.objects WHERE type='U'")
    tbl2 = set(r[0] for r in cur2.fetchall())

    # Differences
    sp_only_db1 = sorted(list(sp1 - sp2))
    sp_only_db2 = sorted(list(sp2 - sp1))
    tbl_only_db1 = sorted(list(tbl1 - tbl2))
    tbl_only_db2 = sorted(list(tbl2 - tbl1))

    show_compare_window(sp_only_db1, sp_only_db2, tbl_only_db1, tbl_only_db2)

# ---------------------- EXPORT MISSING SPs ----------------------
def export_missing_sps(sp_list):
    if not sp_list:
        messagebox.showinfo("Info", "No SPs to export.")
        return

    export_dir = filedialog.askdirectory(title="Select Export Folder")
    if not export_dir:
        return

    cursor = active_conn1.cursor()
    for sp in sp_list:
        cursor.execute("""
            SELECT definition FROM sys.sql_modules 
            WHERE object_id = OBJECT_ID(?)
        """, sp)
        result = cursor.fetchone()
        if result:
            definition = result[0].replace("\r", "").replace("\nGO", "")
            path = os.path.join(export_dir, f"{sp}.sql")
            with open(path, "w", encoding="utf-8") as f:
                f.write(definition)
    cursor.close()
    messagebox.showinfo("Export Complete", f"Exported {len(sp_list)} SPs to {export_dir}")

# ---------------------- RESULT WINDOW ----------------------
def show_compare_window(sp_only_db1, sp_only_db2, tbl_only_db1, tbl_only_db2):
    win = tk.Toplevel(root)
    win.title("Database Comparison Results")
    win.geometry("900x600")

    notebook = ttk.Notebook(win)
    notebook.pack(fill=tk.BOTH, expand=True)

    # SP Frame
    sp_frame = tk.Frame(notebook)
    notebook.add(sp_frame, text="Stored Procedures")

    tree_sp = ttk.Treeview(sp_frame, columns=("DB1", "DB2"), show="headings")
    tree_sp.heading("DB1", text="Only in DB1")
    tree_sp.heading("DB2", text="Only in DB2")
    tree_sp.pack(fill=tk.BOTH, expand=True)

    max_len = max(len(sp_only_db1), len(sp_only_db2))
    for i in range(max_len):
        left = sp_only_db1[i] if i < len(sp_only_db1) else ""
        right = sp_only_db2[i] if i < len(sp_only_db2) else ""
        tree_sp.insert("", "end", values=(left, right))

    # Color rows
    for child in tree_sp.get_children():
        vals = tree_sp.item(child, "values")
        if vals[0] and not vals[1]:
            tree_sp.item(child, tags=("db1",))
        elif vals[1] and not vals[0]:
            tree_sp.item(child, tags=("db2",))
    tree_sp.tag_configure("db1", background="#DFF2BF")  # greenish
    tree_sp.tag_configure("db2", background="#FFBABA")  # reddish

    btn_export = tk.Button(sp_frame, text="Export Missing SPs (from DB1)", bg="#4CAF50", fg="white",
                           command=lambda: export_missing_sps(sp_only_db1))
    btn_export.pack(pady=10)

    # Table Frame
    tbl_frame = tk.Frame(notebook)
    notebook.add(tbl_frame, text="Tables")

    tree_tbl = ttk.Treeview(tbl_frame, columns=("DB1", "DB2"), show="headings")
    tree_tbl.heading("DB1", text="Only in DB1")
    tree_tbl.heading("DB2", text="Only in DB2")
    tree_tbl.pack(fill=tk.BOTH, expand=True)

    max_len_t = max(len(tbl_only_db1), len(tbl_only_db2))
    for i in range(max_len_t):
        left = tbl_only_db1[i] if i < len(tbl_only_db1) else ""
        right = tbl_only_db2[i] if i < len(tbl_only_db2) else ""
        tree_tbl.insert("", "end", values=(left, right))

    for child in tree_tbl.get_children():
        vals = tree_tbl.item(child, "values")
        if vals[0] and not vals[1]:
            tree_tbl.item(child, tags=("db1",))
        elif vals[1] and not vals[0]:
            tree_tbl.item(child, tags=("db2",))
    tree_tbl.tag_configure("db1", background="#DFF2BF")
    tree_tbl.tag_configure("db2", background="#FFBABA")

# ---------------------- UI ----------------------
root = tk.Tk()
root.title("SQL Server Database Compare Tool")
root.geometry("900x400")

# DB1 Frame
frame_conn1 = tk.LabelFrame(root, text="Database 1", padx=10, pady=10)
frame_conn1.pack(fill=tk.X, padx=10, pady=5)

tk.Label(frame_conn1, text="Server:").grid(row=0, column=0)
entry_server1 = tk.Entry(frame_conn1, width=20)
entry_server1.grid(row=0, column=1)
tk.Label(frame_conn1, text="User:").grid(row=0, column=2)
entry_user1 = tk.Entry(frame_conn1, width=15)
entry_user1.grid(row=0, column=3)
tk.Label(frame_conn1, text="Pass:").grid(row=0, column=4)
entry_pass1 = tk.Entry(frame_conn1, width=15, show="*")
entry_pass1.grid(row=0, column=5)
tk.Button(frame_conn1, text="Load DBs",
          command=lambda: combo_db1.configure(values=get_all_databases(entry_server1.get(), entry_user1.get(), entry_pass1.get())),
          bg="#2196F3", fg="white").grid(row=0, column=6, padx=5)
combo_db1 = ttk.Combobox(frame_conn1, width=20, state="readonly")
combo_db1.grid(row=0, column=7)
tk.Button(frame_conn1, text="Connect", command=connect_db1, bg="#4CAF50", fg="white").grid(row=0, column=8, padx=5)

# DB2 Frame
frame_conn2 = tk.LabelFrame(root, text="Database 2", padx=10, pady=10)
frame_conn2.pack(fill=tk.X, padx=10, pady=5)

tk.Label(frame_conn2, text="Server:").grid(row=0, column=0)
entry_server2 = tk.Entry(frame_conn2, width=20)
entry_server2.grid(row=0, column=1)
tk.Label(frame_conn2, text="User:").grid(row=0, column=2)
entry_user2 = tk.Entry(frame_conn2, width=15)
entry_user2.grid(row=0, column=3)
tk.Label(frame_conn2, text="Pass:").grid(row=0, column=4)
entry_pass2 = tk.Entry(frame_conn2, width=15, show="*")
entry_pass2.grid(row=0, column=5)
tk.Button(frame_conn2, text="Load DBs",
          command=lambda: combo_db2.configure(values=get_all_databases(entry_server2.get(), entry_user2.get(), entry_pass2.get())),
          bg="#2196F3", fg="white").grid(row=0, column=6, padx=5)
combo_db2 = ttk.Combobox(frame_conn2, width=20, state="readonly")
combo_db2.grid(row=0, column=7)
tk.Button(frame_conn2, text="Connect", command=connect_db2, bg="#4CAF50", fg="white").grid(row=0, column=8, padx=5)

# Compare Button
tk.Button(root, text="Compare Databases", command=compare_databases,
          bg="#9C27B0", fg="white", font=("Arial", 11, "bold")).pack(pady=15)

root.mainloop()
# pyinstaller --onefile --windowed  exercise2.py