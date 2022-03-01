import socket

HOST, PORT = "", 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket output
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#bind socket to ip adress
listen_socket.bind((HOST, PORT))
#make the socket to be able to accept connection
listen_socket.listen(1)

print ('Serving HTTP on port %s ...' % PORT)

while True: 
    client_connection, client_adress = listen_socket.accept()
    # max buffersize it can accept
    request = client_connection.recv(1024)
    print (request)

    http_response = """\
HTTP/1.1 200 OK

Hello, World!
"""
    # send response 
    client_connection.sendto(http_response.encode("utf-8"), (HOST, PORT))
    client_connection.close()