import mysql.connector
from mysql.connector import errorcode 

# Database connection configuration
config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try: 
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    #1: query and display Studio records
    print("\n-- DISPLAYING Studio RECORDS --")
    cursor.execute("SELECT studio_id, studio_name FROM Studio")
    for studio_id, studio_name in cursor.fetchall():
        print(f"Studio ID: {studio_id}")
        print(f"Studio Name: {studio_name}\n")

    #2: query and display Genre records
    print("\n-- DISPLAYING Genre RECORDS --")
    cursor.execute("SELECT genre_id, genre_name FROM Genre")
    for genre_id, genre_name in cursor.fetchall():
        print(f"Genre ID: {genre_id}")
        print(f"Genre Name: {genre_name}\n")

    #3: query and display short Film records (runtime < 120)
    print("\n-- DISPLAYING Short Film RECORDS --")
    cursor.execute("SELECT film_name, film_runtime FROM Film WHERE film_runtime < 120") # adding filter for short films only
    for film_name, film_runtime in cursor.fetchall():
        print(f"Film Name: {film_name}")
        print(f"Runtime: {film_runtime}\n")

   #4: query and display Director records
    print("\n-- DISPLAYING Director RECORDS in Order --")
    cursor.execute("""
        SELECT film_name, film_director 
        FROM Film
        ORDER BY film_name
        """)
    for film_name, film_director in cursor.fetchall():
        print(f"Film Name: {film_name}")
        print(f"Director: {film_director}\n")   


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)

finally:
    if 'db' in locals() and db.is_connected():
        db.close()
