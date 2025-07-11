import tkinter as tk
from tkinter import messagebox, font

class ToDoApp:
    def _init_(self, root):
        self.root = root
        self.root.title("🎉 Vibrant To-Do List 🎉")
        self.root.geometry("450x400")
        self.root.config(bg="#282c34")

        self.tasks = []

        # Colors and fonts
        bg_color = "#282c34"
        fg_color = "#61dafb"
        entry_bg = "#ffffff"
        select_bg = "#21a1f1"
        delete_bg = "#e06c75"

        self.title_font = font.Font(family="Helvetica", size=20, weight="bold")
        self.button_font = font.Font(family="Helvetica", size=12, weight="bold")
        self.list_font = font.Font(family="Helvetica", size=12)

        # Title
        tk.Label(self.root, text="Your To-Do List", font=self.title_font,
                 bg=bg_color, fg=fg_color).pack(pady=(15, 5))

        # Entry + Add Button
        entry_frame = tk.Frame(self.root, bg=bg_color)
        entry_frame.pack(pady=10)

        self.task_entry = tk.Entry(entry_frame, width=30, font=self.list_font, bg=entry_bg)
        self.task_entry.grid(row=0, column=0, padx=(0, 10), ipady=6)

        self.add_btn = tk.Button(entry_frame, text="Add Task", font=self.button_font,
                                 bg=fg_color, fg=bg_color, width=12,
                                 activebackground=select_bg, activeforeground="white",
                                 command=self.add_task)
        self.add_btn.grid(row=0, column=1)

        # Listbox + Scrollbar
        list_frame = tk.Frame(self.root)
        list_frame.pack(pady=10)

        self.scrollbar = tk.Scrollbar(list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(list_frame, font=self.list_font, width=45, height=12,
                                  yscrollcommand=self.scrollbar.set,
                                  bg="#20232a", fg=fg_color,
                                  selectbackground=select_bg, selectforeground="white",
                                  relief=tk.FLAT, bd=0)
        self.listbox.pack()
        self.scrollbar.config(command=self.listbox.yview)

        # Delete Button
        self.del_btn = tk.Button(self.root, text="Delete Selected Task", font=self.button_font,
                                 width=20, bg=delete_bg, fg="white",
                                 activebackground="#be5046", activeforeground="white",
                                 command=self.delete_task)
        self.del_btn.pack(pady=15)

    def add_task(self):
        task = self.task_entry.get().strip()
        if not task:
            messagebox.showwarning("Warning", "You must enter a task.")
            return
        self.tasks.append(task)
        self.update_listbox()
        self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a task to delete.")
            return
        index = selected[0]
        self.tasks.pop(index)
        self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

if _name_ == "_main_":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
