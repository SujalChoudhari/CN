import socket, json
# create a socket object 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
# connect to the server 
list1 = input("\n\nEnter List:")
key = input("Item to seach:")
message = json.dumps({"data": list1,"key":key})
client_socket.sendto(message.encode(),('172.23.160.1', 2000)) 
print("Send Successfully")
# receive data from the server 
data = client_socket.recvfrom(1024) 
# print the data 
print('Received:', data[0].decode('utf-8')) 
# close the socket 
client_socket.close()