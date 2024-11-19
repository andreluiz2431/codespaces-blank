import time
import socket

def create_tcp_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect_to_server(socket, address, port):
    socket.connect((address, port))

def send_tcp_request(socket, request):
    socket.send(request.encode())

def receive_tcp_response(socket):
    return socket.recv(4096)

def create_udp_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_udp_request(socket, request, address):
    socket.sendto(request.encode(), address)

def receive_udp_response(socket):
    response, _ = socket.recvfrom(4096)
    return response

def test_tcp_performance():
    server_address = 'server_tcp'  # Nome do serviço no Docker Compose
    start_time = time.time()
    
    for _ in range(10000):
        try:
            client_socket = create_tcp_socket()
            connect_to_server(client_socket, server_address, 8080)
            request = "GET / HTTP/1.1\nHost: localhost\n\n"
            send_tcp_request(client_socket, request)
            response = receive_tcp_response(client_socket)
        except Exception as e:
            print(f"Erro na conexão ou envio: {e}")
    
    end_time = time.time()
    client_socket.close()
    print(f"TCP: Time taken for 10,000 requests: {end_time - start_time:.2f} seconds")

def test_udp_performance():
    server_address = ('server_udp', 8080)
    start_time = time.time()

    for _ in range(10000):
        try:
            client_socket = create_udp_socket()
            request = "GET / HTTP/1.1\nHost: localhost\n\n"
            send_udp_request(client_socket, request, server_address)
            response = receive_udp_response(client_socket)
        except Exception as e:
            print(f"Erro na conexão ou envio: {e}")

    end_time = time.time()
    client_socket.close()
    print(f"UDP: Time taken for 10,000 requests: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    test_tcp_performance()
    test_udp_performance()