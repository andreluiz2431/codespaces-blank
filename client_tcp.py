import socket
import time

def create_tcp_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect_to_server(client_socket, address, port):
    client_socket.connect((address, port))

def send_request(client_socket, request):
    client_socket.send(request.encode())

def receive_response(client_socket, buffer_size=4096):
    return client_socket.recv(buffer_size).decode()

def tcp_client():
    time.sleep(15)  # Atraso de 15 segundos para garantir que o servidor esteja pronto
    client_socket = create_tcp_socket()
    try:
        connect_to_server(client_socket, 'server_tcp', 8080)  # Nome do container
        request = "GET / HTTP/1.1\nHost: localhost\n\n"
        send_request(client_socket, request)
        response = receive_response(client_socket)
        print("Response from server:", response)
    finally:
        client_socket.close()

if __name__ == "__main__":
    tcp_client()