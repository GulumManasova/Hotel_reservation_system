import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

# ---------------------- MODEL ---------------------- #
class HotelDatabase:
    def __init__(self, db_name="hoteldatabase.sqlite"):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS Rooms (
                            room_id INTEGER PRIMARY KEY,
                            room_number TEXT,
                            room_type TEXT,
                            price REAL,
                            is_available TEXT)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS Guests (
                            guest_id INTEGER PRIMARY KEY,
                            full_name TEXT,
                            email TEXT,
                            phone TEXT)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS Reservations (
                            reservation_id INTEGER PRIMARY KEY,
                            guest_id INTEGER,
                            room_id INTEGER,
                            check_in_date TEXT,
                            check_out_date TEXT,
                            FOREIGN KEY(guest_id) REFERENCES Guests(guest_id),
                            FOREIGN KEY(room_id) REFERENCES Rooms(room_id))''')
        self.conn.commit()

    def add_room(self, room_id, number, room_type, price):
        self.conn.execute("INSERT INTO Rooms (room_id, room_number, room_type, price, is_available) VALUES (?, ?, ?, ?, 'Yes')",
                          (room_id, number, room_type, price))
        self.conn.commit()

    def delete_room(self, room_id):
        self.conn.execute("DELETE FROM Rooms WHERE room_id = ?", (room_id,))
        self.conn.commit()

    def get_all_rooms(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT room_id, room_number, room_type, price FROM Rooms")
        return cursor.fetchall()

    def add_guest(self, full_name, email, phone):
        self.conn.execute("INSERT INTO Guests (full_name, email, phone) VALUES (?, ?, ?)",
                          (full_name, email, phone))
        self.conn.commit()

    def get_all_guests(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT guests_id, full_name, email, phone FROM Guests")
        return cursor.fetchall()

    def delete_guest(self, guest_id):
        self.conn.execute("DELETE FROM Guests WHERE guest_id = ?", (guest_id,))
        self.conn.commit()

    def add_reservation(self, guest_id, room_id, checkin, checkout):
        self.conn.execute("INSERT INTO Reservations (guest_id, room_id, check_in_date, check_out_date) VALUES (?, ?, ?, ?)",
                          (guest_id, room_id, checkin, checkout))
        self.conn.commit()

    def delete_reservation(self, reservation_id):
        self.conn.execute("DELETE FROM Reservations WHERE reservation_id = ?", (reservation_id,))
        self.conn.commit()

    def get_all_reservations(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT reservation_id, guest_id, room_id, check_in_date, check_out_date FROM Reservations")
        return cursor.fetchall()

# ---------------------- VIEW + CONTROLLER ---------------------- #
import tkinter as tk
from tkinter import ttk

import tkinter as tk
from tkinter import ttk

class HotelApp:
    def __init__(self, root):
        self.db = HotelDatabase()
        self.root = root
        self.root.title("Hotel Reservation System")
        self.root.geometry("1200x800")
        self.root.configure(bg="black")

        # Setup styles
        style = ttk.Style()
        style.theme_use('clam')  # 'clam' supports background color changes

        # Base button style
        style.configure("TButton",
                        foreground="white",
                        font=("Arial", 20, "bold"),
                        padding=20)

        # Custom styles with background colors
        style.configure("View.TButton", background="#9DD8C0")
        style.map("View.TButton", background=[("active", "#e69500")])

        style.configure("Add.TButton", background="#6CB296")
        style.map("Add.TButton", background=[("active", "#3e8e41")])

        style.configure("Delete.TButton", background="#539D80")
        style.map("Delete.TButton", background=[("active", "#d32f2f")])

        style.configure("Exit.TButton", background="#3D6052")
        style.map("Exit.TButton", background=[("active", "#666666")])

        # Title
        title = tk.Label(root, text="Hotel Reservation System", font=("Arial", 36, "bold"), fg="white", bg="black")
        title.pack(pady=40)

        # Button layout
        self.buttons_frame = tk.Frame(root, bg="black")
        self.buttons_frame.pack(pady=20)

        # Left
        left_frame = tk.Frame(self.buttons_frame, bg="black")
        left_frame.grid(row=0, column=0, padx=50)

        self.create_button(left_frame, "View Reservations", self.view_reservations, "View.TButton")
        self.create_button(left_frame, "Add Reservation", self.add_reservation, "Add.TButton")
        self.create_button(left_frame, "Delete Reservation", self.delete_reservation, "Delete.TButton")

        # Center
        center_frame = tk.Frame(self.buttons_frame, bg="black")
        center_frame.grid(row=0, column=1, padx=50)

        self.create_button(center_frame, "View Guests", self.view_guests, "View.TButton")
        self.create_button(center_frame, "Add Guest", self.add_guest, "Add.TButton")
        self.create_button(center_frame, "Delete Guest", self.delete_guest, "Delete.TButton")
        # Right
        right_frame = tk.Frame(self.buttons_frame, bg="black")
        right_frame.grid(row=0, column=2, padx=50)

        self.create_button(right_frame, "View Rooms", self.view_rooms, "View.TButton")
        self.create_button(right_frame, "Add Room", self.add_room, "Add.TButton")
        self.create_button(right_frame, "Delete Room", self.delete_room, "Delete.TButton")

        # Exit button
        exit_frame = tk.Frame(root, bg="black")
        exit_frame.pack(pady=50)
        self.create_button(exit_frame, "Exit", root.quit, "Exit.TButton")

    def create_button(self, parent, text, command, style):
        btn = ttk.Button(parent, text=text, style=style, command=command)
        btn.pack(pady=20, ipadx=80, ipady=30)  # 👈 makes buttons much wider & taller





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

# ---------------------- START APP ---------------------- #
if __name__ == "__main__":
    root = tk.Tk()
    app = HotelApp(root)
    root.mainloop()
