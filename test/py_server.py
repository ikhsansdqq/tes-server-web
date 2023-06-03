import socket
import threading

server_host = 'localhost'


def handle_client(client_socket):
    client_request = client_socket.recv(1024).decode()
    print(f'This is client request: {client_request}')

    server_header = client_request.split('\n')
    method, filename, _ = server_header[0].split()

    if filename == '/':
        filename = '../web/index.html'
    elif filename == '/info':
        filename = '../web/ipsum.html'

    try:
        with open('../web/' + filename) as file:
            content = file.read()
            response = 'HTTP/1.1 200 OK\n\n' + content
            client_socket.sendall(response.encode())

            print('HTTP/1.1 200 OK\r\n')
    except FileNotFoundError:
        with open('../web/404.html') as file:
            content = file.read()
            response = 'HTTP/1.1 404 Not Found\n\n' + content
            client_socket.sendall(response.encode())
            print('HTTP/1.1 404 Not Found\r\n')
    client_socket.close()


def start_server(server_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.listen(5)
    print(f'Server ready to listen at port: {server_port}')

    while True:
        client_socket, client_addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

start_server(8080)
