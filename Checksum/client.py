import socket, json
from checksum import get_check_sum

TCP_DUMP = lambda x: f"4500_0123_f06a_ffff_ffff_{x}_c0a8_0d01_23c3_1a34"

# create a socket object 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
# connect to the server 
message = json.dumps({"header": TCP_DUMP(get_check_sum(TCP_DUMP(0000)))})
client_socket.sendto(message.encode(),('0.0.0.0', 2000)) 
print("Send Successfully")
# receive data from the server 
data = client_socket.recvfrom(1024) 
# print the data 
print('Received:', data[0].decode('utf-8')) 
# close the socket 
client_socket.close()