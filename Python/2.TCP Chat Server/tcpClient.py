import socket

def client_program():
    print('Type Bye To terminate')
    HOST = socket.gethostname()
    PORT = 5000
    client_socket = socket.socket()
    client_socket.connect((HOST,PORT))
    message = input("->")
    while message.lower().strip() != "bye":
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print("Received From Server : "+data)
        message = input("->")
    client_socket.close()
    
if __name__ == "__main__":
    client_program()

