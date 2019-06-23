import socket
import threading
import queue
#Setup Socket
class Server:

    def __init__(self):
        self.HOST_IP = ''#str(socket.INADDR_ANY)
        self.HOST_PORT = 5000
        self.IPV4_ADDRESS = (self.HOST_IP,self.HOST_PORT)
        self.socket = None
        self.BUFFSIZE = 2048
        self.connections = []
        self.threads = []
        self.queue = queue.Queue()

    '''
    this function should create a socket object
    '''
    def create_socket(self):
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
        except socket.error as e:
            print (e)

        #Bind socket to port
        try:
            self.socket.bind(self.IPV4_ADDRESS)
            return True
        except socket.error as e:
            print(e)


        #starts a new thread to echo text. this is to test if multiple servers will run together

        #connection_receptor
    def echo_server(self,conn,addr,queue):
        print('Starting echo server at {}'.format(addr))
        while True:
            data, client = conn.recvfrom(self.BUFFSIZE)
            if data:
                data = data.decode('UTF-8')
                print ("data: {}".format(data))
                queue.put((data,addr))
        '''    try:
                conn.sendall(bytes('# {}'.format(data),'UTF-8'));
            except:

                print('Connection with {}:{} has ended'.format(addr[0],addr[1]))
                break;
'''
    def broadcast_message_thread(self,queue):
        print('starting_broadcast')
        while True:
            print('broadcast')
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

    def broadcast_message(self,data,origin,override=True):
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


        broadcast_thread = threading.Thread(target=self.broadcast_message_thread,args=(self.queue,),daemon=True)
        broadcast_thread.start()
        self.socket.listen(attempts)

        #accept connection
        print("looking for connection")

        while True:
            conn,addr = self.socket.accept()
            #print('connection formed with addr: {} and conn: {} '.format(addr,conn))
            self.connections.append((conn,addr))
            self.threads.append(threading.Thread(target=self.echo_server,args=(conn,addr,self.queue,),daemon=True))
            self.threads[-1].start()
            self.broadcast_message('{} Connected'.format(addr),addr)




s = Server()
s.create_socket()
s.launch()



    #recieve data

    #send data to server and client

    #recieve closing message
