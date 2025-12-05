import socket

#ports can be adjusted later, this is just for testing purposes
HOST = "127.0.0.1"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as x:
    x.connect((HOST,PORT))

    while True:
        message = input("You: ")
        x.sendall(message.encode() + b"\n")

        if message=="exit":
            break
