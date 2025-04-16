import tkinter as tk
from controller import HotelApp  # Make sure controller.py is in the same folder

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelApp(root)
    root.mainloop()
