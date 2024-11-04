import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 65432)
client_socket.connect(server_address)

try:
    message = 'Hello, Server!'
    print(f'Sending: {message}')
    client_socket.sendall(message.encode())

    data = client_socket.recv(1024)
    print(f'Received: {data.decode()}')

finally:
    client_socket.close()
