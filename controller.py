import tkinter as tk
from tkinter import messagebox, ttk
from model import HotelDatabase
from view import setup_styles

class HotelApp:
    def __init__(self, root):
        self.db = HotelDatabase()
        self.root = root
        self.root.title("Hotel Reservation System")
        self.root.geometry("1200x800")
        self.root.configure(bg="black")

        setup_styles()

        title = tk.Label(root, text="Hotel Reservation System", font=("Arial", 36, "bold"), fg="white", bg="black")
        title.pack(pady=40)

        self.buttons_frame = tk.Frame(root, bg="black")
        self.buttons_frame.pack(pady=20)

        left_frame = tk.Frame(self.buttons_frame, bg="black")
        center_frame = tk.Frame(self.buttons_frame, bg="black")
        right_frame = tk.Frame(self.buttons_frame, bg="black")

        left_frame.grid(row=0, column=0, padx=50)
        center_frame.grid(row=0, column=1, padx=50)
        right_frame.grid(row=0, column=2, padx=50)

        self.create_button(left_frame, "View Reservations", self.view_reservations, "View.TButton")
        self.create_button(left_frame, "Add Reservation", self.add_reservation, "Add.TButton")
        self.create_button(left_frame, "Delete Reservation", self.delete_reservation, "Delete.TButton")

        self.create_button(center_frame, "View Guests", self.view_guests, "View.TButton")
        self.create_button(center_frame, "Add Guest", self.add_guest, "Add.TButton")
        self.create_button(center_frame, "Delete Guest", self.delete_guest, "Delete.TButton")

        self.create_button(right_frame, "View Rooms", self.view_rooms, "View.TButton")
        self.create_button(right_frame, "Add Room", self.add_room, "Add.TButton")
        self.create_button(right_frame, "Delete Room", self.delete_room, "Delete.TButton")

        exit_frame = tk.Frame(root, bg="black")
        exit_frame.pack(pady=50)
        self.create_button(exit_frame, "Exit", root.quit, "Exit.TButton")

    def create_button(self, parent, text, command, style):
        btn = ttk.Button(parent, text=text, style=style, command=command)
        btn.pack(pady=20, ipadx=80, ipady=30)

    # 👇 All your original methods go here — unchanged
    # e.g., view_rooms, add_room, delete_room, view_guests, etc.

    def view_rooms(self):
        win = tk.Toplevel()
        win.title("Available Rooms")
        win.geometry("800x400")

        tree = ttk.Treeview(win, columns=("Room ID", "Number", "Type", "Price"), show="headings")
        for col in ("Room ID", "Number", "Type", "Price"):
            tree.heading(col, text=col)
        tree.pack(fill="both", expand=True)

        for room in self.db.get_all_rooms():
            tree.insert("", "end", values=room)

    def add_room(self):
        def submit():
            try:
                self.db.add_room(int(entry_id.get()), entry_number.get(), entry_type.get(), float(entry_price.get()))
                messagebox.showinfo("Success", "Room added!")
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        win = tk.Toplevel()
        win.title("Add Room")
        win.geometry("300x300")

        tk.Label(win, text="Room ID").pack()
        entry_id = tk.Entry(win)
        entry_id.pack()

        tk.Label(win, text="Number").pack()
        entry_number = tk.Entry(win)
        entry_number.pack()

        tk.Label(win, text="Type").pack()
        entry_type = tk.Entry(win)
        entry_type.pack()

        tk.Label(win, text="Price").pack()
        entry_price = tk.Entry(win)
        entry_price.pack()

        tk.Button(win, text="Add", command=submit).pack(pady=10)

    def delete_room(self):
        def submit():
            try:
                self.db.delete_room(int(entry_id.get()))
                messagebox.showinfo("Deleted", "Room deleted!")
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        win = tk.Toplevel()
        win.title("Delete Room")
        win.geometry("300x150")

        tk.Label(win, text="Room ID to Delete").pack()
        entry_id = tk.Entry(win)
        entry_id.pack()

        tk.Button(win, text="Delete", command=submit).pack(pady=10)

    def view_guests(self):
        win = tk.Toplevel()
        win.title("Guests")
        win.geometry("800x400")

        tree = ttk.Treeview(win, columns=("Guest ID", "Full Name", "Email", "Phone"), show="headings")
        for col in ("Guest ID", "Full Name", "Email", "Phone"):
            tree.heading(col, text=col)
        tree.pack(fill="both", expand=True)

        for guest in self.db.get_all_guests():
            tree.insert("", "end", values=guest)

    def add_guest(self):
        def submit():
            try:
                self.db.add_guest(entry_name.get(), entry_email.get(), entry_phone.get())
                messagebox.showinfo("Success", "Guest added!")
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        win = tk.Toplevel()
        win.title("Add Guest")
        win.geometry("300x250")

        tk.Label(win, text="Full Name").pack()
        entry_name = tk.Entry(win)
        entry_name.pack()

        tk.Label(win, text="Email").pack()
        entry_email = tk.Entry(win)
        entry_email.pack()

        tk.Label(win, text="Phone").pack()
        entry_phone = tk.Entry(win)
        entry_phone.pack()

        tk.Button(win, text="Add", command=submit).pack(pady=10)

    def delete_guest(self):
        def submit():
            try:
                self.db.delete_guest(int(entry_id.get()))
                messagebox.showinfo("Deleted", "Guest deleted!")
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        win = tk.Toplevel()
        win.title("Delete Guest")
        win.geometry("300x150")

        tk.Label(win, text="Guest ID to Delete").pack()
        entry_id = tk.Entry(win)
        entry_id.pack()

        tk.Button(win, text="Delete", command=submit).pack(pady=10)

    def view_reservations(self):
        win = tk.Toplevel()
        win.title("Reservations")
        win.geometry("850x400")

        tree = ttk.Treeview(win, columns=("ID", "Guest ID", "Room ID", "Check-in", "Check-out"), show="headings")
        for col in ("ID", "Guest ID", "Room ID", "Check-in", "Check-out"):
            tree.heading(col, text=col)
        tree.pack(fill="both", expand=True)

        for res in self.db.get_all_reservations():
            tree.insert("", "end", values=res)

    def add_reservation(self):
        def submit():
            try:
                self.db.add_reservation(int(entry_guest_id.get()), int(entry_room_id.get()), entry_checkin.get(), entry_checkout.get())
                messagebox.showinfo("Success", "Reservation added!")
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        win = tk.Toplevel()
        win.title("Add Reservation")
        win.geometry("300x300")

        tk.Label(win, text="Guest ID").pack()
        entry_guest_id = tk.Entry(win)
        entry_guest_id.pack()

        tk.Label(win, text="Room ID").pack()
        entry_room_id = tk.Entry(win)
        entry_room_id.pack()

        tk.Label(win, text="Check-in Date (YYYY-MM-DD)").pack()
        entry_checkin = tk.Entry(win)
        entry_checkin.pack()

        tk.Label(win, text="Check-out Date (YYYY-MM-DD)").pack()
        entry_checkout = tk.Entry(win)
        entry_checkout.pack()

        tk.Button(win, text="Add", command=submit).pack(pady=10)

    def delete_reservation(self):
        def submit():
            try:
                self.db.delete_reservation(int(entry_id.get()))
                messagebox.showinfo("Deleted", "Reservation deleted!")
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        win = tk.Toplevel()
        win.title("Delete Reservation")
        win.geometry("300x150")

        tk.Label(win, text="Reservation ID to Delete").pack()
        entry_id = tk.Entry(win)
        entry_id.pack()

        tk.Button(win, text="Delete", command=submit).pack(pady=10)
