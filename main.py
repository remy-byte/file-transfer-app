from receiver import Receiver
from sender import Sender


def main():
    try:
        server = input("server: ")
        port = int(input("port: "))
        response = str(input("What do you want to be? \n"
                             "Receiver or sender?\n"
                             "Response type: 'r' for receiver, 's' for sender: \n"))

        if response == 'r':
            client = Receiver(server, port)
            client.start_app()
        elif response == 's':
            client = Sender(server, port)
            client.start_app()
        else:
            print("Invalid input name")

    except ValueError:
        print("invalid numeric type!")
        return


main()
