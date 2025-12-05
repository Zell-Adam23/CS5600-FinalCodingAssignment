import socket
import threading

#ports can be adjusted later, this is just for testing purposes
HOST = "127.0.0.1"
PORT = 5000

def message_listen(connection):
    while True:
        data = connection.recv(1024)
        if not data:
            break
        print("\n[CHAT]", data.decode(), "\nYou: ", end="")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as x:
    x.connect((HOST,PORT))
    print("connected to chat server!")

    threading.Thread(target=message_listen, args=(x, ), daemon=True).start()

    while True:
        message = input("You: ")
        x.sendall(message.encode() + b"\n")

        if message=="exit":
            break
