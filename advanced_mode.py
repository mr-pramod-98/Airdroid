import server
import sys

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

                # SENDING COMMANDS TO CLIENTS
                send_command(option,conn)


def send_command(option,conn):

        # SETTING INITIAL LOOK AND INITIAL CONDITION
        print("operating in ADVANCED MODE: \n >>>")
        conn.send(option.encode())
        response = conn.recv(1024)
        print(response.decode(), end="")

        while True:

                cmd = input()

                # CLOSES THE CONNECTION IF INPUT IS "exit"
                if cmd == "exit":
                        print("SUCCESSFULLY DISCONNECTED")
                        conn.send(cmd.encode())
                        conn.close()
                        sys.exit()

                if len(str.encode(cmd)) > 0:
                        conn.send(str.encode(cmd))
                        client_response = str(conn.recv(2048), "utf-8")

                # CLOSES THE CONNECTION IF RESPONSE IS "exit"
                if client_response == "exit":
                        print("client exiting")

                print(client_response,end="")
