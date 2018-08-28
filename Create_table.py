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
#cursor.execute("""
#               INSERT INTO Users (username,password)
#               VALUES("admin","21232f297a57a5a743894a0e4a801fc3")
#               """)
db.commit()

cursor.execute("SELECT * FROM dzieci")
print(cursor.fetchall())

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())