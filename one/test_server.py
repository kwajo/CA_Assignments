import sqwackchat
import socket

'''
My test cases are absolutey attrocious. the client and server are codependant and
due to the way I wrote my code I cant get the server and client running together 
on a single thread. Most of my functions have no return so its hard to test them too.

'''

def test_create_socket():
    s = sqwackchat.Server()
    s.create_socket()
    assert isinstance(s.socket,socket.socket)  

def test_empty_connections():
    server = sqwackchat.Server(5000)
    server.create_socket()
    assert server.connections==[]

