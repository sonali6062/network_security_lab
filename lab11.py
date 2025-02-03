import socket

# Define the host and port
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Non-privileged port used by the server

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the specified host and port
    s.bind((HOST, PORT))
    
    # Enable the server to accept connections (max 1 client connection at a time)
    s.listen()
    print(f"Server is listening on {HOST}:{PORT}")
    
    # Accept a connection from the client
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        
        # Receive data from the client (up to 1024 bytes)
        data = conn.recv(1024)
        if data:
            print(f"Received from client: {data.decode()}")
        
        # Send a response to the client
        response = "Hello from server!"
        conn.sendall(response.encode())
