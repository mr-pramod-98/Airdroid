import server

class Mode:
        global conn
        global adderss
        global option
        global obj

        obj = server.networking()

        def __init__(self,opt):
                global option
                option = opt

        # CREATING CONNECTION BETWEEN SERVER AND CLIENT
        def start(self):

                # CREATING THE SOCKET
                obj.create_socket()

                # BINDING PORT AND PUTTING PORT TO LISTEN MODE
                obj.bind_socket()

                # ESTABLISHING CONNECTION WITH THE CLIENT
                conn,adderss = obj.socket_accept()

                # SENDING MESSAGES TO CLIENTS
                send_messages(option,conn)


def send_messages(option,conn):

        # SETTING INITIAL LOOK AND INITIAL CONDITION
        print("operating in NORMAL MODE")
        conn.send(option.encode())

        while True:

                msg = input(">>>")

                # CLOSES THE CONNECTION IF IN PUT IS "exit"
                if msg == "exit":
                        print("SUCCESSFULLY DIS-CONNECTED")
                        conn.send(msg.encode())
                        conn.close()
                        break

                # SENDING AND RECVING MESSAGES
                msg = msg.encode()
                conn.send(msg)
                response = conn.recv(2048)

                # CLOSES THE CONNECTION IF RESPONSE IS "exit"
                if response.decode() == "exit":
                        print("client exiting")
                        conn.close()
                        break
                else:
                        print(response.decode())
