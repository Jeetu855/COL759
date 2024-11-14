# aes.py


def pad(message: bytes) -> bytes:
    """
    Pads the message to be a multiple of 16 bytes using PKCS7 padding.
    """
    padding_length = 16 - (len(message) % 16)
    padding = bytes([padding_length] * padding_length)
    return message + padding


def unpad(padded_message: bytes) -> bytes:
    """
    Removes PKCS7 padding from the message.
    """
    padding_length = padded_message[-1]
    if padding_length < 1 or padding_length > 16:
        raise ValueError("Invalid padding length.")
    return padded_message[:-padding_length]


def xor_bytes(a: bytes, b: bytes) -> bytes:
    """
    Performs XOR between two byte strings.
    """
    return bytes(x ^ y for x, y in zip(a, b))


def encrypt_cbc(key: bytes, iv: bytes, plaintext: bytes) -> bytes:
    """
    Encrypts plaintext using a simplistic XOR-based CBC mode.
    """
    plaintext = pad(plaintext)
    ciphertext = b""
    previous = iv
    for i in range(0, len(plaintext), 16):
        block = plaintext[i : i + 16]
        block = xor_bytes(block, previous)
        # Simple encryption: XOR with key (not actual AES)
        encrypted_block = xor_bytes(block, key[:16])  # Simplistic and insecure
        ciphertext += encrypted_block
        previous = encrypted_block
    return ciphertext


def decrypt_cbc(key: bytes, iv: bytes, ciphertext: bytes) -> bytes:
    """
    Decrypts ciphertext using a simplistic XOR-based CBC mode.
    """
    if len(ciphertext) % 16 != 0:
        raise ValueError("Ciphertext length must be a multiple of 16 bytes.")

    plaintext = b""
    previous = iv
    for i in range(0, len(ciphertext), 16):
        block = ciphertext[i : i + 16]
        # Simple decryption: XOR with key (not actual AES)
        decrypted_block = xor_bytes(block, key[:16])  # Simplistic and insecure
        decrypted_block = xor_bytes(decrypted_block, previous)
        plaintext += decrypted_block
        previous = block
    return unpad(plaintext)
