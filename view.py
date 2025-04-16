from tkinter import ttk

def setup_styles():
    style = ttk.Style()
    style.theme_use('clam')

    style.configure("TButton", foreground="white", font=("Arial", 20, "bold"), padding=20)
    style.configure("View.TButton", background="#9DD8C0")
    style.map("View.TButton", background=[("active", "#e69500")])
    style.configure("Add.TButton", background="#6CB296")
    style.map("Add.TButton", background=[("active", "#3e8e41")])
    style.configure("Delete.TButton", background="#539D80")
    style.map("Delete.TButton", background=[("active", "#d32f2f")])
    style.configure("Exit.TButton", background="#3D6052")
    style.map("Exit.TButton", background=[("active", "#666666")])
