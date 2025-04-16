import sqlite3

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
