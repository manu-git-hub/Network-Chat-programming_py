import socket
from tkinter import *

root = Tk()


def send(listbox, entry):
    message = entry.get()
    listbox.insert('end', message)
    entry.delete(0, END)


entry = Entry()
entry.pack(side=BOTTOM)
listbox = Listbox(root)
listbox.pack()
button = Button(root, text='Send', command=lambda :send(listbox, entry))
button.pack()
root.mainloop()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345
s.bind((HOST_NAME, PORT))
s.listen(4)
client, address = s.accept()
while True:
    message = input("Server : ")
    client.send(bytes(message, "utf-8"))
    message_from_client = client.recv(50)
    print("Client : " + message_from_client.decode('utf-8'))
