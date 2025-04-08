class GuestDAO:
    def __init__(self):
        self.conn = get_db_connection()

    def create_guest(self, full_name, email, phone):
        query = "INSERT INTO Guests (full_name, email, phone) VALUES (?, ?, ?)"
        cur = self.conn.cursor()
        cur.execute(query, (full_name, email, phone))
        self.conn.commit()

    def read_guest(self, guest_id):
        query = "SELECT * FROM Guests WHERE guest_id = ?"
        cur = self.conn.cursor()
        cur.execute(query, (guest_id,))
        return cur.fetchone()

    def update_guest(self, guest_id, full_name, email, phone):
        query = "UPDATE Guests SET full_name = ?, email = ?, phone = ? WHERE guest_id = ?"
        cur = self.conn.cursor()
        cur.execute(query, (full_name, email, phone, guest_id))
        self.conn.commit()

    def delete_guest(self, guest_id):
        query = "DELETE FROM Guests WHERE guest_id = ?"
        cur = self.conn.cursor()
        cur.execute(query, (guest_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()
