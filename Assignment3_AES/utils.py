# utils.py
import hashlib

# Constants
PASSWORD = "YourSecurePassword"  # Replace with your actual pre-shared password
SALT = b"\x1a\xb4\x10\x8c\xe2\xa1\x95\x1f\xbf\xc3\xd9\x88\x7f\xea\xfd\xe4"  # Replace with your actual 16-byte salt
ITERATIONS = 100000
KEY_LENGTH = 32  # 256 bits for AES-256


def derive_key(
    password: str, salt: bytes, iterations: int = ITERATIONS, dklen: int = KEY_LENGTH
) -> bytes:
    """
    Derives a cryptographic key from the given password and salt using PBKDF2.
    """
    key = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, iterations, dklen)
    return key
