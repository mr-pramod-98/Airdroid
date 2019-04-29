from threading import *

# "CONNECTED" IS USED TO CHECK IF CLIENT IS CONNECTED OR NOT
global CONNECTED, NAME
CONNECTED = True

global conn,address
global option


class Mode():

        # INNITIALIZING "option" and "conn"
        def __init__(self, opt, conn_obj):

                global option,conn
                conn = conn_obj
                option = opt


        '''========================================= START OF NORMAL MODE ==========================================='''

        # STARTING NORMAL MODE
        def NormalStart(self,NAME):
                global conn,address
                global option


                '''========================================== THREAD SEND ==========================================='''

                # DEFINATION OF CLASS "send"
                class send(Thread):

                        def run(self):

                                try:
                                        def sending():
                                                while True:

                                                        # INNITIALLY "CONNECTED" IS TRUE
                                                        global CONNECTED
                                                        global conn

                                                        msg = input()

                                                        # CHEACKING IF CLIENT IS CONNECTED TO SERVER OR NOT
                                                        if CONNECTED == True:

                                                                # CLOSES THE CONNECTION IF IN PUT IS "exit"
                                                                if msg == "exit":
                                                                        print("SUCCESSFULLY DIS-CONNECTED")
                                                                        conn.send(msg.encode())
                                                                        conn.close()
                                                                        CONNECTED = False

                                                                # SENDING AND RECVING MESSAGES
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


                '''========================================= THREAD RECIVE =========================================='''

                # DEFINATION OF CLASS "recive"
                class recive(Thread):

                        def run(self):

                                try:
                                        def reciving():
                                                while True:

                                                        # INNITIALLY "CONNECTED" IS TRUE
                                                        global CONNECTED
                                                        global conn
                                                        # RECIVES MESSAGES FROM SERVER ONLY IF CONNECTED
                                                        if CONNECTED:
                                                                try:
                                                                        response = conn.recv(2048)

                                                                        # CLOSES THE CONNECTION IF RESPONSE IS "exit"
                                                                        if "exit" in response.decode() and '>>' not in response.decode():
                                                                                print(response.decode())
                                                                                conn.close()
                                                                                CONNECTED = False
                                                                        else:
                                                                                print(response.decode())
                                                                except:
                                                                        pass

                                                        # BREAK OUT OF LOOP IF NOT CONNECTED TO SERVER
                                                        if not CONNECTED:
                                                                break

                                except:
                                        if CONNECTED:
                                                reciving()

                                # CALL "reciving" FUNCTION ONLY IF CONNECTED TO SERVER
                                if CONNECTED:
                                        reciving()


                # CREATING OBJECT FOR CLASS "recive"
                message_in = recive()


                '''======================================== SENDING MESSAGES ========================================'''

                # SENDING MESSAGES TO CLIENTS
                def send_messages(option):

                        # SETTING INITIAL LOOK AND INITIAL CONDITION
                        print("\n============================================ OPERATING IN NORMAL MODE ==========================================")
                        print("                         ************************ READY TO USE ************************                         \n")

                        conn.send(option.encode())

                        # INITIATING THREAD RECIVE
                        message_in.start()

                        # INITIATING THREAD SEND
                        message_out.run()

                        message_in.join()
                        message_out.join


                # INITIATING "send_message" FUNCTION
                send_messages(option)
