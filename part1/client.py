import socket

HOST = "127.0.0.1"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as x:
    x.connect((HOST,PORT))

    x.sendall(b"Hello from Client-AdamZ\n")

    while True:
        data = x.recv(1024)
        if not data:
            break

        print("[SERVER]:", data.decode())

        message = input("You: ")
        x.sendall(message.encode() + b"\n")

        if message.startswith("Bye"):
            data = x.recv(1024)
            print("[SERVER]:", data.decode())
            break