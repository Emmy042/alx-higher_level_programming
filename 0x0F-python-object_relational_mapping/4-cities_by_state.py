#!/usr/bin/python3


import MySQLdb

if __name__ == "__main__":
    
    db = MySQLdb.connect(
    host="localhost",
    user="alx_workflow",
    passwd="Alx_2025",
    db="hbtn_0e_4_usa"
    )

    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM cities")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
