from flask import Flask
from flask_mysqldb import MySQL

def populate(mysql):
    #Create a table with 5 users. 2 admin and 3 normal users
    cur = mysql.connection.cursor()
    cur.execute('''CREATE TABLE Users (uid INTEGER, role INTEGER)''')
    cur.execute('''INSERT INTO Users VALUES (1, 1)''')
    cur.execute('''INSERT INTO Users VALUES (2, 1)''')
    cur.execute('''INSERT INTO Users VALUES (3, 0)''')
    cur.execute('''INSERT INTO Users VALUES (4, 0)''')
    cur.execute('''INSERT INTO Users VALUES (5, 0)''')
    mysql.connection.commit()