import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345
s.connect((HOST_NAME, PORT))
while True:
    msg = s.recv(100)
    print("Server : " + msg.decode('utf-8'))
    message_to_send = input("Client : ")
    s.send(bytes(message_to_send, "utf-8"))
