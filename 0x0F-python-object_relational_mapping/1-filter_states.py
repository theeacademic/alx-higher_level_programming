#!/usr/bin/python3
import MySQLdb
import sys

def main():
    # Check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=root, passwd=roott, db=my_db)
        cursor = db.cursor()

        # Execute SQL query to retrieve states starting with 'N'
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
        states = cursor.fetchall()

        # Display results
        for state in states:
            print(state)

        # Close the database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL: {}".format(e))
        sys.exit(1)

if __name__ == "__main__":
    main()

