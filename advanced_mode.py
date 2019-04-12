import sys

class Mode:

        global conn
        global option

        def __init__(self, opt, conn_obj):

                global conn, option
                conn = conn_obj
                option = opt

        # CREATING CONNECTION BETWEEN SERVER AND CLIENT
        def AdvanceStart(self):

                # SENDING COMMANDS TO CLIENTS
                send_command(conn)


'''================================================ SENDING COMMANDS ================================================'''

def send_command(conn):

        # SETTING INITIAL LOOK AND INITIAL CONDITION
        print("\n============================================ OPERATING IN ADVANCE MODE ==========================================\n")
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
                        print(client_response, end="")
