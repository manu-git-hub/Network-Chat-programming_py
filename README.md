# Network-Chat-programming_py
A real-time chat system built using network programming in Python. Utilizes sockets and multithreading to support dynamic chat rooms and real-time message broadcast. Ideal for learning about network programming.

<h1><b>Description:</b></h1>

This repository contains a simple client-server chat application implemented in Python using the `socket` and `tkinter` libraries. The `server.py` file creates a server and waits for a client to connect to it. Once a client connects, both the server and client can send messages to each other and display them in a graphical user interface (GUI) created with `tkinter`. The `client.py` file implements the client and connects to the server. 
<br>
The chat application provides a simple and intuitive way to communicate between the server and client. The GUI created using `tkinter` makes it easy for users to interact with the chat application. Additionally, the `socket` library enables low-level communication between the server and client.
<br>
This code serves as a basic example for implementing a client-server chat application, and can be modified and expanded upon to fit different use cases.
<br>
<br>



# Client-Server Chat Application

A simple chat application that allows a server and a client to send messages to each other using the `socket` and `tkinter` libraries in Python. This code serves as a basic example for implementing a client-server chat application, and can be modified and expanded upon to fit different use cases.

## Usage

1. Start the server by running `server.py`.
2. Start the client by running `client.py`.
3. Enter messages in the GUI and send them by clicking the "Send" button.
4. Received messages will be displayed in the GUI.

## Features

- Simple and intuitive GUI for sending and receiving messages.
- Communication between the server and client using the `socket` library.
- Code can be modified and expanded to fit different use cases.

## Requirements

- Python 3
- The `socket` and `tkinter` libraries.

## Note

- The application uses `localhost` as the host name and `12345` as the port number. You may modify these values as needed.
- This chat application is intended for use in a local network, and may not be secure for use over the internet.
- This code serves as a basic example for implementing a client-server chat application, and may have limitations and lack some features that are commonly found in full-fledged chat applications.

