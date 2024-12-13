# Jacob Cannamela, Scott Hackett, Cindy Hernandez, Colton Kohler
# 12/15/2024
# Module 11.1

# *Trip Booking Status Report*
# Description: Report will help the company track the booking status of trips, including how many bookings have been made for each trip and the payment status of these bookings. It provides valuable insight into which trips are performing well and which may need marketing intervention.

import mysql.connector

# Connect to the database
db_connection = mysql.connector.connect(
    host="localhost",
    user="mytestuser",
    password="mytestuser",
    database="OutlandAdventuresDB"
)

# Define the query to fetch trip bookings and payment status
query = """
SELECT t.Destination, b.BookingDate, b.PaymentStatus, c.Name AS CustomerName
FROM Bookings b
JOIN Trips t ON b.TripID = t.TripID
JOIN Customers c ON b.CustomerID = c.CustomerID
ORDER BY t.Destination, b.BookingDate;
"""

# Create a cursor to execute the query
cursor = db_connection.cursor()

# Execute the query
cursor.execute(query)

# Fetch all results
results = cursor.fetchall()

# Display the results (trip bookings and payment status)
for row in results:
    print(f"Destination: {row[0]}, Booking Date: {row[1]}, Payment Status: {row[2]}, Customer Name: {row[3]}")

# Close the cursor and connection
cursor.close()
db_connection.close()
