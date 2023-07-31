import socket
import threading

HOST = "192.168.1.131"  # Update this to the IP address of the chat room server
PORT = 1234


def send_message(client_socket, message, nickname):
    full_message = f"{nickname}: {message}"
    client_socket.send(full_message.encode('utf-8'))


def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("An error occurred while receiving messages.")
            break


def main(translated_sentence):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((HOST, PORT))

        # Receive the "NICK" prompt from the server and send the nickname
        nickname = "TRANSLATION_MACHINE"
        client_socket.send(nickname.encode('utf-8'))

        welcome_message = client_socket.recv(1024).decode('utf-8')
        print(welcome_message)

        # Send the translated sentence as a message to the chat room
        send_thread = threading.Thread(target=send_message, args=(client_socket, translated_sentence, nickname))
        recv_thread = threading.Thread(target=receive_messages, args=(client_socket,))

        send_thread.start()
        recv_thread.start()

        send_thread.join()
        recv_thread.join()

    except KeyboardInterrupt:
        print("Chat closed by the client.")
    finally:
        client_socket.close()


if __name__ == "__main__":
    translated_sentence = "Attempt"
    main(translated_sentence)
