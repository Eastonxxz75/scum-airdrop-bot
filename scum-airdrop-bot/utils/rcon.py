# File: utils/rcon.py

import socket

def send_rcon_command(host, port, password, command):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((host, port))
            sock.sendall((password + "\n").encode())
            sock.sendall((command + "\n").encode())
            return True
    except Exception as e:
        print(f"RCON Error: {e}")
        return False
