# Jacob Cannamela, Scott Hackett, Cindy Hernandez, Colton Kohler
# 12/15/2024
# Module 11.1

# *Marketing Campaign Effectiveness Report*
#Description: This will analyze the marketing data for each trip, focusing on the booking trends, financial efficiency, and market trends. This helps the marketing team identify which trips are generating the most interest and which destinations require more targeted promotional efforts..

import mysql.connector

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
