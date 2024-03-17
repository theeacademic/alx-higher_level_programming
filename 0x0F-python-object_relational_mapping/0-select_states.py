#!/usr/bin/python3
import MySQLdb
import sys

def list_states(username, password, database):
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

        # Create a cursor object
        cursor = db.cursor()

        # Execute the SQL query
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all the rows
        states = cursor.fetchall()

        # Display the results
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
    finally:
        # Close the database connection
        if db:
            db.close()

if __name__ == "__main__":
    # Check if 3 arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the function to list states
    list_states(username, password, database)

