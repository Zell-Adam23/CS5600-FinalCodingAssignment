import socket

#ports can be adjusted later, this is just for testing purposes
HOST = "0.0.0.0"
PORT = 5000


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as x:
    x.bind((HOST,PORT))
    x.listen(1)
    
    while True:
        print(f"[SERVER] Listening on {HOST}:{PORT} for next client")
        connection, address = x.accept()

        with connection:
            print(f"[SERVER] Connected by {address}")
            connection.sendall(b"Hello from Server-AdamZ\n")

            while True:
                data = connection.recv(1024)
                if not data:
                    break
                message = data.decode().strip()
                print("[CLIENT]:", message)

                if message == "exit":
                    print("[SERVER] Client disconnect")
                    break
