import mysql.connector

# Function to connect to the database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",  
            user="mytestuser",       
            password="mytestuser",  
            database="OutlandAdventuresDB"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Function to display data from a table
def display_table_data(cursor, table_name):
    try:
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        print(f"\nTable: {table_name}")
        print("-" * 40)
        if rows:
            for row in rows:
                print(row)
        else:
            print("No data found.")
    except mysql.connector.Error as err:
        print(f"Error retrieving data from {table_name}: {err}")

# Main function
def main():
    connection = connect_to_database()
    if connection is None:
        print("Failed to connect to the database. Exiting...")
        return

    cursor = connection.cursor()
    tables = [
        "Trips", "Guides", "TripGuides", "Customers", "Bookings",
        "Equipment", "Inventory", "Marketing", "Administration", "EcommerceSite"
    ]

    for table in tables:
        display_table_data(cursor, table)

    # Close the database connection
    cursor.close()
    connection.close()
    print("\nDatabase connection closed.")

if __name__ == "__main__":
    main()
