import hashlib


hash_object = hashlib.md5(b'admin')
print(hash_object.hexdigest())