#client.py

import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

default_send_file = "sample.txt"

def recieve_message(connection):
    while True:
        try:
            data = connection.recv(1024)
            if not data:
                print("[CLIENT] Server disconnected.")
                break
            print(f"[SERVER]: {data.decode().strip()}")
        except:
            break

def send_message(connection):
    while True:
        message = input("You: ")
        try:
            connection.sendall(message.encode() + b"\n")
        except:
            print("[CLIENT] Send failed - Server may have disconnected")
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as x:
    x.connect((HOST,PORT))
    print("[CLIENT] Connected to server.")
    x.sendall(b"Hello from Client-AdamZ\n")

    threading.Thread(target=recieve_message, args=(x, ), daemon=True).start()
    threading.Thread(target=send_message, args=(x, ), daemon=True).start()

    threading.Event().wait()


"""
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

        #file sharing
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
"""