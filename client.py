import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345
s.connect((HOST_NAME, PORT))
msg = s.recv(100)
print(msg.decode("utf-8"))