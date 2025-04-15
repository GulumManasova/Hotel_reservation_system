 # Replace with actual path or import

class RoomDAO:
    def __init__(self):
        self.conn = get_db_connection()

    def create_room(self, room_id, room_number, room_type, price, is_available="Yes"):
        query = """
            INSERT INTO Rooms (room_id, room_number, room_type, price, is_available)
            VALUES (?, ?, ?, ?, ?)
        """
        cur = self.conn.cursor()
        cur.execute(query, (room_id, room_number, room_type, price, is_available))
        self.conn.commit()

    def read_room(self, room_id):
        query = "SELECT * FROM Rooms WHERE room_id = ?"
        cur = self.conn.cursor()
        cur.execute(query, (room_id,))
        return cur.fetchone()

    def update_room(self, room_id, room_number, room_type, price, is_available):
        query = """
            UPDATE Rooms
            SET room_number = ?, room_type = ?, price = ?, is_available = ?
            WHERE room_id = ?
        """
        cur = self.conn.cursor()
        cur.execute(query, (room_number, room_type, price, is_available, room_id))
        self.conn.commit()

    def delete_room(self, room_id):
        query = "DELETE FROM Rooms WHERE room_id = ?"
        cur = self.conn.cursor()
        cur.execute(query, (room_id,))
        self.conn.commit()

    def list_all_rooms(self):
        query = "SELECT * FROM Rooms"
        cur = self.conn.cursor()
        cur.execute(query)
        return cur.fetchall()

    def close(self):
        self.conn.close()
