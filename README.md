# Network-Chat-programming_py
A real-time chat system built using network programming in Python. Utilizes sockets and multithreading to support dynamic chat rooms and real-time message broadcast. Ideal for learning about network programming.

'server.py'

 ➤ Imports the socket module
 
 ➤ Creates a socket with the address family AF_INET (IPv4) and socket type SOCK_STREAM (TCP)
 
 ➤ Gets the host name of the server and sets the port to 12345
 
 ➤ Binds the socket to the host name and port
 
 ➤ Listens for incoming connections with a maximum queue size of 4
 
 ➤ Accepts incoming connections and stores the client socket and its address
 
 ➤ Continuously accepts messages from the user and sends them to the client
 
 ➤ Receives messages from the client and displays them on the server
 

'client.py'

 ➤ Imports the socket module
 
 ➤ Creates a socket with the address family AF_INET (IPv4) and socket type SOCK_STREAM (TCP)
 
 ➤ Gets the host name of the client and sets the port to 12345
 
 ➤ Connects the socket to the server with the host name and port
 
 ➤ Continuously receives messages from the server and displays them on the client
 
 ➤ Accepts messages from the user and sends them to the server
 
 
 <br>
 <h1><b>Two-Way Communication Server-Client Program</b></h1>
 
This is a simple two-way communication program between a server and a client using sockets. The program uses the socket module in Python.

Files

✱ The program consists of two files:<br>● server.py  <br>● client.py
<br>
<h3>Running the Program</h3>
Start the server by running python server.py in your terminal.
<br>
Start the client by running python client.py in a separate terminal window.
<br>
The client will connect to the server and you can start sending messages back and forth between the client and the server.
