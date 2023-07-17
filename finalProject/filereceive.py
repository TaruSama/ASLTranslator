import socket
import tqdm

def fileserver():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("192.168.1.131", 9999))
    server.listen()

    client, addr = server.accept()

    file_name = client.recv(1024).decode()
    print("Received file name:", file_name)
    client.send(b"Name received")  # Send acknowledgment back to client for file name

    file_size = int(client.recv(1024).decode())
    print("Received file size:", file_size)
    client.send(b"Size received")  # Send acknowledgment back to client for file size

    file = open(file_name, "wb")

    received_bytes = 0
    progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000, total=file_size)

    while True:
        data = client.recv(1024)
        if data == b"<END>":
            break
        received_bytes += len(data)
        file.write(data)
        progress.update(len(data))

    file.close()
    client.close()
    server.close()

if __name__ == "__main__":
    fileserver()