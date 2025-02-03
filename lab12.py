import socket

# Define the server's host and port
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # The same port as the server

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server
    s.connect((HOST, PORT))
    
    # Send data to the server
    message = "Hello, Server!"
    s.sendall(message.encode())
    
    # Receive data from the server
    data = s.recv(1024)
    
    print(f"Received from server: {data.decode()}")
