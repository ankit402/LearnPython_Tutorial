import os
import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# ---------- Hex <-> Text Conversion ----------
def hex_to_text(value):
    try:
        if all(c in "0123456789ABCDEFabcdef" for c in value) and len(value) % 2 == 0 and value != '':
            return bytes.fromhex(value).decode('utf-8')
    except:
        pass
    return value

def text_to_hex(value):
    try:
        return value.encode('utf-8').hex()
    except:
        return value


# ---------- Insert XML into Treeview ----------
def insert_tree(treeview, parent, node, tag='normal'):
    drag_handle = "☰ "
    name_display = drag_handle + node.attrib.get('NAME', '')
    type_display = node.attrib.get('TYPE', '')
    value_display = hex_to_text(node.attrib.get('VALUE', ''))

    node_id = treeview.insert(parent, 'end',
                              text=name_display,
                              values=(type_display, value_display),
                              tags=(tag,))
    for child in node:
        insert_tree(treeview, node_id, child, tag)


# ---------- Load XML ----------
def browse_xml(tree_attr_prefix):
    file_path = filedialog.askopenfilename(
        filetypes=[("XML files", "*.xml")],
        title="Select XML File"
    )
    if not file_path:
        return None  # Return None so caller knows no file selected

    try:
        xml_tree = ET.parse(file_path)
        xml_root = xml_tree.getroot()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load XML:\n{e}")
        return None

    # Store references globally
    setattr(root_window, f"{tree_attr_prefix}_tree", xml_tree)
    setattr(root_window, f"{tree_attr_prefix}_root", xml_root)
    setattr(root_window, f"{tree_attr_prefix}_file", file_path)

    # Populate Treeview
    treeview = getattr(root_window, f"{tree_attr_prefix}_treeview")
    for item in treeview.get_children():
        treeview.delete(item)

    for node in xml_root.findall('NODE'):
        insert_tree(treeview, '', node)

    return file_path


# ---------- Save XML ----------
def save_xml(tree_attr_prefix):
    if not hasattr(root_window, f"{tree_attr_prefix}_tree"):
        messagebox.showwarning("Warning", "Load XML first!")
        return

    treeview = getattr(root_window, f"{tree_attr_prefix}_treeview")
    xml_tree = getattr(root_window, f"{tree_attr_prefix}_tree")
    xml_root = getattr(root_window, f"{tree_attr_prefix}_root")

    def update_xml(tv_node_id, xml_node):
        # Update VALUE in XML from Treeview
        value = treeview.set(tv_node_id, 'Value')
        xml_node.set('VALUE', text_to_hex(value) if not all(c in "0123456789ABCDEFabcdef" for c in value) else value)

        children_tv = treeview.get_children(tv_node_id)
        for i, child_id in enumerate(children_tv):
            update_xml(child_id, list(xml_node)[i])

    # Update root nodes
    root_tv_nodes = treeview.get_children()
    for i, tv_node_id in enumerate(root_tv_nodes):
        update_xml(tv_node_id, list(xml_root)[i])

    # Ask file path to save
    file_path = filedialog.asksaveasfilename(
        defaultextension=".xml",
        filetypes=[("XML files", "*.xml")],
        title="Save XML As"
    )
    if file_path:
        xml_tree.write(file_path, encoding='utf-8', xml_declaration=True)
        messagebox.showinfo("Success", f"XML saved to {file_path}")


# ---------- Right-Click Editing ----------
def edit_value(tree_node_id, treeview):
    bbox = treeview.bbox(tree_node_id, 'Value')
    if not bbox:
        return
    x, y, width, height = bbox
    value = treeview.set(tree_node_id, 'Value')

    entry = tk.Entry(treeview)
    entry.insert(0, value)
    entry.place(x=x, y=y, width=width, height=height)
    entry.focus_set()

    def save_edit(event=None):
        treeview.set(tree_node_id, 'Value', entry.get())
        entry.destroy()

    entry.bind('<Return>', save_edit)
    entry.bind('<FocusOut>', save_edit)


def on_right_click(event, treeview):
    item_id = treeview.identify_row(event.y)
    if not item_id:
        return
    menu = tk.Menu(root_window, tearoff=0)
    menu.add_command(label="Edit Value", command=lambda: edit_value(item_id, treeview))
    menu.post(event.x_root, event.y_root)


# ---------- Drag & Drop ----------
dragging_item = None
dragging_tree = None

def on_start_drag(event, treeview):
    global dragging_item, dragging_tree
    dragging_item = treeview.identify_row(event.y)
    dragging_tree = treeview

def on_drag_motion(event):
    global dragging_item, dragging_tree
    if dragging_item and dragging_tree:
        dragging_tree.selection_set(dragging_item)

def on_drop(event):
    global dragging_item, dragging_tree
    if dragging_item and dragging_tree:
        target_item = dragging_tree.identify_row(event.y)
        if not target_item or target_item == dragging_item:
            dragging_item = None
            dragging_tree = None
            return
        dragging_tree.move(dragging_item, target_item, 'end')
        dragging_item = None
        dragging_tree = None


