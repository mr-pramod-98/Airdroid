from threading import *
from time import sleep


# "CONNECTED" IS USED TO CHECK IF CLIENT IS CONNECTED OR NOT.

# "n" IS NUMBER OF CONNECTIONS.
n = 2

# "all_connections" IS USED HOLD ALL THE CONNECTED OBJECTS.
all_connections = []

# "index" IS USED TO ACCESS ELEMENTS TO THE LIST "conn".
index = None

option = None


# DEFINITION OF CLASS "Mode".
class Mode():


    # INITIALIZING "n"(number of connections) and "all_connections".
    def __init__(self, num, opt, conn_obj):

        global all_connections, n, option
        n = num
        all_connections = conn_obj
        option = opt

    '''========================================= START OF GROUP MODE ==========================================='''

    # STARTING GROUP MODE
    def GroupStart(self):

        '''''========================================= THREAD COORDINATE ==========================================='''''

        # DEFINITION OF CLASS "receive"
        class Co_ordinate(Thread):

            def run(self):

                global index
                i = index
                CONNECTED = True

                try:
                    def receiving():

                        while True:

                            # INITIALLY "CONNECTED" IS TRUE
                            global all_connections, n
                            CONNECTED = True

                            # RECEIVES MESSAGES FROM SERVER ONLY IF CONNECTED
                            if CONNECTED:

                                try:
                                    # COLLECTING THE RESPONSE OF 'i'th OBJECT IN THE LIST "all_connections"
                                    response = all_connections[i].recv(2048)
                                    response = response.decode()

                                    # CLOSES THE CONNECTION IF RESPONSE IS "exit"
                                    if 'exit' in response and '>>' not in response:

                                        # CLOSE THE CONNECTION AND DECREMENT "n"
                                        all_connections[i].close()
                                        n = n - 1
                                        CONNECTED = False

                                        # GENERATING A FRIENDLY MESSAGE TO BE SENT
                                        response = response.replace("exit", "")
                                        response = response + "left the connection, Clients left - " + str(n)

                                        # INTIMATING TO OTHER CONNECTED CLIENT THAT "all_connectios[i]" AS LEFT THE CONVERSATION.
                                        # THE EXCEPTION OF SENDING MESSAGE TO A DIS-CONNECTED IS HANDLED BY THE try AND except BLOCK.
                                        for c in all_connections:
                                            try:
                                                c.send(response.encode())
                                            except:
                                                pass

                                    elif "/FILE/" in response:

                                        # SENDING REQUEST TO ALL CONNECTED CLIENTS EXCEPT TO THE CLIENT WHICH IS GENERATING THE REQUEST
                                        for c in all_connections:

                                            # "all_connections[i]" IS GENERATING THE REQUEST
                                            # THE EXCEPTION OF SENDING MESSAGE TO A DIS-CONNECTED IS HANDLED BY THE try AND except BLOCK.
                                            if c == all_connections[i]:
                                                continue
                                            try:
                                                c.send(response.encode())
                                            except:
                                                pass

                                        try:
                                            path = response.replace("/FILE/", "")
                                            print("path :", path)
                                            file = open(path, 'rb')

                                            # SENDING DATA OF THE FILE IN A LOOP
                                            for data in file:

                                                # SENDING data TO ALL OTHER CONNECTED CLIENTS
                                                for c in all_connections:

                                                    # "all_connections[i]" IS GENERATING THE REQUEST
                                                    # THE EXCEPTION OF SENDING MESSAGE TO A DIS-CONNECTED IS HANDLED BY THE try AND except BLOCK.
                                                    if c == all_connections[i]:
                                                        continue
                                                    try:
                                                        c.send(data)
                                                    except:
                                                        pass

                                            # SENDING "FILE EXIT"  MESSAGE TO ALL CONNECTED CLIENTS EXCEPT TO THE CLIENT WHICH IS SENDING THE FILE
                                            for c in all_connections:

                                                # "all_connections[i]" IS SENDING THE FILE
                                                if c == all_connections[i]:
                                                    continue
                                                try:
                                                    c.send(bytes("FILE EXIT".encode()))
                                                except:
                                                    pass

                                            msg_complete = "file sent"
                                            all_connections[i].send(msg_complete.encode())
                                            file.close()

                                        except:

                                            # NOTIFYING SENDER THAT ERROR HAS OCCURRED
                                            msg_exception = "file could not be transfered pleas try again"
                                            all_connections[i].send(msg_exception.encode())

                                            # SENDING "FILE EXIT"  MESSAGE TO ALL CONNECTED CLIENTS EXCEPT TO THE CLIENT WHICH IS SENDING THE FILE
                                            for c in all_connections:

                                                # "all_connections[i]" IS SENDING THE FILE
                                                # THE EXCEPTION OF SENDING MESSAGE TO A DIS-CONNECTED IS HANDLED BY THE try AND except BLOCK.
                                                if c == all_connections[i]:
                                                    continue
                                                try:
                                                    c.send(bytes("TRANSFERED FILED".encode()))
                                                    c.send(bytes("FILE EXIT".encode()))
                                                except:
                                                    pass

                                    else:

                                        # SENDING RESPONSE TO ALL CONNECTED CLIENTS EXCEPT TO THE CLIENT WHICH IS GENERATING THE RESPONSE
                                        for c in all_connections:

                                            # "all_connections[i]" IS GENERATING THE RESPONSE
                                            # THE EXCEPTION OF SENDING MESSAGE TO A DIS-CONNECTED IS HANDLED BY THE try AND except BLOCK.
                                            if c == all_connections[i]:
                                                continue
                                            try:
                                                c.send(response.encode())
                                            except:
                                                pass

                                except:
                                    print("error")
                                    pass

                            # BREAK OUT OF LOOP IF NOT CONNECTED TO SERVER
                            if not CONNECTED:
                                break

                except:
                    if CONNECTED:
                        receiving()

                # CALL "receiving" FUNCTION ONLY IF CONNECTED TO CLIENT
                if CONNECTED:
                    receiving()

        # "message_in" LIST IS USED TO HOLD THE OBJECTS OF CLASS "receive"
        message_in = []

        # CREATING "n" OBJECTS FOR CLASS "receive"
        for i in range(n):
            obj = Co_ordinate()
            message_in.append(obj)

        '''======================================== SENDING MESSAGES ========================================'''

        # SENDING MESSAGES TO CLIENTS
        def send_messages():

            # SETTING INITIAL LOOK AND INITIAL CONDITION
            print("\n============================================ OPERATING IN GROUP MODE ==========================================")
            print("                         ************************ READY TO USE ************************                        \n")

            for c in all_connections:
                c.send(option.encode())

            # INITIATING THREAD RECEIVE FOR ALL THE OBJECT'S IN THE LIST "message_in"
            for i in range(n):
                global index
                index = i
                message_in[i].start()
                sleep(1)

        # INITIATING "send_message" FUNCTION
        send_messages()
