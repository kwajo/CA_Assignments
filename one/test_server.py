import server
import socket



def test_create_socket():
    s = server.Server()
    s.create_socket()
    assert isinstance(s.socket,socket.socket)  