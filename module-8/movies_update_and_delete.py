import mysql.connector
from mysql.connector import errorcode

# Connect to the database
config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

def show_films(cursor, title):
    # method to execute the inner join query and output the results
    # iterate over the dataset and output the results to the terminal window
    # inner join query
    cursor.execute("""
        SELECT 
            film_name AS Name, 
            film_director AS Director, 
            genre_name AS Genre, 
            studio_name AS 'Studio Name'
        FROM 
            film
        INNER JOIN genre ON film.genre_id = genre.genre_id
        INNER JOIN studio ON film.studio_id = studio.studio_id
    """)
    # get the results from the cursor object
    films = cursor.fetchall()
    print("\n -- {} --".format(title))

    # iterate over the data set and display results
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

db = mysql.connector.connect(**config)
cursor = db.cursor()
show_films(cursor, "-- DISPLAYING FILMS --")

# Insert a new film record (using "Keanu" by Jordan Peele)
cursor.execute("""
        INSERT INTO film (film_name, film_director, genre_id, studio_id, film_releaseDate, film_runtime)
        VALUES ('Keanu', 'Jordan Peele', 3, 2, 2016, 100);
    """)
db.commit()

# Display all films after insertion
show_films(cursor, "-- DISPLAYING FILMS AFTER INSERTION --")

# Update the film "Alien" to be a Horror film (assuming Genre ID 1 is Horror)
cursor.execute("""
        UPDATE film
        SET genre_id = 1
        WHERE film_name = 'Alien';
    """)
db.commit()

# Display all films after updating "Alien"
show_films(cursor, "-- DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror --")

# Delete the film "Gladiator"
cursor.execute("""
        DELETE FROM film
        WHERE film_name = 'Gladiator';
    """)
db.commit()

# Display all films after deletion
show_films(cursor, "-- DISPLAYING FILMS AFTER DELETE-- ")