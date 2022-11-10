import socket


class client:

    def __init__(self, name, port, ip):
        self.name = name
        self.port = port
        self.ip = ip

    def connect(self):
        print("connect function invoked!")
        s = socket.socket()

        s.connect((self.ip, self.port))

        while True:
            print(s.recv(1024).decode())


user = client("name", 1024, "127.0.0.1")
user.connect()
