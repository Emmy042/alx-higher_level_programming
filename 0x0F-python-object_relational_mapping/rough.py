#!/usr/bin/python3

import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="alx_workflow",
    passwd="Alx_2025",
    db="hbtn_0c_0"
)

cursor = db.cursor()

# Create table if it doesn't exist
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS anonymous (
#     id INT PRIMARY KEY AUTO_INCREMENT,
#     title VARCHAR(256) NOT NULL
# )
# """)

# titles = ('chief', 'chairman', 'MD', 'GENERAL')

# for t in titles:
#     cursor.execute("INSERT INTO anonymous(title) VALUES (%s)", (t,))
#     print(f"Auto Increment ID: {cursor.lastrowid}")

# Commit changes and close

numrows = cursor.execute("SELECT * FROM anonymous")
print ("Selected %s rows" % numrows  )    
print ("Selected %s rows" % cursor.rowcount)

db.commit()
cursor.close()
db.close()

