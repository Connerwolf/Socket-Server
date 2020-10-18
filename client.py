import socket

def client(port):
    host = socket.gethostname()
    p = port
    client_socket = socket.socket()
    client_socket.connect((host,p))

    s = input("You: ")

    while s != "end":
        s = s.encode()
        client_socket.send(s)
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Server[{host}]: {data}")
        s = input("You: ")

    client_socket.close()

if __name__ == '__main__':
    client(1414)