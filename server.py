import socket
import threading

HOST = 'localhost'
PORT = 8080
LISTEN_COUNT = 5
ENCODING = "utf-8"


def handle_request(client_socket: socket.socket):
    try:
        data = client_socket.recv(1024)
        method = data.decode(ENCODING).split()[0]
        if method in ['GET', 'HEAD']:
            response = "Hi from server"
            client_socket.sendall(response.encode(ENCODING))
    except socket.error as e:
        print(e)
    finally:
        client_socket.close()


def start_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(LISTEN_COUNT)

    while True:
        client_socket, addr = sock.accept()
        print('Connected:', addr)
        client_handler = threading.Thread(target=handle_request, args=(client_socket,))
        client_handler.start()


if __name__ == "__main__":
    start_server()
