import pyodbc
import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, ttk, filedialog
from tkcalendar import DateEntry  # pip install tkcalendar

# -------------------- CONFIG --------------------
BACKUP_DIR = r"C:\Temp\SP_Backups"
os.makedirs(BACKUP_DIR, exist_ok=True)

# -------------------- GLOBALS --------------------
active_conn = None
sp_vars = {}
tbl_vars = {}
sp_count_label = None
tbl_count_label = None

def get_available_odbc_drivers():
    """Return a list of available ODBC drivers installed on the PC."""
    try:
        drivers = pyodbc.drivers()
        # Filter SQL Server drivers only
        drivers = [d for d in drivers if "SQL Server" in d]
        return sorted(drivers, reverse=True) or ["ODBC Driver 17 for SQL Server"]
    except Exception:
        return ["ODBC Driver 17 for SQL Server"]

# -------------------- DATABASE FUNCTIONS --------------------
def connect_db(driver, server, database, username, password):
    """Connect using selected ODBC driver."""
    conn_str = (
        f"DRIVER={{{driver}}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password}"
    )
    return pyodbc.connect(conn_str, autocommit=False)

def get_all_databases(driver, server, username, password):
    """Get database names using selected driver."""
    try:
        conn = pyodbc.connect(
            f"DRIVER={{{driver}}};"
            f"SERVER={server};DATABASE=master;"
            f"UID={username};PWD={password}"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sys.databases ORDER BY name")
        dbs = [row[0] for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return dbs
    except Exception as e:
        messagebox.showerror("Connection Error", f"Unable to retrieve databases:\n{e}")
        return []

def get_all_stored_procedures(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sys.objects WHERE type = 'P' ORDER BY name")
    result = [row[0] for row in cursor.fetchall()]
    cursor.close()
    return result

def get_all_tables(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sys.objects WHERE type = 'U' ORDER BY name")
    result = [row[0] for row in cursor.fetchall()]
    cursor.close()
    return result

# -------------------- SELECTION COUNTERS --------------------
def update_sp_count():
    if sp_count_label:
        sp_count_label.config(text=f"Selected: {sum(var.get() for var in sp_vars.values())}")

def update_tbl_count():
    if tbl_count_label:
        tbl_count_label.config(text=f"Selected: {sum(var.get() for var in tbl_vars.values())}")

# -------------------- BROWSE & EXECUTE Store Procedure--------------------
def browse_and_execute(sp_name):
    if not active_conn:
        messagebox.showwarning("No Connection", "Please connect to a database first.")
        return
    file_path = filedialog.askopenfilename(filetypes=[("SQL Files", "*.sql")])
    if not file_path:
        return
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            sql_script = f.read()
        # Replace CREATE PROCEDURE with ALTER PROCEDURE if exists
        lines = sql_script.splitlines()
        for i, line in enumerate(lines):
            if line.strip().upper().startswith("CREATE PROCEDURE"):
                lines[i] = line.replace("CREATE PROCEDURE", "ALTER PROCEDURE", 1)
        sql_script = "\n".join(lines)

        cursor = active_conn.cursor()
        # pyodbc can execute batch scripts; if script contains GO statements this may fail.
        # For complex scripts, a more robust batch-splitting is needed. For now try execute directly.
        cursor.execute(sql_script)
        active_conn.commit()
        cursor.close()
        messagebox.showinfo("Success", f"Script executed successfully for {sp_name}")
    except Exception as e:
        messagebox.showerror("Execution Error", f"Failed to execute script:\n{e}")

# -------------------- BROWSE & EXECUTE Table--------------------
def browse_and_execute_table(tbl_name):
    if not active_conn:
        messagebox.showwarning("No Connection", "Please connect to a database first.")
        return
    file_path = filedialog.askopenfilename(filetypes=[("SQL Files", "*.sql")])
    if not file_path:
        return
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            sql_script = f.read()
        cursor = active_conn.cursor()
        cursor.execute(sql_script)
        active_conn.commit()
        cursor.close()
        messagebox.showinfo("Success", f"Script executed successfully for table {tbl_name}")
    except Exception as e:
        messagebox.showerror("Execution Error", f"Failed to execute script:\n{e}")

# -------------------- BACKUP FUNCTIONS --------------------
def backup_stored_procedure(sp_name):
    cursor = active_conn.cursor()
    cursor.execute("""
        SELECT sm.definition
        FROM sys.sql_modules sm
        INNER JOIN sys.objects so ON sm.object_id = so.object_id
        WHERE so.type = 'P' AND so.name = ?
    """, (sp_name,))
    row = cursor.fetchone()
    if row:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = os.path.join(BACKUP_DIR, f"{sp_name}_backup_{timestamp}.sql")
        # Remove all GO statements
        sql = "\n".join([line for line in row.definition.splitlines() if not line.strip().upper() == "GO"])
        with open(backup_file, "w", encoding="utf-8") as f:
            f.write(sql)
    cursor.close()

# -------------------- Modify SP--------------------
def open_sp_modify_window(sp_name):
    if not active_conn:
        messagebox.showwarning("No Connection", "Please connect to a database first.")
        return

    win = tk.Toplevel(root)
    win.title(f"Modify & Execute Stored Procedure - {sp_name}")
    win.geometry("1000x650")

    # Frame for buttons
    button_frame = tk.Frame(win)
    button_frame.pack(fill=tk.X, pady=5)

    # Text box for SP code
    text_box = tk.Text(win, wrap="none", undo=True, font=("Consolas", 11))
    text_box.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    # Scrollbars
    yscroll = ttk.Scrollbar(win, orient="vertical", command=text_box.yview)
    yscroll.pack(side=tk.RIGHT, fill="y")
    text_box.configure(yscrollcommand=yscroll.set)

    # Load stored procedure definition
    try:
        cursor = active_conn.cursor()
        cursor.execute(
            f"""
            SELECT sm.definition
            FROM sys.sql_modules sm
            INNER JOIN sys.objects so ON sm.object_id = so.object_id
            WHERE so.name = ?
            """,
            (sp_name,)
        )
        row = cursor.fetchone()
        if row and row[0]:
            text_box.insert("1.0", row[0])
        else:
            messagebox.showinfo("Info", f"No source definition found for {sp_name}")
        cursor.close()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load stored procedure:\n{e}")
        return

    # ---- Button Actions ----
    def save_changes():
        sql_text = text_box.get("1.0", tk.END).strip()
        if not sql_text:
            messagebox.showwarning("Empty", "Stored procedure text cannot be empty.")
            return

        try:
            cursor = active_conn.cursor()
            cursor.execute(sql_text)
            active_conn.commit()
            cursor.close()
            messagebox.showinfo("Success", f"{sp_name} modified successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to alter procedure:\n{e}")

    def execute_sp():
        try:
            cursor = active_conn.cursor()
            cursor.execute(f"EXEC {sp_name}")
            try:
                columns = [desc[0] for desc in cursor.description]
                rows = cursor.fetchall()

                result_win = tk.Toplevel(win)
                result_win.title(f"Results - {sp_name}")
                result_win.geometry("900x400")

                tree = ttk.Treeview(result_win)
                tree.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
                sb = ttk.Scrollbar(result_win, orient="vertical", command=tree.yview)
                sb.pack(side=tk.RIGHT, fill="y")
                tree.configure(yscrollcommand=sb.set)

                tree["columns"] = columns
                tree["show"] = "headings"
                for col in columns:
                    tree.heading(col, text=col)
                    tree.column(col, width=150)
                for row in rows:
                    tree.insert("", tk.END, values=row)

            except Exception:
                messagebox.showinfo("Executed", f"{sp_name} executed successfully (no result set).")

            cursor.close()
        except Exception as e:
            messagebox.showerror("Execution Error", f"Error executing stored procedure:\n{e}")

    tk.Button(button_frame, text="Save Changes (ALTER)", command=save_changes, bg="#4CAF50", fg="white").pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Execute SP", command=execute_sp, bg="#2196F3", fg="white").pack(side=tk.LEFT, padx=5)


def backup_table(tbl_name):
    cursor = active_conn.cursor()
    cursor.execute("""
        SELECT 
            'CREATE TABLE [' + s.name + '].[' + t.name + '](' + CHAR(13) + CHAR(10) +
            STRING_AGG(
                '    [' + c.name + '] ' + 
                tp.name +
                CASE 
                    WHEN tp.name IN ('varchar','nvarchar','varbinary') THEN '(' + 
                        CASE WHEN c.max_length=-1 THEN 'MAX' ELSE CAST(c.max_length AS VARCHAR) END + ')'
                    WHEN tp.name IN ('decimal','numeric') THEN '(' + CAST(c.precision AS VARCHAR) + ',' + CAST(c.scale AS VARCHAR) + ')'
                    ELSE '' 
                END +
                CASE WHEN c.is_nullable=0 THEN ' NOT NULL' ELSE '' END
                , ',' + CHAR(13) + CHAR(10)
            ) WITHIN GROUP (ORDER BY c.column_id) +
            CHAR(13) + CHAR(10) + ');' AS TableScript
        FROM sys.tables t
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        INNER JOIN sys.columns c ON t.object_id = c.object_id
        INNER JOIN sys.types tp ON c.user_type_id = tp.user_type_id
        WHERE t.name = ?
        GROUP BY t.name, s.name
    """, (tbl_name,))
    row = cursor.fetchone()
    if row and getattr(row, "TableScript", None):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = os.path.join(BACKUP_DIR, f"{tbl_name}_backup_{timestamp}.sql")
        with open(backup_file, "w", encoding="utf-8") as f:
            f.write(row.TableScript)
    cursor.close()

# -------------------- EXPORT FUNCTION --------------------

# -------------------- HIGHLIGHT CHECKBOX --------------------
def update_checkbox_color(var, frame):
    if var.get():
        frame.config(bg="#C8E6C9")  # Light green
        for child in frame.winfo_children():
            try:
                child.config(bg="#C8E6C9")
            except Exception:
                pass
    else:
        frame.config(bg=root.cget("bg"))  # Default
        for child in frame.winfo_children():
            try:
                child.config(bg=root.cget("bg"))
            except Exception:
                pass

def get_sp_parameters(conn, sp_name):
    cursor = conn.cursor()
    query = """
        SELECT 
            p.name AS ParameterName,
            t.name AS DataType,
            p.is_output AS IsOutput
        FROM sys.parameters p
        INNER JOIN sys.types t ON p.user_type_id = t.user_type_id
        INNER JOIN sys.objects o ON p.object_id = o.object_id
        WHERE o.name = ?
        ORDER BY p.parameter_id
    """
    cursor.execute(query, (sp_name,))
    params = [(row[0], row[1], row[2]) for row in cursor.fetchall()]
    cursor.close()
    return params


def open_sp_execution_window(sp_name):
    if not active_conn:
        messagebox.showwarning("No Connection", "Please connect to a database first.")
        return

    exec_win = tk.Toplevel(root)
    exec_win.title(f"Execute Stored Procedure - {sp_name}")
    exec_win.geometry("900x550")

    try:
        param_defs = get_sp_parameters(active_conn, sp_name)  # renamed to avoid collision
    except Exception as e:
        messagebox.showerror("Error", f"Unable to fetch parameters:\n{e}")
        return

    param_frame = tk.LabelFrame(exec_win, text="Procedure Parameters", padx=10, pady=10)
    param_frame.pack(fill=tk.X, padx=10, pady=10)

    entries = {}
    for i, (name, dtype, is_output) in enumerate(param_defs):
        direction = "OUTPUT" if is_output else "INPUT"
        tk.Label(param_frame, text=f"{name} ({dtype}, {direction})").grid(row=i, column=0, sticky="w", padx=5, pady=3)

        dtype_lower = dtype.lower()
        if any(x in dtype_lower for x in ["char", "text", "nchar", "ntext"]):
            widget = tk.Entry(param_frame, width=40)
        elif any(x in dtype_lower for x in ["int", "decimal", "numeric", "float", "money", "real"]):
            widget = tk.Entry(param_frame, width=20)
        elif "date" in dtype_lower:
            widget = DateEntry(param_frame, width=20, date_pattern="yyyy-mm-dd")
        elif "bit" in dtype_lower:
            widget = ttk.Combobox(param_frame, values=["0", "1"], width=5)
            widget.set("0")
        else:
            widget = tk.Entry(param_frame, width=30)

        widget.grid(row=i, column=1, padx=5, pady=2)
        entries[name] = (widget, dtype_lower, is_output)

    # Frame for results
    result_frame = tk.Frame(exec_win)
    result_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    tree = ttk.Treeview(result_frame)
    tree.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
    scrollbar = ttk.Scrollbar(result_frame, orient="vertical", command=tree.yview)
    scrollbar.pack(side=tk.RIGHT, fill="y")
    tree.configure(yscrollcommand=scrollbar.set)

    def execute_sp():
        cursor = None
        try:
            cursor = active_conn.cursor()
            param_values = []

            # Build parameter values list
            for name, (widget, dtype, is_output) in entries.items():
                val = None
                try:
                    raw = widget.get().strip()
                except Exception:
                    raw = ""
                if raw == "":
                    val = None
                else:
                    try:
                        if dtype in ("int", "smallint", "tinyint", "bigint"):
                            val = int(raw)
                        elif dtype in ("decimal", "numeric", "float", "money", "real"):
                            val = float(raw)
                        elif "bit" in dtype:
                            val = 1 if raw in ("1", "true", "True", "TRUE") else 0
                        elif "date" in dtype:
                            # DateEntry returns yyyy-mm-dd
                            val = datetime.strptime(raw, "%Y-%m-%d")
                        else:
                            val = raw
                    except Exception:
                        val = raw

                # For OUTPUT params we currently pass None placeholder (capturing outputs requires different handling)
                param_values.append(val)

            # Use ODBC CALL syntax
            placeholder_str = ", ".join(["?"] * len(param_values))
            if placeholder_str:
                sql = f"{{CALL {sp_name} ({placeholder_str})}}"
            else:
                sql = f"{{CALL {sp_name}}}"

            print("Executing:", sql, "with", param_values)
            cursor.execute(sql, tuple(param_values))

            # Try to display resultset
            try:
                columns = [desc[0] for desc in cursor.description]
                rows = cursor.fetchall()

                result_win = tk.Toplevel(exec_win)
                result_win.title(f"Results - {sp_name}")
                result_win.geometry("900x400")

                tree = ttk.Treeview(result_win)
                tree.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
                sb = ttk.Scrollbar(result_win, orient="vertical", command=tree.yview)
                sb.pack(side=tk.RIGHT, fill="y")
                tree.configure(yscrollcommand=sb.set)

                tree["columns"] = columns
                tree["show"] = "headings"
                for col in columns:
                    tree.heading(col, text=col)
                    tree.column(col, width=150)
                for row in rows:
                    tree.insert("", tk.END, values=row)

            except Exception:
                messagebox.showinfo("Execution Complete", "Stored procedure executed successfully (no result set).")

        except Exception as e:
            messagebox.showerror("Execution Error", f"Error executing stored procedure:\n{e}")
        finally:
            if cursor:
                cursor.close()

    tk.Button(exec_win, text="Execute", command=execute_sp, bg="#4CAF50", fg="white", width=15).pack(pady=8)

# -------------------- REFRESH CHECKBOXES --------------------
def refresh_sp_checkboxes():
    for widget in inner_frame_sp.winfo_children():
        widget.destroy()
    sp_vars.clear()
    global sp_count_label
    sp_count_label = tk.Label(inner_frame_sp, text="Selected: 0", fg="blue", font=("Arial", 10, "bold"))
    sp_count_label.pack(anchor="w", pady=(0,5))

    try:
        sp_list = get_all_stored_procedures(active_conn)
        for sp in sp_list:
            var = tk.BooleanVar()
            frame_row = tk.Frame(inner_frame_sp)
            frame_row.pack(fill="x", anchor="w", pady=1)
            chk = tk.Checkbutton(frame_row, text=sp, variable=var,
                                 command=lambda v=var, f=frame_row: [update_sp_count(), update_checkbox_color(v, f)])
            chk.pack(side=tk.LEFT, anchor="w")
            btn = tk.Button(frame_row, text="Browse & Execute", command=lambda s=sp: browse_and_execute(s),
                            bg="#00BCD4", fg="white")
            btn.pack(side=tk.RIGHT, padx=5)
            sp_vars[sp] = var
    except Exception as e:
        messagebox.showerror("Error", f"Unable to load SPs:\n{e}")
    update_sp_count()

def refresh_tbl_checkboxes():
    for widget in inner_frame_tbl.winfo_children():
        widget.destroy()
    tbl_vars.clear()
    global tbl_count_label
    tbl_count_label = tk.Label(inner_frame_tbl, text="Selected: 0", fg="blue", font=("Arial", 10, "bold"))
    tbl_count_label.pack(anchor="w", pady=(0,5))

    try:
        tbl_list = get_all_tables(active_conn)
        for tbl in tbl_list:
            var = tk.BooleanVar()
            frame_row = tk.Frame(inner_frame_tbl)
            frame_row.pack(fill="x", anchor="w", pady=1)
            chk = tk.Checkbutton(frame_row, text=tbl, variable=var,
                                 command=lambda v=var, f=frame_row: [update_tbl_count(), update_checkbox_color(v, f)])
            chk.pack(side=tk.LEFT, anchor="w")
            btn = tk.Button(frame_row, text="Browse & Execute", command=lambda t=tbl: browse_and_execute_table(t),
                            bg="#00BCD4", fg="white")
            btn.pack(side=tk.RIGHT, padx=5)
            tbl_vars[tbl] = var
    except Exception as e:
        messagebox.showerror("Error", f"Unable to load Tables:\n{e}")
    update_tbl_count()
#Progress Bar UI
from tkinter import ttk

def refresh_sp_checkboxes():
    for widget in inner_frame_sp.winfo_children():
        widget.destroy()
    sp_vars.clear()
    global sp_count_label
    sp_count_label = tk.Label(inner_frame_sp, text="Selected: 0", fg="blue", font=("Arial", 10, "bold"))
    sp_count_label.pack(anchor="w", pady=(0,5))

    # Progress bar frame
    progress_frame = tk.Frame(inner_frame_sp)
    progress_frame.pack(fill="x", pady=5)
    tk.Label(progress_frame, text="Loading Stored Procedures...", fg="gray").pack(anchor="w")
    progress = ttk.Progressbar(progress_frame, mode="determinate")
    progress.pack(fill="x", padx=5, pady=2)

    root.update_idletasks()

    try:
        sp_list = get_all_stored_procedures(active_conn)
        total = len(sp_list)
        if total == 0:
            tk.Label(inner_frame_sp, text="No stored procedures found.", fg="red").pack(anchor="w", pady=5)
            progress_frame.destroy()
            return

        progress["maximum"] = total

        for i, sp in enumerate(sp_list, 1):
            var = tk.BooleanVar()
            frame_row = tk.Frame(inner_frame_sp)
            frame_row.pack(fill="x", anchor="w", pady=1)
            chk = tk.Checkbutton(frame_row, text=sp, variable=var,
                                 command=lambda v=var, f=frame_row: [update_sp_count(), update_checkbox_color(v, f)])
            chk.pack(side=tk.LEFT, anchor="w")
            btn = tk.Button(frame_row, text="Browse & Execute", command=lambda s=sp: browse_and_execute(s),
                            bg="#00BCD4", fg="white")
            btn.pack(side=tk.RIGHT, padx=5)
            sp_vars[sp] = var

            # Update progress bar
            progress["value"] = i
            root.update_idletasks()

        progress_frame.destroy()
    except Exception as e:
        progress_frame.destroy()
        messagebox.showerror("Error", f"Unable to load SPs:\n{e}")

    update_sp_count()


def refresh_tbl_checkboxes():
    for widget in inner_frame_tbl.winfo_children():
        widget.destroy()
    tbl_vars.clear()
    global tbl_count_label
    tbl_count_label = tk.Label(inner_frame_tbl, text="Selected: 0", fg="blue", font=("Arial", 10, "bold"))
    tbl_count_label.pack(anchor="w", pady=(0,5))

    # Progress bar frame
    progress_frame = tk.Frame(inner_frame_tbl)
    progress_frame.pack(fill="x", pady=5)
    tk.Label(progress_frame, text="Loading Tables...", fg="gray").pack(anchor="w")
    progress = ttk.Progressbar(progress_frame, mode="determinate")
    progress.pack(fill="x", padx=5, pady=2)

    root.update_idletasks()

    try:
        tbl_list = get_all_tables(active_conn)
        total = len(tbl_list)
        if total == 0:
            tk.Label(inner_frame_tbl, text="No tables found.", fg="red").pack(anchor="w", pady=5)
            progress_frame.destroy()
            return

        progress["maximum"] = total

        for i, tbl in enumerate(tbl_list, 1):
            var = tk.BooleanVar()
            frame_row = tk.Frame(inner_frame_tbl)
            frame_row.pack(fill="x", anchor="w", pady=1)
            chk = tk.Checkbutton(frame_row, text=tbl, variable=var,
                                 command=lambda v=var, f=frame_row: [update_tbl_count(), update_checkbox_color(v, f)])
            chk.pack(side=tk.LEFT, anchor="w")
            btn = tk.Button(frame_row, text="Browse & Execute", command=lambda t=tbl: browse_and_execute_table(t),
                            bg="#00BCD4", fg="white")
            btn.pack(side=tk.RIGHT, padx=5)
            tbl_vars[tbl] = var

            # Update progress bar
            progress["value"] = i
            root.update_idletasks()

        progress_frame.destroy()
    except Exception as e:
        progress_frame.destroy()
        messagebox.showerror("Error", f"Unable to load Tables:\n{e}")

    update_tbl_count()

# -------------------- GUI SETUP --------------------
root = tk.Tk()
root.title("SQL SP & Tables Exporter with Backup")
root.geometry("1440x800")  # fixed typo from 14400

# Connection Frame
frame_conn = tk.LabelFrame(root, text="Database Connection", padx=10, pady=10)
frame_conn.pack(fill=tk.X, padx=20, pady=5)

# ODBC Driver dropdown
tk.Label(frame_conn, text="ODBC Driver:").grid(row=0, column=0, sticky="w")
combo_driver = ttk.Combobox(frame_conn, width=30, state="readonly")
combo_driver['values'] = get_available_odbc_drivers()
try:
    combo_driver.current(0)
except Exception:
    pass
combo_driver.grid(row=0, column=1, padx=5)

tk.Label(frame_conn, text="Server:").grid(row=0, column=2)
entry_server = tk.Entry(frame_conn, width=25)
entry_server.grid(row=0, column=3)
tk.Label(frame_conn, text="Username:").grid(row=0, column=4)
entry_user = tk.Entry(frame_conn, width=20)
entry_user.grid(row=0, column=5)
tk.Label(frame_conn, text="Password:").grid(row=0, column=6)
entry_pass = tk.Entry(frame_conn, width=20, show="*")
entry_pass.grid(row=0, column=7)

# Fix: pass driver argument to get_all_databases
tk.Button(frame_conn, text="Load DBs", command=lambda: combo_db.configure(values=get_all_databases(combo_driver.get().strip() or combo_driver['values'][0], entry_server.get(), entry_user.get(), entry_pass.get())), bg="#2196F3", fg="white").grid(row=0, column=8, padx=5)

combo_db = ttk.Combobox(frame_conn, width=25, state="readonly")
combo_db.grid(row=1, column=3)
tk.Button(frame_conn, text="Connect", command=lambda: connect_and_refresh(), bg="#4CAF50", fg="white").grid(row=1, column=4)

def connect_and_refresh():
    global active_conn
    driver = combo_driver.get().strip() or (combo_driver['values'][0] if combo_driver['values'] else "")
    server = entry_server.get().strip()
    database = combo_db.get().strip()
    username = entry_user.get().strip()
    password = entry_pass.get().strip()
    if not all([driver, server, database, username, password]):
        messagebox.showwarning("Missing Info", "Please fill all connection details.")
        return
    try:
        active_conn = connect_db(driver, server, database, username, password)
        refresh_sp_checkboxes()
        refresh_tbl_checkboxes()
        messagebox.showinfo("Connected", f"Connected successfully using {driver}")
    except Exception as e:
        messagebox.showerror("Connection Error", f"Unable to connect:\n{e}")

# table part
def open_table_update_window(table_name):
    if not active_conn:
        messagebox.showwarning("No Connection", "Please connect to a database first.")
        return

    upd_win = tk.Toplevel(root)
    upd_win.title(f"Update Table - {table_name}")
    upd_win.geometry("1000x600")

    frame = tk.Frame(upd_win)
    frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    tree = ttk.Treeview(frame)
    tree.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    scrollbar.pack(side=tk.RIGHT, fill="y")
    tree.configure(yscrollcommand=scrollbar.set)

    cursor = active_conn.cursor()
    try:
        cursor.execute(f"SELECT TOP 100 * FROM {table_name}")  # load first 100 rows
        columns = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        tree["columns"] = columns
        tree["show"] = "headings"

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)

        for row in rows:
            tree.insert("", tk.END, values=row)

    except Exception as e:
        messagebox.showerror("Error", f"Unable to load table:\n{e}")
        upd_win.destroy()
        return
    finally:
        cursor.close()

    # ---- Editing feature ----
    edit_frame = tk.Frame(upd_win)
    edit_frame.pack(fill=tk.X, padx=10, pady=5)

    tk.Label(edit_frame, text="Double-click a cell to edit. Then click 'Save Changes' to update the database.").pack(anchor="w")

    edited_rows = {}

    def on_double_click(event):
        item = tree.identify_row(event.y)
        col = tree.identify_column(event.x)
        if not item or not col:
            return

        col_index = int(col.replace("#", "")) - 1
        col_name = columns[col_index]
        old_value = tree.item(item, "values")[col_index]

        edit_popup = tk.Toplevel(upd_win)
        edit_popup.title("Edit Value")
        edit_popup.geometry("300x120")
        tk.Label(edit_popup, text=f"{col_name}:").pack(pady=5)
        entry = tk.Entry(edit_popup)
        entry.insert(0, old_value)
        entry.pack(pady=5)

        def save_edit():
            new_value = entry.get()
            values = list(tree.item(item, "values"))
            values[col_index] = new_value
            tree.item(item, values=values)
            edited_rows[item] = values
            edit_popup.destroy()

        tk.Button(edit_popup, text="Save", command=save_edit, bg="#4CAF50", fg="white").pack(pady=5)

    tree.bind("<Double-1>", on_double_click)

# Main Frame
frame_main = tk.Frame(root)
frame_main.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

# SP Frame
frame_sp = tk.Frame(frame_main)
frame_sp.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0,10))
tk.Label(frame_sp, text="Stored Procedures").pack(anchor="w")
canvas_sp = tk.Canvas(frame_sp)
scroll_sp = tk.Scrollbar(frame_sp, orient="vertical", command=canvas_sp.yview)
scroll_sp.pack(side=tk.RIGHT, fill=tk.Y)
canvas_sp.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
inner_frame_sp = tk.Frame(canvas_sp)
canvas_sp.create_window((0,0), window=inner_frame_sp, anchor="nw")
canvas_sp.configure(yscrollcommand=scroll_sp.set)
inner_frame_sp.bind("<Configure>", lambda e: canvas_sp.configure(scrollregion=canvas_sp.bbox("all")))

# Tables Frame
frame_tbl = tk.Frame(frame_main)
frame_tbl.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10,0))
tk.Label(frame_tbl, text="Tables").pack(anchor="w")
canvas_tbl = tk.Canvas(frame_tbl)
scroll_tbl = tk.Scrollbar(frame_tbl, orient="vertical", command=canvas_tbl.yview)
scroll_tbl.pack(side=tk.RIGHT, fill=tk.Y)
canvas_tbl.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
inner_frame_tbl = tk.Frame(canvas_tbl)
canvas_tbl.create_window((0,0), window=inner_frame_tbl, anchor="nw")
canvas_tbl.configure(yscrollcommand=scroll_tbl.set)
inner_frame_tbl.bind("<Configure>", lambda e: canvas_tbl.configure(scrollregion=canvas_tbl.bbox("all")))

# Buttons
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)
tk.Button(frame_buttons, text="Refresh Lists", command=lambda: [refresh_sp_checkboxes(), refresh_tbl_checkboxes()], bg="#9C27B0", fg="white").pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons, text="Open Selected Table(s)", command=lambda: [open_table_update_window(tbl) for tbl, var in tbl_vars.items() if var.get()], bg="#03A9F4", fg="white").pack(side=tk.LEFT, padx=5)
tk.Button(
    frame_buttons,
    text="Open SP for Modify/Execute",
    command=lambda: [open_sp_modify_window(sp) for sp, var in sp_vars.items() if var.get()],
    bg="#795548",
    fg="white"
).pack(side=tk.LEFT, padx=5)

root.mainloop()
