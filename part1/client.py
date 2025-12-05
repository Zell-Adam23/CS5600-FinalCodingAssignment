import socket

#ports can be adjusted later, this is just for testing purposes
HOST = "127.0.0.1"
PORT = 5000

#change to send a different file
default_send_file = "sample.txt"

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

        if message.startswith("file"):
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