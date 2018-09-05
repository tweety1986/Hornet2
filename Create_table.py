import sqlite3

with sqlite3.connect("static/user.db") as db:
    cursor = db.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    grupa TEXT NOT NULL,
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
               INSERT INTO Users (grupa, username, password, email)
               VALUES(
               "admin",
               "admin", 
               "4626093d4bc650544f61f471d24f9e17232205882e5e8d5ed3968623713e2dcc8d2aa6dd0d33240c79ca37e41e6904401f753da49ba9a2a08ef7d508fcbd5361",
               "gwolyniec25@gmail.com");
               ''')
db.commit()

#cursor.execute("SELECT * FROM dzieci")
#print(cursor.fetchall())

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())