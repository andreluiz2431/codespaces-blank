import socket

def create_udp_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def bind_socket_to_address(socket, address):
    socket.bind(address)

def listen_for_incoming_data(socket):
    print("UDP Server listening on port 8080...")
    while True:
        yield socket.recvfrom(1024)

def handle_incoming_data(data, address):
    print(f"Received data from {address}")
    response = "HTTP/1.1 200 OK\nContent-Type: text/plain\n\nGET request received"
    return response.encode(), address

def send_response(socket, data, address):
    socket.sendto(data, address)

def udp_server():
    server_socket = create_udp_socket()
    bind_socket_to_address(server_socket, ('0.0.0.0', 8080))
    for data, address in listen_for_incoming_data(server_socket):
        response, address = handle_incoming_data(data, address)
        send_response(server_socket, response, address)
    server_socket.close()

if __name__ == "__main__":
    udp_server()
