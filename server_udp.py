import socket

def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', 8080))
    print("UDP Server listening on port 8080...")
    
    while True:
        data, address = server_socket.recvfrom(1024)
        print(f"Received data from {address}")
        response = "HTTP/1.1 200 OK\nContent-Type: text/plain\n\nGET request received"
        server_socket.sendto(response.encode(), address)

if __name__ == "__main__":
    udp_server()
