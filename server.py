import socket

def server(port, listeners):
    host = socket.gethostname()
    p = port
    server_socket = socket.socket()
    server_socket.bind((host,p))

    server_socket.listen(listeners)
    client, address = server_socket.accept()
    print(f"Connection: Client{address}")

    while True:
        data = client.recv(1024).decode('utf-8')

        if not data:
            break
        else:
            print(f"Client[{address[0]}]: {data}")
            s = input("You: ")
            s = s.encode()
            client.send(s)

    client.close()

if __name__ == '__main__':
    server(1414, 1)