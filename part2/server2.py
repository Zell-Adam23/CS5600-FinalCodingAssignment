import socket
import threading

#ports can be adjusted later, this is just for testing purposes
HOST = "0.0.0.0"
PORT = 5000

clients = []

def broadcast_to_all(message, sender):
    for x in clients:
        if x!= sender:
            try:
                x.sendall(message.encode())
            except:
                x.close()
                clients.remove(x)

def handle_new_client(connection, address):
    print(f"[SERVER] New Client connected: {address}")
    with connection:
        while True:
            data =connection.recv(1024)
            if not data:
                break
            message = data.decode().strip()
            print(f"[{address}]: {message}")

            if message == "exit":
                break

            broadcast_to_all(f"[{address}]: {message}", connection)

    print(f"[SERVER] Client {address} disconnected")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as x:
    x.bind((HOST,PORT))
    x.listen()
    print("[SERVER] Server now up and running")
    
    while True:
        print(f"[SERVER] Listening on {HOST}:{PORT} for next client")
        connection, address = x.accept()
        clients.append(connection)
        threading.Thread(target=handle_new_client, args=(connection,address), daemon=True).start()
