import socket


class Networking:

    _socket: socket.socket
    host: str  # "host" IS THE IP ADDRESS/SYSTEM NAME OF HOST COMPUTER
    port: int

    # CREATING THE SOCKET
    @staticmethod
    def create_socket():

        try:
            Networking.host = socket.gethostname()
            Networking.port = 9999
            Networking._socket = socket.socket()

            print("HOST :", Networking.host)

        except socket.error as msg:
            print("socket creation error:", str(msg))
            print("could not create a socket")

    # BINDING PORT AND PUTTING PORT TO LISTEN MODE
    @staticmethod
    def bind_socket():

        try:
            print("binding the port:", Networking.port)
            Networking._socket.bind((Networking.host, Networking.port))
            Networking._socket.listen(1)

        except socket.error as msg:
            print("socket binding error:", str(msg), "\n retrying.....")
            Networking.bind_socket()

    # ESTABLISHING CONNECTION WITH THE CLIENTS
    @staticmethod
    def socket_accept(n):

        all_connection = []

        if n == 1:
            conn, address = Networking._socket.accept()
            return conn

        else:
            # CREATING "n" CONNECTION
            for i in range(n):
                conn, address = Networking._socket.accept()
                print("client-", i, " ", conn)
                all_connection.append(conn)

            print("connection established!!!!")
            return all_connection
