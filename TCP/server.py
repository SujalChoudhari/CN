import socket, functools, sys, threading

def serve(port):
    print("Server started at ", port)
    while True:
        # create a socket object 
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # ipv4, tcp
        # bind the socket to a specific address and port 
        server_socket.bind(('10.120.103.40', port)) 
        # listen for incoming connections 
        server_socket.listen() 
        # wait for a client to connect 
        client_socket, address = server_socket.accept() 
        print('Client connected at port',port)
        # handle communication with the client 
        while True: 
            size = client_socket.recv(16) 
            if not size:
                break
            data = client_socket.recv(int(size.decode())) 
            if not data: 
                break 
            
            print("Data Received:", data.decode(),"by port ",port," of size ",size.decode())
            nums =  data.decode().split(",")
            nums.sort(key=lambda x: x)

            payload = str(nums)
            client_socket.sendall(str(len(payload)).encode()) 
            client_socket.sendall(payload.encode()) 
        # close the socket 
        client_socket.close() 
        server_socket.close()
        print("Connection terminated at port no ",port)


if __name__ == "__main__":
    thread1 = threading.Thread(target=serve,args=(8000,))
    thread2 = threading.Thread(target=serve,args=(8080,))
    thread3 = threading.Thread(target=serve,args=(8090,))

    thread1.start()
    thread2.start()
    thread3.start()