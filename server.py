import socket
import threading
import os

HOST = 'localhost'
PORT=8080
DOCUMENT_ROOT = './www' #root folder for static files
def handle_request(client_socket):
    try:
        #todo
        # 1 get request
        # 2 get headers
        # 3 split headers to methods
        # 4 give back response index.html
        if method in ['GET', 'HEAD']:
            # create response and send it back
            return
     finally:
        client_socket.close()

def start_server():
    # 1. create sockets
    # 2. bind socket to address and port
    #3. in while loop create threads with function for handle_request

if __name__ == "__main__":
    starr_server()