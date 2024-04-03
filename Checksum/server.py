import socket, json
from checksum import get_check_sum
def serve(port):
    print("Server started at ", port)
    while True:
        # create a socket object 
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # ipv4, udp
        # bind the socket to a specific address and port 
        server_socket.bind(('0.0.0.0', port)) 
        # handle communication with the client 
        while True: 
            data = server_socket.recvfrom(1024) 
            if not data: 
                break 
            json_string = data[0].decode()
            print("Data Received:", json_string)
            parsed_json = json.loads(json_string)
            header =  parsed_json["header"]
            server_socket.sendto(str(get_check_sum(header)).encode(),data[1]) 
        # close the socket 
        server_socket.close()

serve(2000)