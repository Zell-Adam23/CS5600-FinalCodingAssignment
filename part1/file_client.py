import socket

HOST = "127.0.0.1"
PORT = 5000

default_send_file = "sample.txt"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as x:
    x.connect((HOST,PORT))

    data = open(default_send_file, "rb").read()
    size = len(data)

    x.sendall(str(size).encode())
    x.recv(1024)

    x.sendall(data)

    updated_size = int(x.recv(1024).decode())
    x.sendall(b"OK")

    updated_data = b""
    while len(updated_data) < updated_size:
        chunk = x.recv(4096)
        if not chunk:
            break
        updated_data += chunk

    print("file recieved\n")
    print(updated_data.decode(errors="ignore"))
    print("\nEOF\n")

    with open("client_updated.txt", "wb") as y:
        y.write(updated_data)