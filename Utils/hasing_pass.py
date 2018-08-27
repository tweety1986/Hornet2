import hashlib


hash_object = hashlib.md5(b'123')
print(hash_object.hexdigest())