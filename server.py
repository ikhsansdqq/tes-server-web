import socket
import threading

server_host = 'localhost'
# adding localhost as the server host name


def handle_client(client_socket):
    client_request = client_socket.recv(1024).decode()
    # makes the maximum bytes to receive is 1024, then decode the client request from bytes to string

    print(f'This is client request: {client_request}')
    # print client request

    server_header = client_request.split('\n')
    # splits the client request into list of strings

    method, filename, _ = server_header[0].split()
    # splits the server header into multiple strings

    if filename == "/":
        filename = "/index.html"
    # makes the root URL into index.html

    elif filename == "/info":
        filename = "/ipsum.html"
    # makes the info URL into ipsum.html

    try:
        fin = open('web' + filename)
        # makes a variable that opens up a web page with a specific URL

        content = fin.read()
        # makes content variable that shows the content using .read() method

        response = 'HTTP/1.1 200 OK\r\n\r\n' + content
        # response http/1.1 200 ok and display the content

        client_socket.sendall(response.encode())

        print('HTTP/1.1 200 OK\r\n')
        # print http/1.1 200 ok

    except FileNotFoundError:
        fin = open('web/404.html')
        # makes a variable that opens up a web page with a specific URL

        content = fin.read()
        # makes content variable that shows the content using .read() method

        response = 'HTTP/1.1 404 NOT FOUND\r\n\r\n' + content
        # response http/1.1 400 not found and display the content
        client_socket.sendall(response.encode())
        print('HTTP/1.1 404 Not Found\r\n')
        # print http/1.1 404 not found

    client_socket.close()
    # closing the connection


def start_server(serverport):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # creating a socket that uses IPv4 address and TCP

    server_socket.bind((server_host, serverport))
    # bind the socket into to a specific host and port

    server_socket.listen(5)
    # configure the socket to start listening for incoming client connection
    # and makes the maximum client usage of the connection to 5

    print(f"Ready to listen at port: {serverport}")
    # print ready to listen

    while True:
        client_socket, client_address = server_socket.accept()
        # assign the client socket object and client address to the variables

        client_thread = threading.Thread(target=handle_client, args=(client_socket,))

        client_thread.start()


while True:
    client_port_input = input("Please input a port number (ex: 8080): ")
    # creating a port based on user's input

    try:
        server_port = int(client_port_input)
        # making a server port with client port input

        if len(str(server_port)) != 4:
            raise ValueError("Invalid port number. Please enter a 4-digit number.")
        # make an error if user's input length is not 4

        start_server(server_port)
        # starting the server

    except ValueError as e:
        print("Error:", str(e))
    # if value error, then prints out error
