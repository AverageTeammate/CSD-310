# Jacob Cannamela, Scott Hackett, Cindy Hernandez, Colton Kohler
# 12/15/2024
# Module 11.1

# *Equipment Availability Report*
# Description: This report will provide the current status of the equipment, including its condition and availability. This is important for ensuring that all trips are well-equipped and any shortages or damaged equipment can be addressed proactively.

import mysql.connector

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
