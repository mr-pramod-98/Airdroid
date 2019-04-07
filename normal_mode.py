from threading import *

# "CONNECTED" IS USED TO CHECK IF CLIENT IS CONNECTED OR NOT
global CONNECTED
CONNECTED = True

global conn,address
global message_in,replay
global option
global obj


class Mode():

        # INNITIALIZING "option" and "conn"
        def __init__(self, opt,conn_obj,socket):
                global option,conn,s
                s = socket
                conn = conn_obj
                option = opt


        '''========================================= START OF NORMAL MODE ==========================================='''

        # STARTING NORMAL MODE
        def NormalStart(self):
                global conn,address
                global s
                global replay,msg
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

                                                        msg = input(">>>")

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
                                                                        msg = msg.encode()
                                                                        conn.send(msg)

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
                reply = send()


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
                                                                        if response.decode() == "exit":
                                                                                print("client exiting")
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
                        print("operating in NORMAL MODE")
                        conn.send(option.encode())

                        # INITIATING THREAD RECIVE
                        message_in.start()

                        # INITIATING THREAD SEND
                        reply.run()

                        message_in.join()
                        reply.join


                # INITIATING "send_message" FUNCTION
                send_messages(option)
