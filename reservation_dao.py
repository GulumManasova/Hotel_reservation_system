class ReservationDAO:
    def __init__(self):
        self.conn = get_db_connection()

    def create_reservation(self, guest_id, room_id, check_in_date, check_out_date):
        query = "INSERT INTO Reservations (guest_id, room_id, check_in_date, check_out_date) VALUES (?, ?, ?, ?)"
        cur = self.conn.cursor()
        cur.execute(query, (guest_id, room_id, check_in_date, check_out_date))
        self.conn.commit()

    def read_reservation(self, reservation_id):
        query = "SELECT * FROM Reservations WHERE reservation_id = ?"
        cur = self.conn.cursor()
        cur.execute(query, (reservation_id,))
        return cur.fetchone()

    def update_reservation(self, reservation_id, guest_id, room_id, check_in_date, check_out_date):
        query = "UPDATE Reservations SET guest_id = ?, room_id = ?, check_in_date = ?, check_out_date = ? WHERE reservation_id = ?"
        cur = self.conn.cursor()
        cur.execute(query, (guest_id, room_id, check_in_date, check_out_date, reservation_id))
        self.conn.commit()

    def delete_reservation(self, reservation_id):
        query = "DELETE FROM Reservations WHERE reservation_id = ?"
        cur = self.conn.cursor()
        cur.execute(query, (reservation_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()
