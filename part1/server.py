import socket

HOST = "0.0.0.0"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as x:
    x.bind((HOST,PORT))
    x.listen(1)
    print(f"[SERVER] Listening on {HOST}:{PORT}")

    connection, address = x.accept()

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

            connection.sendall(f"Server recieved: {message}".encode())
