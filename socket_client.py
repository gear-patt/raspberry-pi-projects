import socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = ""
my_socket.connect((server_ip, 1234)) # "127.0.0.1" is a loopback ip address, which means you send the data to yourself and 1234 is the port number
while True:
    data = input('Choose the mode of the LED: ')
    my_socket.sendall(bytes((data+"\n"), "ascii"))
    if data == 'close':
        break
# you can use "nc -l 1234" to create a server to recieve the data (in this case type the command in the raspberry pi) or use socket_server.py to create a server too