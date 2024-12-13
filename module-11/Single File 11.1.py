# Jacob Cannamela, Scott Hackett, Cindy Hernandez, Colton Kohler
# 12/15/2024
# Module 11.1

# All reports in a single file

import mysql.connector

# Function for Trip Booking Status Report
def trip_booking_report():
    db_connection = mysql.connector.connect(
        host="localhost",
        user="mytestuser",
        password="mytestuser",
        database="OutlandAdventuresDB"
    )
    query = """
    SELECT t.Destination, b.BookingDate, b.PaymentStatus, c.Name AS CustomerName
    FROM Bookings b
    JOIN Trips t ON b.TripID = t.TripID
    JOIN Customers c ON b.CustomerID = c.CustomerID
    ORDER BY t.Destination, b.BookingDate;
    """
    cursor = db_connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(f"Destination: {row[0]}, Booking Date: {row[1]}, Payment Status: {row[2]}, Customer Name: {row[3]}")

    cursor.close()
    db_connection.close()

# Function for Equipment Availability Report
def equipment_availability_report():
    db_connection = mysql.connector.connect(
        host="localhost",
        user="mytestuser",
        password="mytestuser",
        database="OutlandAdventuresDB"
    )
    query = """
    SELECT e.Category, e.Description, e.ItemCondition, e.Availability
    FROM Equipment e
    ORDER BY e.Category;
    """
    cursor = db_connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(f"Category: {row[0]}, Description: {row[1]}, Item Condition: {row[2]}, Availability: {row[3]}")

    cursor.close()
    db_connection.close()

# Function for Marketing Campaign Effectiveness Report
def marketing_campaign_report():
    db_connection = mysql.connector.connect(
        host="localhost",
        user="mytestuser",
        password="mytestuser",
        database="OutlandAdventuresDB"
    )
    query = """
    SELECT m.Destination, m.BookingTrends, m.FinancialEfficiency, m.MarketTrends
    FROM Marketing m
    ORDER BY m.Destination;
    """
    cursor = db_connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(f"Destination: {row[0]}, Booking Trends: {row[1]}, Financial Efficiency: {row[2]}, Market Trends: {row[3]}")

    cursor.close()
    db_connection.close()

# Run each report
if __name__ == "__main__":
    print("Trip Booking Status Report:")
    trip_booking_report()
    print("\nEquipment Availability Report:")
    equipment_availability_report()
    print("\nMarketing Campaign Effectiveness Report:")
    marketing_campaign_report()
