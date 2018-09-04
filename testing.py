import sqlite3
import hashlib


with sqlite3.connect("static/user.db") as db:
    cursor = db.cursor()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

def hash_passwd(hashed_password):
    hash_pass = hashlib.sha3_512(hashed_password.encode()).hexdigest()
    return hash_pass

def check_password(hashed_password, user_password):
    return hashed_password == hashlib.sha3_512(user_password.encode()).hexdigest()

hash_object = hashlib.md5(b'123')


print(hash_object.hexdigest())
print(check_password('48c8947f69c054a5caa934674ce8881d02bb18fb59d5a63eeaddff735b0e9801e87294783281ae49fc8287a0fd86779b27d7972d3e84f0fa0d826d7cb67dfefc','123'))
print(hash_passwd('g11w85lol2Z!'))