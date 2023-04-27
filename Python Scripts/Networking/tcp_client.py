#/usr/bin/python3
import socket
host= "0.0.0.0"
port=8888
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))
#client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
client.send(b"Its Hot boi!!")
response=client.recv(4096)
print(response.decode())
client.close()