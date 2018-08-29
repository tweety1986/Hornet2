import sqlite3

with sqlite3.connect("static/user.db") as db:
    cursor = db.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    username TEXT PRIMARY KEY NOT NULL,
    password TEXT NOT NULL)
''')
cursor.execute('''
                    CREATE TABLE IF NOT EXISTS dzieci(
                    pesel INT NOT NULL,
                    name TEXT NOT NULL,
                    surname TEXT NOT NULL,
                    birth TEXT NOT NULL ,
                    grupa TEXT NOT NULL)
                ''')
cursor.execute("""
               INSERT INTO Users (username,password)
               VALUES("haxman","202cb962ac59075b964b07152d234b70")
               """)
db.commit()

cursor.execute("SELECT * FROM dzieci")
print(cursor.fetchall())

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())