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

if len(sys.argv) != 5:
    print("Usage: ./script.py <username> <password> <database_name> <state_name>")
    sys.exit(1)

search = sys.argv[4]

db = MySQLdb.connect(
    host="localhost",
    user="alx_workflow",
    passwd="Alx_2025",
    db="hbtn_0e_0_usa"
)

cursor = db.cursor()
cursor.execute("SELECT * FROM states WHERE name = %s", (search,))

rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
db.close()
