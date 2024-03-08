import socket
import json
import time

class Server:
    def __init__(self, host='localhost', port=3000):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        self.socket.listen(1)
        self.connection = None
        self.client_address = None
        print("[INFO] Server is active")


    def receive(self, buffer_size=1024):
        if not self.connection:
            self.connection, self.client_address = self.socket.accept()
        data = self.connection.recv(buffer_size)
        if data:
            return json.loads(data.decode())
        else: return None

    def send(self, data, buffer_size=1024):
        if not self.connection:
            self.connection, self.client_address = self.socket.accept()
        self.connection.sendall(str(data).encode())

    def close(self):
        self.connection.close()

if __name__ == "__main__":
    server = Server(port=3001)
    currentSeq = -1
    collective_data = []

    while True:
        data = server.receive()
        if data is None:
            break
        print("[INFO] Received: ", data)
        time.sleep(3)
        newSeq = int(data["seq"])
        if currentSeq < 0:
            currentSeq = newSeq
            collective_data.append(data)
        elif currentSeq + 1 == newSeq:
                currentSeq = newSeq
                collective_data.append(data)
        else:
            print("[EROR] Wrong SequenceNo received:", newSeq, "expecting:", currentSeq + 1)
        server.send(currentSeq + 1)
        print("[INFO] Sending:",(currentSeq + 1) )

    print("[INFO] Server is closed")
    print("[DATA]: Received", "".join([x["data"] for x in collective_data]))
    server.close()