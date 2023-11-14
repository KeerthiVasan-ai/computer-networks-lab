import socket
HOST = "127.0.0.1"
PORT = 1080
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
str_ ='World Hello!'
a = str_.encode('utf-8')
s.send(a)
print(a)
data = s.recv(1024)
s.close()
print("Received",data)
