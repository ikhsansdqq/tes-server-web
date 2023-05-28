import socket


def generate_html(name, birth):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Dynamic HTML</title>
    </head>
    <body>
        <h1>Welcome</h1>
        <p>Name: {name}</p>
        <p>Birth: {birth}</p>
    </body>
    </html>
    """
    return html.format(name=name, birth=birth)


def handle_request(request, theName, theBirth):
    # Extract the data from the request
    data = request.split('\r\n\r\n')[-1]  # Assuming the form data is in the body of the request

    # Extract the values from the form data
    name = theName
    birth = theBirth
    for item in data.split('&'):
        if '=' in item:
            key, value = item.split('=')
            if key == 'NAME':
                name = value
            elif key == 'BIRTH':
                birth = value

    # Generate the dynamic HTML
    html_content = generate_html(name, birth)

    # Create the HTTP response with the dynamic HTML
    response = "HTTP/1.1 200 OK\r\n"
    response += "Content-type: text/html\r\n\r\n"
    response += html_content

    return response


def run_server(names, births):
    host = ''  # Listen on all available network interfaces
    port = 8000  # Choose a port number

    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the host and port
    server_socket.bind((host, port))

    # Start listening for incoming connections
    server_socket.listen(1)

    print('Server listening on port', port)

    while True:
        # Accept a client connection
        client_socket, client_address = server_socket.accept()

        # Receive the client's request
        request = client_socket.recv(4096).decode('utf-8')

        # Handle the request and generate a response
        response = handle_request(request, names, births)

        # Send the response back to the client
        client_socket.sendall(response.encode('utf-8'))

        # Close the client connection
        client_socket.close()


if __name__ == '__main__':
    place_name = input("Please input name: ")
    place_birth = input("Please input birth: ")
    run_server(place_name, place_birth)
