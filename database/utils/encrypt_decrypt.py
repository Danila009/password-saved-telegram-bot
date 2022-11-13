import os
from cryptography.fernet import Fernet

KEY = os.environ.get('ENCRYPT_DECRYPT_KEY').encode()


def encrypt(message: bytes, key: bytes = KEY) -> bytes:
    return Fernet(key).encrypt(message)


def decrypt(token: str, key: bytes = KEY) -> bytes:
    return Fernet(key).decrypt(token.encode())
