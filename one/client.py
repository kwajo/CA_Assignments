import socket
import sys
import time
class Client:

    def __init__(self):
        self.HOST_IP = '10.1.1.1'#124.169.15.130'#'49.181.246.235'
        self.HOST_PORT = 80  #works on port 80 but not 5000 w definitly a firewall issue
        self.IPV4_ADDRESS = (self.HOST_IP,self.HOST_PORT)
        self.socket = None
        self.BUFFSIZE = 2048

    def create_socket(self):
        print("creating socket")
        '''
        define the ipv4 address to bind to
        INADDR_ANY will bind to all interfaces

        https://stackoverflow.com/questions/16508685/understanding-inaddr-any-for-socket-programming what is inaddr
        https://realpython.com/python-sockets/ diagram for creating a chat 
        '''
        

        #to bind the socket object to an ipv4 port we need to pass a host, port tuple
        

        #use with to ensure connection is closed
        try:
            self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            print("socket Created")
        except socket.error as e:
            print (e)


    def connect_to_server(self):
        print("Connecting to server")
        try:
            self.socket.connect(self.IPV4_ADDRESS)
            print("Connected to server Created")
        except socket.error as e:
            print (e)



    def send_message(self, message):
            message = bytes(message,'UTF-8')
            self.socket.send(message)
            print('message delivered')

c = Client()

c.create_socket()
c.connect_to_server()
while True:
    c.send_message('things and stuffs and shit')
    time.sleep(2)