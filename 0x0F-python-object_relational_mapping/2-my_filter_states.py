#!/usr/bin/python3
"""
Script that takes 4 arguments:
  - mysql username
  - mysql password
  - database name
  - state name to search for

Displays all values in the `states` table where name matches the argument.
Uses MySQLdb and connects to localhost:3306.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments
    username, password, dbname, state_name = sys.argv[1:5]

    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="alx_workflow",
        passwd="Alx_2025",
        db="hbtn_0e_0_usa"
    )

    cursor = db.cursor()

    # ⚠️ Using `.format()` as required (though not safe for production)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    # Fetch and print rows
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
