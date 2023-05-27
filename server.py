import os.path
import socket

host = "localhost"
port = 8080
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)
print("listening on port %s" % port)

while True:
    client_connection, client_addr = server_socket.accept()
    req = client_connection.recv(1024).decode()
    print(req)

    headers = req.split('\n')
    method, filename, _ = headers[0].split()

    if filename == '/':
        filename = '/index.html'

    if method == 'GET':
        try:
            if filename == '/download':
                file_path = 'download/example.txt'
                if os.path.isfile(file_path):
                    with open(file_path, 'rb') as f:
                        content = f.read()
                    response = "HTTP/1.1 200 OK\r\n\r\n"
                    client_connection.sendall(response.encode())
                    client_connection.sendall(content)
                else:
                    response = "HTTP/1.1 404 NOT FOUND\r\n\r\n" + "<h1>404 NOT FOUND</h1>"
                    client_connection.sendall(response.encode())
            else:
                fin = open('web' + filename)
                content = fin.read()
                fin.close()
                response = "HTTP/1.1 200 OK\r\n\r\n" + content
                client_connection.sendall(response.encode())
        except FileNotFoundError:
            try:
                fin = open('web/404.html')
                content = fin.read()
                fin.close()
                response = "HTTP/1.1 404 NOT FOUND\r\n\r\n" + content
                client_connection.sendall(response.encode())
            except FileNotFoundError:
                response = "HTTP/1.1 404 NOT FOUND\r\n\r\n" + "<h1>404 Not Found</h1>"
                client_connection.sendall(response.encode())
    elif method == 'POST' and filename == '/submit':
        data = req.split('\r\n\r\n', 1)[1]
        print("POST data:", data)
        response = "HTTP/1.1 200 OK\r\n\r\n" + "<h1>POST request processed</h1>"
        client_connection.sendall(response.encode())
    else:
        response = "HTTP/1.1 404 NOT FOUND\r\n\r\n" + "<h4>NOT FOUND</h4>"
        client_connection.sendall(response.encode())

    client_connection.close()

server_socket.close()
