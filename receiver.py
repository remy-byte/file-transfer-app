import socket

class Receiver:

    def __init__(self, server, port):
        self.__server_ip = server
        self.__port = port
        self.__addr_ini = (self.__server_ip, self.__port)
        self.__format = 'utf-8'
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.bind(self.__addr_ini)
        self.__server.listen()

        self.__client, self.__addr = self.__server.accept()

    def start_app(self):
        self.__file_name = self.__client.recv(1024).decode(self.__format)
        print("Connection established!")
        print(self.__file_name)

        file = open(self.__file_name, "wb")

        file_in_bytes = b""

        finished = False
        print("Loading...")
        while not finished:
            data = self.__client.recv(1024)
            if file_in_bytes[-4:] == b"DONE":
                finished = True
            else:
                file_in_bytes += data

        print("done!")
        file.write(file_in_bytes)

        file.close()
        self.__client.close()
