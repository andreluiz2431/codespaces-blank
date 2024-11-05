import socket
import time

def tcp_server():
    time.sleep(10)  # Atraso para garantir que o servidor esteja pronto
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8080))
    server_socket.listen(50)  # Aumentar para permitir mais conexões pendentes
    print("TCP Server listening on port 8080...")
    
    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from {address} established.")
        data = client_socket.recv(1024)
        response = "HTTP/1.1 200 OK\nContent-Type: text/plain\n\nGET request received"
        client_socket.send(response.encode())
        client_socket.close()

if __name__ == "__main__":
    tcp_server()
