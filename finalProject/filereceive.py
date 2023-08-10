import socket
import os

def receive_file(client, file_path, file_size):
    client.send(b"ACK")  # Send acknowledgment back to client to start receiving the file

    # Receive the actual file data from the client
    with open(file_path, "wb") as file:
        received_bytes = 0
        while received_bytes < file_size:
            data = client.recv(1024)
            received_bytes += len(data)
            file.write(data)

    print(f"File received: {file_path}")
    client.send(b"ACK")  # Send acknowledgment back to client for successful file reception

def fileserver(destination_directory):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("192.168.1.131", 9999))
    print("Server is listening on 192.168.1.131:9999")
    server.listen()

    client, addr = server.accept()
    print(f"Connection established with {addr}")

    while True:
        data = client.recv(1024).decode()
        if data == "<END>":
            break

        file_name, file_size = data.split(",")
        file_size = int(file_size)

        # You can specify a directory where you want to store the received files
        # Replace "/path/to/destination" with the desired directory path
        file_path = os.path.join(destination_directory, file_name)

        receive_file(client, file_path, file_size)

    client.close()
    server.close()

if __name__ == "__main__":
    destination_directory = "/home/tester/finalProject/videos"
    fileserver(destination_directory)
