import RPi.GPIO as GPIO
import socket

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind(("",1234))
my_socket.listen(5)
conn, addr = my_socket.accept()
print('Got a request')

while True:
    data = conn.recv(1000)
    if data == b'on\n':
        GPIO.output(8, True)
        continue
    if data == b'off\n':
        GPIO.output(8, False)
    if data == b'close\n':
        break

GPIO.cleanup()
conn.close()
my_socket.close()
# you can use "nc ip_addr port_no" to send a data from any device (in this case can be your computer) to the server or you can use socket_client.py to send too