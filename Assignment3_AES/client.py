# client.py
import os
import socket
import sys

from aes import encrypt_cbc  # Updated to use actual AES encryption
from utils import derive_key

# Constants
SERVER_HOST = "127.0.0.1"  # Replace with server's IP address if needed
SERVER_PORT = 65432
BUFFER_SIZE = 4096
PASSWORD = "YourSecurePassword"  # Must match the server's password
SALT = b"\x1a\xb4\x10\x8c\xe2\xa1\x95\x1f\xbf\xc3\xd9\x88\x7f\xea\xfd\xe4"  # Must match the server's salt
MAX_USERNAME_LENGTH = 16  # Limit username to 16 bytes

# Derive the encryption key
KEY = derive_key(PASSWORD, SALT)


def send_message(client_socket, user_id, message):
    # Generate a unique IV for this message
    iv = os.urandom(16)

    # Enforce username length limit
    user_id_bytes = user_id.encode("utf-8")
    if len(user_id_bytes) > MAX_USERNAME_LENGTH:
        user_id_bytes = user_id_bytes[:MAX_USERNAME_LENGTH]
        user_id = user_id_bytes.decode("utf-8", errors="ignore")
        print(f"Username truncated to: {user_id}")

    # Encrypt user_id and message
    encrypted_user_id = encrypt_cbc(KEY, iv, user_id.encode("utf-8"))
    encrypted_message = encrypt_cbc(KEY, iv, message.encode("utf-8"))

    # Prepare data
    user_id_length = len(encrypted_user_id)
    data = (
        user_id_length.to_bytes(4, byteorder="big")
        + iv
        + encrypted_user_id
        + encrypted_message
    )

    # Send data length first
    data_length = len(data)
    client_socket.sendall(data_length.to_bytes(4, byteorder="big"))
    # Then send the actual data
    client_socket.sendall(data)


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <username>")
        sys.exit(1)

    username = sys.argv[1]

    # Enforce username length limit
    username_bytes = username.encode("utf-8")
    if len(username_bytes) > MAX_USERNAME_LENGTH:
        print(f"Username exceeds maximum length of {MAX_USERNAME_LENGTH} bytes.")
        username_bytes = username_bytes[:MAX_USERNAME_LENGTH]
        username = username_bytes.decode("utf-8", errors="ignore")
        print(f"Username truncated to: {username}")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((SERVER_HOST, SERVER_PORT))
        print(f"[*] Connected to {SERVER_HOST}:{SERVER_PORT} as {username}")

        while True:
            message = input("Enter message (type 'exit' to quit): ")
            if message.lower() == "exit":
                break
            send_message(client, username, message)
    except BrokenPipeError:
        print("[-] Connection error: Broken pipe.")
    except Exception as e:
        print(f"[-] Connection error: {e}")
    finally:
        client.close()
        print("[*] Disconnected from the server.")


if __name__ == "__main__":
    main()
