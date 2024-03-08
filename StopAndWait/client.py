import socket,json,random,time

class Client:
    def __init__(self, host='localhost', port=3000,timeout=5):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        self.socket.settimeout(timeout)
        print("[INFO] Client Active")

    def receive(self, buffer_size=1024):
        try:
            data = self.socket.recv(buffer_size)
            return data.decode()
        except socket.timeout:
            return None

    def send(self, data, buffer_size=1024):
        self.socket.sendall(data.encode())

    def falsySend(self, data:str,seq:int,isfst:bool):
        """Simulate dataloss"""
        if random.choice([False,False,False,True]): # 1/3 chance of lost packet
            print("[FALT] Simulating Packet Loss: Data " + data + " is lost")
            return

        if random.choice([False,False,False,True]) and not isfst: # 1/3 chance of wrong seq
            seq = random.randint(100,2000)
            print("[FALT] Simulating Wrong Sequence No: ",seq )
            time.sleep(1)

        self.send(json.dumps({"data":data,"seq":seq}))

    def close(self):
        self.socket.close()



if __name__ == "__main__":
    client = Client(port=3001,timeout=7)
    sequenceNo = random.randint(2000,9000)
    startSeqNo = sequenceNo
    userData = input("[INPT] Enter Data to send: ")
    while sequenceNo -  startSeqNo < len(userData):
        print("\n[SEND] Sending character: ", userData[sequenceNo - startSeqNo])
        client.falsySend(userData[sequenceNo - startSeqNo],seq=sequenceNo,isfst=(sequenceNo == startSeqNo))
        receivedData = client.receive() # next no | none 
        if(receivedData == None):
            print("[ACKN] No acknowledgement Received, Sending" , userData[sequenceNo - startSeqNo], "again...")
            time.sleep(2)
        else:
            print("[ACKN] Acknowledgement Received.")
            sequenceNo = int(receivedData)
            time.sleep(1)

    # Close the connection
    print("[INFO] Client Closed")
    client.close()