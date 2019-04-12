from threading import *
from time import sleep

# "NAME" IS USED TO REFER SERVER
NAME = "HOST"

# "CONNECTED" IS USED TO CHECK IF CLIENT IS CONNECTED OR NOT
CONNECTED = True

# "all_connections" IS USED HOLD ALL THE CONNECTED OBJECTS
all_connections = []

# "index" IS USED TO ACCESS ELEMENTS TO THE LIST "conn"
index = None

option = None

# DEFINATION OF CLASS "Mode"
class Mode():

        # INNITIALIZING "n"(number of connections) and "all_connections"
        def __init__(self, num, opt, conn_obj):

                global all_connections, n, option
                n = num
                all_connections = conn_obj
                option = opt

        '''========================================= START OF GROUP MODE ==========================================='''

        # STARTING GROUP MODE
        def GroupStart(self):

                '''''========================================= THREAD RECIVE ==========================================='''''

                # DEFINATION OF CLASS "recive"
                class coordinate(Thread):

                        def run(self):

                                global index
                                i = index

                                try:
                                        def reciving():
                                                while True:

                                                        # INNITIALLY "CONNECTED" IS TRUE
                                                        global CONNECTED, all_connections

                                                        # RECIVES MESSAGES FROM SERVER ONLY IF CONNECTED
                                                        if len(all_connections) > 0:
                                                                try:
                                                                        # COLLECTING THE RESPONSE OF 'i'th OBJECT IN THE LIST "all_connections"
                                                                        print(all_connections[i])
                                                                        response = all_connections[i].recv(2048)

                                                                        # CLOSES THE CONNECTION IF RESPONSE IS "exit"
                                                                        if response.decode() == "exit":
                                                                                all_connections[i].close()
                                                                                all_connections.remove(all_connections[i])

                                                                                # INTIMATING TO OTHER CONNECTED CLIENT THAT "all_connectios[i]" AS LEFT THE CONVERSATION
                                                                                for c in all_connections:
                                                                                        msg = "one of the client exited"
                                                                                        c.send(msg.encode())

                                                                        else:
                                                                                response = response.decode()

                                                                                # SENDING RESPONSE TO ALL CONNECTED CLIENTS EXCEPT TO THE CLIENT WHICH IS GENERATING THE RESPONSE
                                                                                for c in all_connections:

                                                                                        # "all_connections[i]" IS GENERATING THE RESPONSE
                                                                                        if c == all_connections[i]:
                                                                                                continue
                                                                                        c.send(response.encode())
                                                                except:
                                                                        pass

                                                        # BREAK OUT OF LOOP IF NOT CONNECTED TO SERVER
                                                        if not (len(all_connections) > 0):
                                                                break

                                except:
                                        if len(all_connections) > 0:
                                                reciving()

                                # CALL "reciving" FUNCTION ONLY IF CONNECTED TO SERVER
                                if len(all_connections) > 0:
                                        reciving()

                # "message_in" LIST IS USED TO HOLD THE OBJECTS OF CLASS "recive"
                message_in = []

                # CREATING "n" OBJECTS FOR CLASS "recive"
                for i in range(n):
                        obj = coordinate()
                        message_in.append(obj)

                '''======================================== SENDING MESSAGES ========================================'''

                # SENDING MESSAGES TO CLIENTS
                def send_messages():

                        # SETTING INITIAL LOOK AND INITIAL CONDITION
                        print("\n============================================ OPERATING IN GROUP MODE ==========================================\n")

                        for c in all_connections:
                                c.send(option.encode())

                        # INITIATING THREAD RECIVE FOR ALL THE OBJECT'S IN THE LIST "message_in"
                        for i in range(n):
                                global index
                                index = i
                                message_in[i].start()
                                sleep(1)

                # INITIATING "send_message" FUNCTION
                send_messages()
