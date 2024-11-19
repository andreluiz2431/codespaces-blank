import socket
import time

def create_udp_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_request(client_socket, request, address):
    client_socket.sendto(request.encode(), address)

def receive_response(client_socket):
    response, _ = client_socket.recvfrom(4096)
    return response.decode()

def udp_client():
    time.sleep(15)  # Atraso de 15 segundos para garantir que o servidor esteja pronto
    client_socket = create_udp_socket()
    request = "GET / HTTP/1.1\nHost: localhost\n\n"
    send_request(client_socket, request, ('server_udp', 8080))
    response = receive_response(client_socket)
    print("Response from server:", response)
    client_socket.close()

if __name__ == "__main__":
    udp_client()
