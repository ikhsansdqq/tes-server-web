import socket
import threading

server_host = 'localhost'


def handle_client(client_socket):
    client_request = client_socket.recv(1024).decode()
    print(f'This is client request: {client_request}')

    server_header = client_request.split('\n')
    method, filename, _ = server_header[0].split()

    if filename == "/":
        filename = "/index.html"
    elif filename == "/info":
        filename = "/ipsum.html"

    try:
        fin = open('web' + filename, encoding='ISO-8859-1')
        content = fin.read()
        response = 'HTTP/1.1 200 OK\r\n\r\n' + content
        client_socket.sendall(response.encode())
        print('HTTP/1.1 200 OK\r\n')
    except FileNotFoundError:
        fin = open('web/404.html')
        content = fin.read()
        response = 'HTTP/1.1 404 NOT FOUND\r\n\r\n' + content
        client_socket.sendall(response.encode())
        print('HTTP/1.1 404 Not Found\r\n')

    client_socket.close()


def start_server(serverport):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_host, serverport))
    server_socket.listen(5)
    print(f"Ready to listen at port: {serverport}")

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()


while True:
    client_port_input = input("Please input a port number (ex: 8080): ")

    try:
        server_port = int(client_port_input)
        if len(str(server_port)) != 4:
            raise ValueError("Invalid port number. Please enter a 4-digit number.")
        start_server(server_port)
    except ValueError as e:
        print("Error:", str(e))
