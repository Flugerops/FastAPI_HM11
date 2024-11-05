from hashlib import sha256


def hash_pwd(pwd: str) -> str:
    password_bytes = pwd.encode("utf-8")
    hash_object = sha256(password_bytes)
    return hash_object.hexdigest()
