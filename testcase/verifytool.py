import re
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

pattern = r'<add\s+key="([^"]+)"\s+value="([^"]+)"\s*/?>'

class App:
    def __init__(self, root):
        self.root = root
        root.title("Web.Config Key-Value Extractor")

        # Select file button
        self.btn_select = tk.Button(root, text="Select Web.Config File", command=self.load_file)
        self.btn_select.pack(pady=5)

        # Text area to display results
        self.text_area = scrolledtext.ScrolledText(root, width=70, height=20)
        self.text_area.pack(pady=5)

        # Save buttons frame
        frame = tk.Frame(root)
        frame.pack(pady=5)

        self.btn_save_overwrite = tk.Button(frame, text="Save (Overwrite)", command=lambda: self.save_results(append=False))
        self.btn_save_overwrite.pack(side=tk.LEFT, padx=5)

        self.btn_save_append = tk.Button(frame, text="Save (Append)", command=lambda: self.save_results(append=True))
        self.btn_save_append.pack(side=tk.LEFT, padx=5)

        # Store extracted results here
        self.results = []

    def load_file(self):
        file_path = filedialog.askopenfilename(title="Select Web.Config File", filetypes=[("Config Files", "*.config"), ("All Files", "*.*")])
        if not file_path:
            return
        self.results.clear()
        self.text_area.delete(1.0, tk.END)

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip().startswith('<add key'):
                        match = re.search(pattern, line)
                        if match:
                            key = match.group(1)
                            value = match.group(2)
                            entry = f"{key:<30} | {value:<20}"
                            self.results.append(entry)

            if not self.results:
                self.text_area.insert(tk.END, "No matching <add key=... value=... /> lines found.\n")
            else:
                self.text_area.insert(tk.END, f"{'Key':<30} | {'Value':<20}\n")
                self.text_area.insert(tk.END, "-" * 55 + "\n")
                self.text_area.insert(tk.END, "\n".join(self.results))

        except Exception as e:
            messagebox.showerror("Error", f"Failed to read file:\n{e}")

    def save_results(self, append=False):
        if not self.results:
            messagebox.showinfo("Info", "No data to save. Please load a file first.")
            return

        mode = 'a' if append else 'w'
        try:
            with open("result.txt", mode, encoding='utf-8') as f:
                if not append:
                    f.write("✅ Filterdata\n")
                f.write("\n".join(self.results) + "\n")

            messagebox.showinfo("Success", f"Results saved to result.txt ({'appended' if append else 'overwritten'}).")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
