from threading import *
import File_Transfer


# "CONNECTED" IS USED TO CHECK IF CLIENT IS CONNECTED OR NOT
CONNECTED = True
conn = None
option = None

class Mode():

        # INITIALIZING "option" and "conn"
        def __init__(self, opt, conn_obj):

                global option, conn
                conn = conn_obj
                option = opt


        '''========================================= START OF NORMAL MODE ==========================================='''

        # STARTING NORMAL MODE
        def NormalStart(self, NAME):

                global conn, option

                '''========================================== THREAD SEND ==========================================='''

                # DEFINITION OF CLASS "send"
                class send(Thread):

                        def run(self):

                                try:
                                        def sending():

                                                while True:

                                                        # INITIALLY "CONNECTED" IS TRUE
                                                        global CONNECTED
                                                        global conn

                                                        msg = input()

                                                        # CHECKING IF CLIENT IS CONNECTED TO SERVER OR NOT
                                                        if CONNECTED == True:

                                                                # CLOSES THE CONNECTION IF IN PUT IS "exit"
                                                                if msg == "exit":
                                                                        print("SUCCESSFULLY DIS-CONNECTED")
                                                                        msg = NAME + " " + msg
                                                                        conn.send(msg.encode())
                                                                        conn.close()
                                                                        CONNECTED = False

                                                                # IF "FILE >" IN THE "msg" FILE TRANSFER IS INITIATED
                                                                elif "FILE >" in msg:
                                                                        path = msg.replace("FILE >", "")
                                                                        request = "/FILE/" + path
                                                                        conn.send(request.encode())
                                                                        file_out = File_Transfer.Send(conn, path, NAME)
                                                                        file_out.start()

                                                                # SENDING AND RECEIVING MESSAGES
                                                                else:
                                                                        msg = NAME + ">> " + msg
                                                                        conn.send(msg.encode())

                                                        # BREAK OUT OF LOOP IF NOT CONNECTED TO SERVER
                                                        if not CONNECTED:
                                                                break
                                except:
                                        if CONNECTED:
                                                sending()

                                # CALL "sending" FUNCTION ONLY IF CONNECTED TO SERVER
                                if CONNECTED:
                                        sending()


                # CREATING OBJECT FOR CLASS "send"
                message_out = send()


                '''========================================= THREAD RECEIVE =========================================='''

                # DEFINATION OF CLASS "receive"
                class receive(Thread):

                        def run(self):

                                try:
                                        def receiving():

                                                while True:

                                                        # INITIALLY "CONNECTED" IS TRUE
                                                        global CONNECTED, conn

                                                        # RECEIVES MESSAGES FROM SERVER ONLY IF CONNECTED
                                                        if CONNECTED:

                                                                try:
                                                                        response = conn.recv(2048)

                                                                        # CLOSES THE CONNECTION IF RESPONSE IS "exit"
                                                                        if "exit" in response.decode() and '>>' not in response.decode():
                                                                                print(response.decode())
                                                                                conn.close()
                                                                                CONNECTED = False

                                                                        elif "/FILE/" in response.decode():
                                                                                path = response.decode()
                                                                                path = path.replace("/FILE/", "")
                                                                                file_out = File_Transfer.Receive(conn, path)
                                                                                file_out.start()

                                                                        else:
                                                                                print(response.decode())
                                                                except:
                                                                        pass

                                                        # BREAK OUT OF LOOP IF NOT CONNECTED TO SERVER
                                                        if not CONNECTED:
                                                                break

                                except:
                                        if CONNECTED:
                                                receiving()

                                # CALL "reciving" FUNCTION ONLY IF CONNECTED TO SERVER
                                if CONNECTED:
                                        receiving()


                # CREATING OBJECT FOR CLASS "recive"
                message_in = receive()


                '''======================================== SENDING MESSAGES ========================================'''

                # SENDING MESSAGES TO CLIENTS
                def send_messages(option):

                        # SETTING INITIAL LOOK AND INITIAL CONDITION
                        print("\n============================================ OPERATING IN NORMAL MODE ==========================================")
                        print("                         ************************ READY TO USE ************************                         \n")

                        conn.send(option.encode())

                        # INITIATING THREAD RECEIVE
                        message_in.start()

                        # INITIATING THREAD SEND
                        message_out.run()

                        message_in.join()
                        message_out.join()


                # INITIATING "send_message" FUNCTION
                send_messages(option)
