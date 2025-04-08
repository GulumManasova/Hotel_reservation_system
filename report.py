import sqlite3


# Function to connect to the database
def connect_to_db(db_name):
    try:
        conn = sqlite3.connect(db_name)  # Use 'hoteldatabase.sqlite' for your database file
        print("Successfully connected to the database.")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None


# Function to execute SELECT query and print results
def execute_select_query(cursor, query, params=()):
    try:
        cursor.execute(query, params)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except sqlite3.Error as e:
        print(f"Error executing query: {e}")


# Main script
def main():
    # Connect to the database
    conn = connect_to_db('hoteldatabase.sqlite')  # Connecting to 'hoteldatabase.sqlite'

    if conn is None:
        return  # Exit if connection failed

    cursor = conn.cursor()

    # Example 1: Get all available rooms
    print("Available rooms:")
    query = "SELECT * FROM Rooms WHERE is_available = 1"
    execute_select_query(cursor, query)

    # Example 2: Get all reservations for a particular guest
    print("\nReservations for guest_id 1:")
    query = "SELECT * FROM Reservations WHERE guest_id = ?"
    guest_id = 1
    execute_select_query(cursor, query, (guest_id,))

    # Example 3: Get total number of guests
    print("\nTotal number of guests:")
    query = "SELECT COUNT(*) FROM Guests"
    execute_select_query(cursor, query)

    # Example 4: Get rooms with price between 40 and 100
    print("\nRooms with price between 40 and 100:")
    query = "SELECT * FROM Rooms WHERE price BETWEEN ? AND ?"
    min_price = 40.0
    max_price = 100.0
    execute_select_query(cursor, query, (min_price, max_price))

    # Example 5: Get reservations count per month
    print("\nReservation counts by month:")
    query = "SELECT strftime('%Y-%m', check_in_date) AS month, COUNT(*) FROM Reservations GROUP BY month"
    execute_select_query(cursor, query)

    # Example 6: Get rooms and their booking counts
    print("\nRooms and their booking counts:")
    query = """
    SELECT Rooms.room_number, Rooms.room_type, Rooms.price, 
           COUNT(Reservations.room_id) AS booking_count
    FROM Rooms
    LEFT JOIN Reservations ON Rooms.room_id = Reservations.room_id
    GROUP BY Rooms.room_number
    """
    execute_select_query(cursor, query)

    # Close the connection
    conn.close()


# Run the main function
if __name__ == "__main__":
    main()
