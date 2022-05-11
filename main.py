# import socket module
from socket import *
import sys  # In order to terminate the program


def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)  # Create Socket
    # Prepare a sever socket
    # Fill in start
    serverPort = 12000  # define server point
    serverSocket.bind(('', serverPort))  # binds the ServerSocket to the specified socket address, i.e. IP address and port number.

    # Now we will define the length of the backlog queue( e.g. in our case 1)
    # which is the number of incoming connections that have been completed by the TCP/IP stack but not yet accepted by the application.
    # In the socket, server listen to connection request from clients
    serverSocket.listen(1)
    # Fill in end

    while True:
        # Establish the connection
        print('Ready to serve...')
        # Server waits for the connection requests from clients. The server creates a connection socket to the client
        connectionSocket, addr = serverSocket.accept()  # Filled in
        try:
            # Get a massage from the client and decode it (reading bytes from the socket)
            message = connectionSocket.recv(2048).decode()  # Filled in
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.read()  # Filled in
            # Send one HTTP header line into socket
            message = 'HTTP/1.1 200 OK \r\n\r\n'
            # Send the encoded massage (as bytes) inside the socket
            connectionSocket.send(message.encode())  # Filled in

            # Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())

            connectionSocket.close()
        except IOError:
            # Send response message for file not found
            message = "HTTP/1.1 200 OK  \r\n\r\n 404 Not Found"  # Filled in
            connectionSocket.send(bytes(message.encode()))

            # Close client socket
            connectionSocket.close()  # Filled in
    serverSocket.close()  # close the connection socket to specific client (not the entry socket).
    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == '__main__':
    main()
