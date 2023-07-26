import socket
HOST = "127.0.0.1"
PORT = 1080
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn,addr = s.accept()
print('Connected By:',addr)
while 1:
    data = conn.recv(1024)
    print(data)
    if not data:
        break
    conn.send(data)
conn.close()
