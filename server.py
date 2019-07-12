import socket

class networking:

        # CREATING THE SOCKET
        def create_socket(self):

                try:
                        global s
                        global host     # "host" IS THE IP ADDRESS/SYSTEM NAME OF HOST COMPUTER
                        global port

                        host = socket.gethostname()
                        port = 9999

                        s = socket.socket()
                        print("HOST :", host)

                except socket.error as msg:
                        print("socket creation error:", str(msg))
                        print("cound not create a socket")


        # BINDING PORT AND PUTTING PORT TO LISTEN MODE
        def bind_socket(self):

                try:
                        global host
                        global port
                        global s
                
                        print("binding the port:" + str(port))
                        s.bind((host,port))
                        s.listen(1)

                except socket.error as msg:
                        print("socket binding error:", str(msg), "\n retrying.....")
                        self.bind_socket()


        # ESTABLISHING CONNECTION WITH THE CLIENTS
        def socket_accept(self, n):

                all_connection = []
                global s

                if n == 1:
                        conn, address = s.accept()
                        return conn

                else:
                        # CREATING "n" CONNECTION
                        for i in range(n):
                                conn, address = s.accept()
                                print("client-", i, " ", conn)
                                all_connection.append(conn)
                        print("connection established!!!!")
                        return all_connection
