import hashlib


hash_object = hashlib.sha3_512(b'123')

print(hash_object.hexdigest())