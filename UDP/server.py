import socket, json

def serve(port):
    print("Server started at ", port)
    while True:
        # create a socket object 
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # ipv4, udp
        # bind the socket to a specific address and port 
        server_socket.bind(('172.23.160.1', port)) 
        # handle communication with the client 
        while True: 
            data = server_socket.recvfrom(1024) 
            if not data: 
                break 
            json_string = data[0].decode()
            print("Data Received:", json_string)
            parsed_json = json.loads(json_string)
            list1 =  parsed_json["data"].split(",")
            list1 = [int(x) for x in list1]
            key = int(parsed_json["key"])
            payload = -1
            if  key in list1:
                payload = list1.index(key)
                print("Data Sent:",str(payload) )
            server_socket.sendto(str(payload).encode(),data[1]) 
        # close the socket 
        server_socket.close()

serve(2000)