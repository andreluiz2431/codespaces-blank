import socket
import time

def tcp_client():
    time.sleep(15)  # Atraso de 15 segundos para garantir que o servidor esteja pronto
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('server_tcp', 8080))  # Nome do container
    request = "GET / HTTP/1.1\nHost: localhost\n\n"
    client_socket.send(request.encode())
    response = client_socket.recv(4096)
    print("Response from server:", response.decode())
    client_socket.close()

if __name__ == "__main__":
    tcp_client()
