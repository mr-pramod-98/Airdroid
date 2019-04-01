import socket

class networking:

        # CREATING THE SOCKET
        def create_socket(self):
               try:
                        global s

                        # "host" IS THE IP ADDRESS OF HOST COMPUTER
                        global host
                        global port
                        host = ""
                        port = 9999
                        s = socket.socket()

               except socket.error as msg:
                        print("socket creation error:",str(msg))
                        print("cound not create a socket")


        # BINDING PORT AND PUTTING PORT TO LISTEN MODE
        def bind_socket(self):
                try:
                        global host
                        global port
                        global s
                        print("binding the port:"+ str(port))
                        s.bind((host,port))
                        s.listen(1)

                except socket.error as msg:
                        print("socket binding error:",str(msg),"\n retrying.....")
                        self.bind_socket()


        # ESTABLISHING CONNECTION WITH THE CLIENTS
        def socket_accept(self):
                global conn
                global address
                conn,address = s.accept()
                print("connection has been established!!!!")
                print("IP: ",str(address[0]))
                print("port: ",str(address[1]))
                return conn,address
