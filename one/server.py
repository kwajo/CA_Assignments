import socket
#Setup Socket
class Server:

    def __init__(self):
        self.HOST_IP = ''#str(socket.INADDR_ANY)
        self.HOST_PORT = 5000
        self.IPV4_ADDRESS = (self.HOST_IP,self.HOST_PORT)
        self.socket = None
        self.BUFFSIZE = 2048
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


    '''
    no idea how to test this yet
    '''
    def search(self,attempts=10):

        #listen to port
        self.socket.listen(attempts)

        #accept connection
        print("looking for connection")
        #while True:
        conn,addr = self.socket.accept()
        print('connection formed with addr: {} and conn: {} '.format(addr,conn))
        while True:
            data, client = conn.recvfrom(self.BUFFSIZE)
            data.decode('UTF-8')
            print ("data: {}".format(data.decode('UTF-8')))
            conn.sendall(bytes('sent: {}'.format(data),'UTF-8'));

s = Server()

s.create_socket()
s.search()



    #recieve data

    #send data to server and client

    #recieve closing message
