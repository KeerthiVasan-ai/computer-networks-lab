import socket

def server_program():
    HOST = socket.gethostname()
    PORT = 5000
    server_socket = socket.socket()
    server_socket.bind((HOST,PORT))
    server_socket.listen(2)
    conn,addr = server_socket.accept()
    print("Connection From:"+str(addr))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print('From Connected user : '+str(data))
        data = input('->')
        conn.send(data.encode())
    conn.close()
        
if __name__ == "__main__":
    server_program()