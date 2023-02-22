import os
import socket
import zipfile


class Sender:

    def __init__(self, server, port):
        self.__server = server
        self.__port = port
        self.__addr = (self.__server, self.__port)
        self.__format = 'utf-8'
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.connect(self.__addr)

    def start_app(self):
        self.__path_file = input("Input the path to the file: ")
        self.__path_file = self.__path_file.strip('"')
        self.__abs_source_file = os.path.abspath(self.__path_file)
        zip_file = zipfile.ZipFile("zip_file.zip", "w")
        self.__server.send("zip_file.zip".encode(self.__format))
        for dirname, subdirs, files in os.walk(self.__path_file):
            for filename in files:
                absname = os.path.abspath(os.path.join(dirname, filename))
                arcname = absname[len(self.__abs_source_file) + 1:]
                zip_file.write(absname, arcname)
        zip_file.close()

        file = open("zip_file.zip", "rb")
        file_size = os.path.getsize("zip_file.zip")
        print(f"file size in bytes: {file_size}")

        print("sending...")
        data = file.read()
        self.__server.sendall(data)
        self.__server.send(b"DONE")
        print("done!")

        file.close()
        self.__server.close()
