import sqlite3,time

def login():
    while True:
        username = input("LOGIN: ")
        password = input("PASSWORD")
        with sqlite3.connect("logowanie.db") as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM user WHERE username = ? AND password = ?")
        cursor.execute(find_user,[(username),(password)])
        result = cursor.fetchall()

        if result:
            for i in result:
                print("Welcome" + i[2])
            return("exit")

        else:
            print("Username or Paswword invalid")
            again = input("Again ?")
            if again.lower() == "n":
                print("Godbye")
                time.sleep(1)
                return("exit")

login()