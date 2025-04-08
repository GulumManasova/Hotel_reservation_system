import sqlite3

def run_report(query):
    connection = sqlite3.connect("hoteldatabase.sqlite")
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    connection.close()

# Reports
report1 = """
SELECT COUNT(*) AS total_guests
FROM Guests;
"""

report2 = """
SELECT room_number, room_type, price
FROM Rooms
WHERE is_available = 1;
"""

report3 = """
SELECT Rooms.room_number, Rooms.room_type, Rooms.price, COUNT(Reservations.room_id) AS reservation_count
FROM Rooms
LEFT JOIN Reservations ON Rooms.room_id = Reservations.room_id
WHERE Rooms.is_available = 1
GROUP BY Rooms.room_number, Rooms.room_type, Rooms.price;
"""

report4 = """
SELECT strftime('%Y-%m', check_in_date) AS month, COUNT(reservation_id) AS reservation_count
FROM Reservations
GROUP BY month
ORDER BY month;
"""





report5 = """
SELECT Reservations.room_id, 
       SUM(Rooms.price * (julianday(Reservations.check_out_date) - julianday(Reservations.check_in_date))) AS total_revenue
FROM Reservations
JOIN Rooms ON Reservations.room_id = Rooms.room_number
GROUP BY Reservations.room_id;
"""

# Execute and print the reports
print("Report 1: Total number of guests")
run_report(report1)
print("\nReport 2: Available rooms")
run_report(report2)
print("\nReport 3: Available Rooms and Reservation Counts")
run_report(report3)
print("\nReport 4: Reservation Counts by Month")
run_report(report4)

print("\nReport 5: Total revenue from bookings")
run_report(report5)
