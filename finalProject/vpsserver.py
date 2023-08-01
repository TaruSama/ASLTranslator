import socket
import threading
import time

# HOST = socket.gethostbyname(socket.gethostname())

HOST = "192.168.1.131"
PORT = 1234

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

clients = []
nicknames = []


#def read_message_from_file():
#    with open("/home/tester/finalProject/sentence.txt", "r") as file:
#        return file.read().strip()


def broadcast(message):
    for client in clients:
        client.send(message)


def handle_connection(client):
    stop = False
    while not stop:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            nickname = nicknames[index]
            nicknames.remove(nickname)
            broadcast(f"{nickname} left the chat!".encode('utf-8'))
            stop = True


def main():
    print("192.168.1.131:1234 - Chat Room Host Server")
    while True:
        client, addr = server.accept()
        print(f"Connected to {addr}")

        client.send("NICK".encode('utf-8'))

        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)
        print(f"Nickname is {nickname}")

        broadcast(f"{nickname} joined the chat!".encode('utf-8'))

        client.send("You are now connected!".encode('utf-8'))

        thread = threading.Thread(target=handle_connection, args=(client,))
        thread.start()

        welcome_message = "\nWelcome to the chat room!"
        client.send(welcome_message.encode('utf-8'))


if __name__ == "__main__":
    main()