# TCP Web Server

This project is a TCP-based web server developed as part of the final project assignment for the Computer Network lecture at Telkom University in 2023. The web server is designed to handle HTTP requests, perform web parsing, explore the client's requested file, and generate appropriate HTTP response messages.

## Features
1. HTTP Request Handling: The TCP web server is capable of receiving and processing HTTP requests from clients. It supports common HTTP methods such as GET, POST, PUT, DELETE, etc.
2. Web Parsing: The server parses the received HTTP requests to extract relevant information, such as the requested file path, query parameters, headers, and more. This allows the server to understand the client's intentions and respond accordingly.
3. File Exploration: Upon receiving a request for a specific file, the server explores the client's file system to locate the requested file. It handles various file types, including HTML, CSS, JavaScript, images, and more.
4. HTTP Response Generation: The server generates appropriate HTTP response messages based on the client's request. It constructs the response headers, sets the appropriate status code, and includes the requested file or relevant data in the response body.
5. Request and Response Handling: The web server efficiently manages incoming requests and maintains separate connections for each client. It ensures proper handling of multiple concurrent requests by utilizing TCP/IP protocols and socket programming techniques.

## Usage
To use this TCP web server, follow these steps:

1. Clone the project repository from GitHub link.
2. Install the necessary dependencies and libraries required to run the server. (Provide instructions or dependencies if any)
3. Run the server application by running a file named *server.py* on your preferred development environment or terminal.
5. Configure the server settings for port number and any other required parameters.
6. Access the server by opening a web browser and entering the appropriate URL and port number that was specified earlier.

## Documentation
![image](https://github.com/ikhsansdqq/tes-server-web/assets/91542488/f41f63a3-06d9-4d3d-807a-979b0f74e026)

![image](https://github.com/ikhsansdqq/tes-server-web/assets/91542488/701df76b-4708-4628-9272-ed7dca12c6a3)

## Project Specifications
This project is a TCP-based web server developed as part of the final project assignment for the Computer Network lecture at Telkom University in 2023. The web server primarily utilizes the following languages and libraries to provide its functionality:

- **Python (41.6%)**: The majority of the server's implementation is written in Python, utilizing the socket library for TCP communication, handling network connections, and managing HTTP requests and responses.
- **JavaScript with DOM (36.5%)**: JavaScript is used to enhance the web server's interactivity and dynamic behavior on the client side. The Document Object Model (DOM) is employed to manipulate and update the server-generated HTML content dynamically.
- **HTML (12.9%)**: HTML is employed to structure the web server's content and define the layout of the webpages. It is responsible for presenting the requested files to clients and rendering them in web browsers.
- **CSS (9.0%)**: Cascading Style Sheets (CSS) are utilized to enhance the visual presentation and styling of the server-generated HTML content. It ensures a visually appealing and consistent user experience across different devices and browsers. Additionally, the Bootstrap framework is incorporated to simplify the process of creating responsive and mobile-friendly web designs.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white) ![NPM](https://img.shields.io/badge/NPM-%23CB3837.svg?style=for-the-badge&logo=npm&logoColor=white)

## Contributors
The TCP Web Server project was developed by [**Ikhsan Assidiqie**](https://github.com/ikhsansdqq), [**Fizio Ramadhan Herman**](https://github.com/fiziorh) and **Dawwi Raissa Damarjati Muljana**. This project was created as part of the final assignment for the Computer Network lecture at Telkom University in 2023.

## License
This project is released under the **[MIT License](https://opensource.org/license/mit/)**. Feel free to use, modify, and distribute this code as per the terms of the license with creator's concerns.