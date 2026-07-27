import socket

user_ip = input("Enter your IP address:")
PORT_START = 1
PORT_END = 1024

for port in range(PORT_START, PORT_END + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((user_ip, port))
    if result == 0:
        print(f"port {port} is open")
    sock.close()
    