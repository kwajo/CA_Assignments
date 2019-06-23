import socket
import sys
import time
from datetime import datetime
import threading
class Client:

    def __init__(self):
        self.HOST_IP = '10.1.1.10'#124.169.15.130'#'49.181.246.235'
        self.HOST_PORT = 5000  #works on port 80 but not 5000 w definitly a firewall issue
        self.IPV4_ADDRESS = (self.HOST_IP,self.HOST_PORT)
        self.socket = None
        self.BUFFSIZE = 2048
        self.msg_buffer = ''
        self.local_port = ()

    def create_socket(self):
        print("Creating socket")
        
        #to bind the socket object to an ipv4 port we need to pass a host, port tuple
        

        #use with to ensure connection is closed
        try:
            self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.local_port = self.socket.getsockname()
            print('Socket Created')
        except socket.error as e:
            print (e)


    def connect_to_server(self):
        print('Connecting to QwackChat')
        print('Host address-->     {}:{}'.format(c.HOST_IP,c.HOST_PORT))
        print('Local address-->    {}:{}'.format(self.local_port[0],self.local_port[1]))
        try:
            self.socket.connect(self.IPV4_ADDRESS)
            print("Connected @ {}".format(str(datetime.now())))
        except:
            print ('Connection to-->    {}:{} failed\nExiting'.format(self.HOST_IP,self.HOST_PORT))
            sys.exit()

    def send_message(self, message):
        msg = bytes(message,'UTF-8')
        try:
            self.socket.send(msg)
        except socket.error as e:
            print(e)
    
    def recieve_message(self):
        data = self.socket.recv(self.BUFFSIZE)
        return data
        
def get_message_thread(c):
    while True:
        recieved_msg = c.recieve_message()
        print(recieved_msg.decode('utf-8'))    



c = Client()
c.create_socket()
c.connect_to_server()

recv_thread = threading.Thread(target=get_message_thread,args=(c,),daemon=True)
recv_thread.start()


while True:
    
    message = input('$ ')
    c.send_message(message)
