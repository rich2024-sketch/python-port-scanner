import socket


def scan_ports(user_ip, port_start, port_end):
    open_ports = []

    for port in range(port_start, port_end + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((user_ip, port))
        sock.close()

        if result == 0:
            open_ports.append(port)

    return open_ports


def get_service_name(port):
    try:
        return socket.getservbyport(port, "tcp")
    except OSError:
        return "Unknown"


def main():
    user_ip = input("Enter your IP address: ")
    port_start = 130
    port_end = 150

    open_ports = scan_ports(user_ip, port_start, port_end)

    if not open_ports:
        print("No open ports were found.")
        return

    for port in open_ports:
        service_name = get_service_name(port)
        print(f"Port {port} is open and running {service_name}")


if __name__ == "__main__":
    main()