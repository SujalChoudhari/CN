import socket, sys
# create a socket object 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# connect to the server 
client_socket.connect(('10.120.103.40', int(sys.argv[1]))) 
print("Connection to the server...")
# send data to the server 
while True:
    message = input("Enter Message:")
    client_socket.sendall(str(len(message)).encode()) 
    client_socket.sendall(message.encode()) 
    if len(message) <=0:
        break
    # receive data from the server 
    size = client_socket.recv(16) 
    data = client_socket.recv(int(size.decode())) 
    # print the data 
    print('Received:', data.decode('utf-8')) 
    # print("Connection to the server terminated.")
# close the socket 
client_socket.close()
print("Connection to the server terminated.")