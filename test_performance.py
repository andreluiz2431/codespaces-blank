import time
import socket

def test_tcp_performance():
    server_address = 'server_tcp'  # Nome do serviço no Docker Compose
    start_time = time.time()
    
    for _ in range(10000):
        try:
            # Criar um socket e conectar ao servidor
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((server_address, 8080))
            request = "GET / HTTP/1.1\nHost: localhost\n\n"
            client_socket.send(request.encode())
            response = client_socket.recv(4096)
            client_socket.close()
        except Exception as e:
            print(f"Erro na conexão ou envio: {e}")
    
    end_time = time.time()
    print(f"TCP: Time taken for 10,000 requests: {end_time - start_time:.2f} seconds")

def test_udp_performance():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    start_time = time.time()
    
    for _ in range(10000):
        request = "GET / HTTP/1.1\nHost: localhost\n\n"
        client_socket.sendto(request.encode(), ('server_udp', 8080))
        response, _ = client_socket.recvfrom(4096)
    
    end_time = time.time()
    client_socket.close()
    print(f"UDP: Time taken for 10,000 requests: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    test_tcp_performance()
    test_udp_performance()