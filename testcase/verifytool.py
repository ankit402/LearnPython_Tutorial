import re
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

pattern = r'<add\s+key="([^"]+)"\s+value="([^"]+)"\s*/?>'

class ConfigComparer:
    def __init__(self, root):
        self.root = root
        root.title("Web.Config Comparer (Side-by-Side)")
        root.geometry("1200x700")

        # Top Buttons
        frame_buttons = tk.Frame(root)
        frame_buttons.pack(pady=10)

        tk.Button(frame_buttons, text="Load File 1", command=self.load_file1).pack(side=tk.LEFT, padx=10)
        tk.Button(frame_buttons, text="Load File 2", command=self.load_file2).pack(side=tk.LEFT, padx=10)
        tk.Button(frame_buttons, text="Compare Files", command=self.compare).pack(side=tk.LEFT, padx=10)

        # Text Area
        self.text_area = scrolledtext.ScrolledText(root, width=160, height=30, font=("Consolas", 11))
        self.text_area.pack(padx=10, pady=10)

        # Tag styles
        self.text_area.tag_config("header", font=("Consolas", 11, "bold"))
        self.text_area.tag_config("diff", foreground="red", font=("Consolas", 11, "bold"))
        self.text_area.tag_config("match", foreground="green")

        # Data holders
        self.data1 = {}
        self.data2 = {}

    def load_file(self, title):
        file_path = filedialog.askopenfilename(title=title, filetypes=[("Config Files", "*.config"), ("All Files", "*.*")])
        if not file_path:
            return None
        data = {}
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    match = re.search(pattern, line.strip())
                    if match:
                        key, value = match.group(1), match.group(2)
                        data[key] = value
            return data
        except Exception as e:
            messagebox.showerror("Error", f"Error loading file: {e}")
            return None

    def load_file1(self):
        self.data1 = self.load_file("Select First Web.Config File")
        messagebox.showinfo("Success", "File 1 loaded successfully.")

    def load_file2(self):
        self.data2 = self.load_file("Select Second Web.Config File")
        messagebox.showinfo("Success", "File 2 loaded successfully.")

    def compare(self):
        if not self.data1 or not self.data2:
            messagebox.showwarning("Missing Files", "Please load both config files first.")
            return

        self.text_area.delete(1.0, tk.END)
        all_keys = sorted(set(self.data1.keys()).union(set(self.data2.keys())))

        # Header row
        self.text_area.insert(tk.END, f"{'Key':<50} | {'File 1 Value':<50} | {'File 2 Value':<50}\n", "header")
        self.text_area.insert(tk.END, "-" * 160 + "\n")

        for key in all_keys:
            val1 = self.data1.get(key, "❌ MISSING")
            val2 = self.data2.get(key, "❌ MISSING")
            line = f"{key:<50} | {val1:<50} | {val2:<50}\n"

            if val1 != val2:
                self.text_area.insert(tk.END, line, "diff")

            else:
                self.text_area.insert(tk.END, line, "match")

        self.text_area.insert(tk.END, "\n✅ Comparison complete.\n", "header")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConfigComparer(root)
    root.mainloop()
