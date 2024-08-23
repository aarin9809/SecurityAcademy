import pandas as pd
import hashlib


def hash_key_with_salt(key, salt):
    return hashlib.sha256((key + salt).encode()).hexdigest()


print(hash_key_with_salt)