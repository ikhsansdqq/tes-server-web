import socket

server_host = 'localhost'
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    client_port_input = input("Please input a port number (ex: 8080): ")

    try:
        server_port = int(client_port_input)
        if len(str(server_port)) != 4:
            raise ValueError("Invalid port number. Please enter a 4-digit number.")
        server_socket.bind((server_host, server_port))
        server_socket.listen(1)
        print(f"Ready to listen at port: {server_port}")
        while True:
            client_connection, client_address = server_socket.accept()
            client_request = client_connection.recv(1024).decode()
            print(f'This is client request: {client_request}')

            server_header = client_request.split('\n')
            method, filename, _ = server_header[0].split()

            if filename == "/":
                filename = "/index.html"
            elif filename == "/info":
                filename = "/ipsum.html"

            try:
                fin = open('web' + filename)
                content = fin.read()
                response = 'HTTP/1.1 200 OK\r\n\r\n' + content
                client_connection.sendall(response.encode())
                print('HTTP/1.1 200 OK\r\n')
            except FileNotFoundError:
                fin = open('web/404.html')
                content = fin.read()
                response = 'HTTP/1.1 404 NOT FOUND\r\n\r\n' + content
                client_connection.sendall(response.encode())
                print('HTTP/1.1 404 Not Found\r\n')
            client_connection.close()
    except ValueError as e:
        print("Error:", str(e))
