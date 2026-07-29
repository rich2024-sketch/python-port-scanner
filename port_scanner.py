import socket 

user_ip = input("Enter your IP address:") 
PORT_START = 1
PORT_END = 1024

for port in range(PORT_START, PORT_END + 1): 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a new socket object using the IPv4 address family and TCP protocol. 
    # socket.AF_INET is used for IPv4 addresses, and socket.SOCK_STREAM is used for TCP connections.

    sock.settimeout(1) # Set a timeout of 1 second for the socket connection attempt. This means that if the connection attempt to a port takes too long 
    # ( more than 1 second), it will be aborted, and the program will move on to the next port.))

    result = sock.connect_ex((user_ip, port)) # The connect_ex() method attempts to connect to the specified IP adddress and port. It returns 0 if the connection is successful (indicating that the port is open), or an error code if the connection fails (indicating that the port is closed or filtered).

    if result == 0: 
        service_tcp = socket.getservbyport(port, 'tcp') # If the port is open, this line retrieves the service name associated with that port using the getservbyport() method.
        print(f"port {port} is open and running {service_tcp}")

    sock.close() # Close the socket after checking the port to free up system resources. This is important to avoid running out of available sockets and to ensure that the program can continue scanning other ports without issues.
    