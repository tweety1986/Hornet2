import sqlite3
import hashlib
import datetime
with sqlite3.connect("static/user.db") as db:
    cursor = db.cursor()

cursor.execute("SELECT * FROM users")
#print(cursor.fetchall())

def hash_passwd(hashed_password):
    hash_pass = hashlib.sha3_512(hashed_password.encode()).hexdigest()
    return hash_pass

def check_password(hashed_password, user_password):
    return hashed_password == hashlib.sha3_512(user_password.encode()).hexdigest()

#hash_object = hashlib.md5(b'123')


#print(hash_object.hexdigest())
#print(check_password('48c8947f69c054a5caa934674ce8881d02bb18fb59d5a63eeaddff735b0e9801e87294783281ae49fc8287a0fd86779b27d7972d3e84f0fa0d826d7cb67dfefc','123'))
#print(hash_passwd(''))


#def find_child(pesel):
#    with sqlite3.connect("static/user.db") as db:
#        cursor = db.cursor()
#        pesel = int(pesel)
#        cursor.execute ('SELECT * FROM dzieci WHERE person_id = ?', (pesel,))
#        data = cursor.fetchall()
#        return data



#date_entry = '1985/11/01'
#year, month, day = map(int, date_entry.split('/'))
#date1 = str(datetime.date(year, month, day))
#date1 = int(date1)


for i in range (0,20,3):
     print(i)
