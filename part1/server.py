#server.py

import socket
import threading

HOST = "0.0.0.0"
PORT = 5000

output_file = "recieved.txt"
updated_file = "updated.txt"

def recieve_message(connection):
    while True:
        try:
            data = connection.recv(1024)
            if not data:
                print("[SERVER] Client disconnected.")
                break
            print(f"[CLIENT]: {data.decode().strip()}")
        except:
            break

def send_message(connection):
    while True:
        message = input("You (Server): ")
        try:
            connection.sendall(message.encode() + b"\n")
        except:
            print("[SERVER] Send failed - client may have disconnected")
            break

def recv_all(connection, size):
    data = b""
    while len(data) < size:
        chunk = connection.recv(4096)
        if not chunk:
            break
        data += chunk
    return data

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as x:
    x.bind((HOST,PORT))
    x.listen(1)
    print(f"[SERVER] Listening on {HOST}:{PORT}")

    connection, address = x.accept()

    print(f"[SERVER] Connected by {address}")

    connection.sendall(b"Hello from Server-AdamZ\n")

    threading.Thread(target=recieve_message, args=(connection, ), daemon=True).start()
    threading.Thread(target=send_message, args=(connection, ), daemon=True).start()

    threading.Event().wait()

""" 
    with connection:
        print(f"[SERVER] Connected by {address}")

        connection.sendall(b"Hello from Server-AdamZ\n")
        pointlessfirstline = connection.recv(1024)

        while True:
            data = connection.recv(1024)
            if not data:
                break
            message = data.decode().strip()
            print("[CLIENT]:", message)

            if message.startswith("Bye"):
                connection.sendall(b"Bye from Server-AdamZ\n")
                break

            # file sharing
            if message.startswith("file"):
                filesize = int(connection.recv(1024).decode())
                connection.sendall(b"sizeok")

                print(f"[SERVER] Expecting {filesize} bytes")

                filedata = recv_all(connection, filesize)

                print("file recieved")
                print(filedata.decode(errors="ignore"))
                print("\nEOF\n")

                with open(output_file, "wb") as y:
                    y.write(filedata)
                
                updated_data = filedata + b"\nThis is an added line from the server.\n"
                with open(updated_file, "wb") as y:
                    y.write(updated_data)

                connection.sendall(str(len(updated_data)).encode())
                connection.recv(1024)
                connection.sendall(updated_data)

                print("[SERVER] updated file sent back")

            connection.sendall(f"Server recieved: {message}".encode())
 """