# ---------- Compare XML ----------
def compare_xmls():
    if not hasattr(root_window, 'tree1_root') or not hasattr(root_window, 'tree2_root'):
        messagebox.showwarning("Warning", "Load both XMLs first!")
        return

    tree1_tv = root_window.tree1_treeview
    tree2_tv = root_window.tree2_treeview
    tree1_tv.tag_configure('diff', background='yellow')
    tree2_tv.tag_configure('diff', background='yellow')

    def compare_and_highlight(tv1, tv2, node1_id, node2_id, xml1, xml2):
        if (xml1.attrib.get('NAME') != xml2.attrib.get('NAME') or
            xml1.attrib.get('TYPE') != xml2.attrib.get('TYPE') or
            xml1.attrib.get('VALUE') != xml2.attrib.get('VALUE')):
            tv1.item(node1_id, tags=('diff',))
            tv2.item(node2_id, tags=('diff',))

        children1 = list(xml1)
        children2 = list(xml2)
        for i, (child1, child2) in enumerate(zip(children1, children2)):
            c1_id = tv1.get_children(node1_id)[i]
            c2_id = tv2.get_children(node2_id)[i]
            compare_and_highlight(tv1, tv2, c1_id, c2_id, child1, child2)

    for n1, n2, xml1, xml2 in zip(tree1_tv.get_children(), tree2_tv.get_children(),
                                  root_window.tree1_root.findall('NODE'),
                                  root_window.tree2_root.findall('NODE')):
        compare_and_highlight(tree1_tv, tree2_tv, n1, n2, xml1, xml2)

    messagebox.showinfo("Compare Result", "Differences highlighted in yellow.")


# ---------- GUI ----------
root_window = tk.Tk()
root_window.title("XML Compare Editor V1.2")
root_window.geometry("1200x800")

tree_frame = ttk.Frame(root_window)
tree_frame.pack(fill='both', expand=True, padx=5, pady=5)

# Tree 1 frame
frame1 = ttk.Frame(tree_frame)
frame1.pack(side='left', fill='both', expand=True, padx=5, pady=5)

tree1_label = tk.Label(frame1, text="XML 1: Not loaded", font=("Arial", 10))
tree1_label.pack(pady=2)

# Tree 2 frame
frame2 = ttk.Frame(tree_frame)
frame2.pack(side='left', fill='both', expand=True, padx=5, pady=5)

tree2_label = tk.Label(frame2, text="XML 2: Not loaded", font=("Arial", 10))
tree2_label.pack(pady=2)

columns = ('Type', 'Value')

# Tree 1
tree1 = ttk.Treeview(frame1, columns=columns, show='tree headings')
tree1.heading('#0', text='Node Name', anchor='w')
tree1.heading('Type', text='Type', anchor='w')
tree1.heading('Value', text='Value', anchor='w')
tree1.column('#0', width=300)
tree1.column('Type', width=150)
tree1.column('Value', width=250)
tree1.pack(fill='both', expand=True)
scroll1 = ttk.Scrollbar(frame1, orient="vertical", command=tree1.yview)
scroll1.pack(side='right', fill='y')
tree1.configure(yscrollcommand=scroll1.set)
root_window.tree1_treeview = tree1

# Tree 2
tree2 = ttk.Treeview(frame2, columns=columns, show='tree headings')
tree2.heading('#0', text='Node Name', anchor='w')
tree2.heading('Type', text='Type', anchor='w')
tree2.heading('Value', text='Value', anchor='w')
tree2.column('#0', width=300)
tree2.column('Type', width=150)
tree2.column('Value', width=250)
tree2.pack(fill='both', expand=True)
scroll2 = ttk.Scrollbar(frame2, orient="vertical", command=tree2.yview)
scroll2.pack(side='right', fill='y')
tree2.configure(yscrollcommand=scroll2.set)
root_window.tree2_treeview = tree2

# Buttons
btn_frame = ttk.Frame(root_window)
btn_frame.pack(fill='x', pady=5)

def load_xml1():
    file_path = browse_xml('tree1')
    if file_path:
        tree1_label.config(text=f"XML 1: {os.path.basename(file_path)}")

def load_xml2():
    file_path = browse_xml('tree2')
    if file_path:
        tree2_label.config(text=f"XML 2: {os.path.basename(file_path)}")

tk.Button(btn_frame, text="Load XML 1", command=load_xml1, bg="#2196F3", fg="white", width=15).pack(side='left', padx=5)
tk.Button(btn_frame, text="Load XML 2", command=load_xml2, bg="#FF9800", fg="white", width=15).pack(side='left', padx=5)
tk.Button(btn_frame, text="Compare XMLs", command=compare_xmls, bg="#4CAF50", fg="white", width=15).pack(side='left', padx=5)
tk.Button(btn_frame, text="Save XML 1", command=lambda: save_xml('tree1'), bg="#607D8B", fg="white", width=15).pack(side='left', padx=5)
tk.Button(btn_frame, text="Save XML 2", command=lambda: save_xml('tree2'), bg="#607D8B", fg="white", width=15).pack(side='left', padx=5)

# Bindings
tree1.bind('<Button-3>', lambda e: on_right_click(e, tree1))
tree2.bind('<Button-3>', lambda e: on_right_click(e, tree2))
for tv in [tree1, tree2]:
    tv.bind("<ButtonPress-1>", lambda e, tv=tv: on_start_drag(e, tv))
    tv.bind("<B1-Motion>", on_drag_motion)
    tv.bind("<ButtonRelease-1>", on_drop)

root_window.mainloop()
