#!/usr/bin/env python

import socket
import threading
import queue
import sys
import time
import signal
#Setup Socket
class Server:

    def __init__(self,port=5000):
        self.HOST_IP = ''#str(socket.INADDR_ANY)
        self.HOST_PORT = port
        self.IPV4_ADDRESS = (self.HOST_IP,self.HOST_PORT)
        self.socket = None
        self.BUFFSIZE = 2048
        self.connections = []
        self.threads = []
        self.queue = queue.Queue()

    def close_connection(self,conn,addr):
        conn.close()
        self.connections.remove((conn,addr))
        
    '''
    this function should create a socket object
    '''
    def server_input_thread(self):
        while True:
            data = input('')
            if data == 'kill':
                print('killing connections')
                self.broadcast_message('kill')
                self.connections = []
    def create_socket(self):
        '''
        define the ipv4 address to bind to
        INADDR_ANY will bind to all interfaces

        https://stackoverflow.com/questions/16508685/understanding-inaddr-any-for-socket-programming what is inaddr
        https://realpython.com/python-sockets/ diagram for creating a chat
        '''


        #to bind the socket object to an ipv4 port we need to pass a host, port tuple


        #use with to ensure connection is closed
        print('connecting to socket')
        try:
            self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            print('socket connected')
        except socket.error as e:
            print ('Failed to open socket')
            sys.exit()

        #Bind socket to port
        print('binding socket to port')
        try:
            self.socket.bind(self.IPV4_ADDRESS)
            print('socket bound to port {}'.format(self.HOST_PORT))
            return True
        except socket.error as e:
            print('failed to bind socket\nexiting...')
            sys.exit()

        #starts a new thread to echo text. this is to test if multiple servers will run together

        #recieve data
    def echo_server(self,conn,addr,queue):
        print('connection established with {}'.format(addr))
        while True:
            data, client = conn.recvfrom(self.BUFFSIZE)
            if data:
                data = data.decode('UTF-8')
                '''
                Compartmentalise this command because it quits the server
                '''
                if data == '(q)':
                    print(len(self.connections))
                    self.close_connection(conn,addr)
                    print(len(self.connections))
                    return
                print ("data: {}".format(data))
                queue.put((data,addr))
     
    def broadcast_message_thread(self,queue):
        while True:
            try:
                data,origin_addr = queue.get()
            except ValueError as e:
                print (e)

            for conn, addr in self.connections:
                if origin_addr == addr:
                    continue
                try:
                    conn.sendall(bytes('{}>{}'.format(addr,data),'UTF-8'))
                except ValueError as e:
                    print (e)

    def signal_handler(self,signal, frame):
        self.broadcast_message('kill')
        print()
        for i in range (3,0,-1):
            print('closing in: {}'.format(i))
            time.sleep(1)
        sys.exit()

    def broadcast_message(self,data,origin=None,override=True):
        for conn, addr in self.connections:
            if origin == addr:
                continue
            if override:
                try:
                    conn.sendall(bytes('{}'.format(data),'UTF-8'))
                except ValueError as e:
                    print(e)
                return
            try:
                conn.sendall(bytes('{} # {}'.format(addr,data),'UTF-8'))
            except ValueError as e:
                print (e)
    def launch(self,attempts=10):

        print("listening for connections")
        self.socket.listen(attempts)
        
      
        print("Starting broadcast thread")
        broadcast_thread = threading.Thread(target=self.broadcast_message_thread,args=(self.queue,),daemon=True)
        broadcast_thread.start()
       
        print("Starting Server <command> listener")
        server_input = threading.Thread(target=self.server_input_thread,daemon=True)
        server_input.start()

        #accept connection
     

        while True:
            conn,addr = self.socket.accept()
            #print('connection formed with addr: {} and conn: {} '.format(addr,conn))
            self.connections.append((conn,addr))
            print('Connections')
            for conn,addr in self.connections:
                print(addr)
            self.threads.append(threading.Thread(target=self.echo_server,args=(conn,addr,self.queue,),daemon=True))
            self.threads[-1].start()
            self.broadcast_message('{} Connected'.format(addr),addr)



#use argparse
s = Server(int(sys.argv[1]))
s.create_socket()
signal.signal(signal.SIGINT, s.signal_handler)
s.launch()



    #recieve data

    #send data to server and client

    #recieve closing message
