#!/usr/bin/python3


import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="alx_workflow",
    passwd="Alx_2025",
    db="hbtn_0e_0_usa"
)

cursor = db.cursor()
cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ")

rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
db.close()
