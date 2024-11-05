import socket

def udp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    request = "GET / HTTP/1.1\nHost: localhost\n\n"
    client_socket.sendto(request.encode(), ('server_udp', 8080))
    response, _ = client_socket.recvfrom(4096)
    print("Response from server:", response.decode())
    client_socket.close()

if __name__ == "__main__":
    udp_client()
