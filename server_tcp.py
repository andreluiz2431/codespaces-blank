import socket

def create_tcp_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def bind_socket_to_address(socket, address):
    socket.bind(address)

def listen_for_incoming_data(socket):
    socket.listen(50)
    print("TCP Server listening on port 8080...")

def handle_client_connection(client_socket):
    print("Handling client connection.")
    data = client_socket.recv(1024)  # Receive data from client
    response = "HTTP/1.1 200 OK\nContent-Type: text/plain\n\nGET request received"
    client_socket.send(response.encode())  # Send response to client
    client_socket.close()  # Close client connection

def accept_connections(server_socket):
    while True:
        client_socket, address = server_socket.accept()  # Accept new connection
        print(f"Connection from {address} established.")
        handle_client_connection(client_socket)  # Handle client in separate function

def tcp_server():
    server_socket = create_tcp_socket()
    bind_socket_to_address(server_socket, ('0.0.0.0', 8080))  # Bind to all interfaces on port 8080
    listen_for_incoming_data(server_socket)
    accept_connections(server_socket)  # Handle incoming connections

if __name__ == "__main__":
    tcp_server()
