import sqlite3

with sqlite3.connect("static/user.db") as db:
    cursor = db.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL)
''')
cursor.execute('''
                    CREATE TABLE IF NOT EXISTS dzieci(
                    pesel INT NOT NULL,
                    name TEXT NOT NULL,
                    surname TEXT NOT NULL,
                    birth TEXT NOT NULL ,
                    grupa TEXT NOT NULL)
                ''')
cursor.execute('''
               INSERT INTO Users (username, password, email)
               VALUES(
               "admin", 
               "ba69f73cca23a9ac5c8b567dc185a756e97c982164fe25859e0d1dcc1475c80a615b2123af1f5f94c11e3e9402c3ac558f500199d95b6d3e301758586281dcd26",
               "gwolyniec25@gmail.com");
               ''')
db.commit()

#cursor.execute("SELECT * FROM dzieci")
#print(cursor.fetchall())

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())