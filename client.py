import socket
from threading import *
import File_Transfer


# "NAME" IS USED AS THE REFERENCE NAME FOR CLIENT
global NAME, opt

# "FIRST" IS USED TO MAKE SURE THAT THIS FILE IS EXECUTED ONLY ONCE
FIRST = True

# "CONNECTED" IS USED TO CHECK IF CLIENT IS CONNECTED OR NOT
CONNECTED = True

'''======================================== THREAD RECIVE FOR NORMAL MODE ==========================================='''


# DEFINATION OF CLASS "recive"
class receive(Thread):

        def run(self):

                try:
                        def receiving():

                                # WHILE LOOP IS USED TO KEEP THE THREAD ALIVE UNTIL THE CONNECTION IS BROKEN
                                while True:

                                        # INITIALLY "CONNECTED" IS TRUE
                                        global CONNECTED

                                        # RECEIVES MESSAGES FROM SERVER ONLY IF CONNECTED
                                        if CONNECTED:

                                                try:
                                                        msg = s.recv(1024)

                                                        # CLOSES THE CONNECTION IF "msg" IS "exit"
                                                        if 'exit' in msg.decode() and '>>' not in msg.decode():
                                                                print(msg.decode())
                                                                CONNECTED = False

                                                        elif "/FILE/" in msg.decode():
                                                                path = msg.decode()
                                                                path = path.replace("/FILE/", "")
                                                                file_out = File_Transfer.Receive(s, path)
                                                                file_out.start()

                                                        else:
                                                                print(msg.decode())

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

'''========================================= THREAD SEND FOR NORMAL MODE ============================================'''


# DEFINITION OF CLASS "send"
class send(Thread):

        def run(self):

                try:
                        def sending():
                                while True:

                                        # INITIALLY "CONNECTED" IS TRUE
                                        global CONNECTED

                                        reply = input()

                                        # CHECKING IF CLIENT IS CONNECTED TO SERVER OR NOT
                                        if CONNECTED:

                                                try:
                                                        # CLOSES THE CONNECTION IF "replay" IS "exit"
                                                        if reply == "exit":
                                                                print("SUCCESSFULLY DIS-CONNECTED")
                                                                reply = NAME + " " + reply
                                                                s.send(reply.encode())
                                                                CONNECTED = False

                                                        elif "FILE >" in reply:
                                                                path = reply.replace("FILE >", "")
                                                                request = "/FILE/" + path
                                                                s.send(request.encode())

                                                                if opt == '1':
                                                                        file_out = File_Transfer.Send(s, path, NAME)
                                                                        file_out.start()

                                                        else:
                                                                reply = NAME + ">> " + reply
                                                                s.send(reply.encode())

                                                except:
                                                        pass

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

'''============================================= NORMAL MODE ========================================================'''


# CLIENT WORKING IN NORMAL MODE
def FileShare():
        global NAME
        NAME = input("Enter your name : ")
        NAME = NAME.upper()

        print("\n============================================ OPERATING IN NORMAL MODE ==========================================\n")
        print("                          ************************ READY TO USE ***********************                        \n")

        # INITIATING "receive" THREAD
        message_in.start()

        # INITIATING "send" THREAD
        message_out.start()

        # join IS USED TO MAKE SURE THAT "main Thread" DOES NOT EXIT UNTIL "sub-Thread" ARE DONE WITH THEIR WORK
        message_in.join()
        message_out.join()


'''============================================= GROUP MODE ========================================================'''


# CLIENTS WORKING IN GROUP MODE
def ShareZone():
        global NAME
        NAME = input("Enter your name : ")
        NAME = NAME.upper()

        print("\n============================================ SHARE ZONE ==========================================")
        print("                          ************************ READY TO USE ***********************                        \n")

        # INITIATING "receive" THREAD
        message_in.start()

        # INITIATING "send" THREAD
        message_out.start()

        # join IS USED TO MAKE SURE THAT "main Thread" DOES NOT EXIT UNTIL "sub-Thread" ARE DONE WITH THEIR WORK
        message_in.join()
        message_out.join()


'''===================================== STARTING CONNECTION WITH THE SERVER ========================================'''

if FIRST:

        def start_connection():

                try:
                        global s
                        s = socket.socket()
                        host = input("Enter host name : ")
                        port = 9999

                        s.connect((host, port))
                except:
                        print("trying to connect host....")
                        start_connection()

                # "opt"  CONTAINS THE MODE OF WORKING
                global opt
                opt = s.recv(1024).decode()

                # IF "opt" IS "1" INITIATE "normal mode"
                if opt == '1':
                        FileShare()

                # IF "opt" IS "2" INITIATE "advanced mode"
                if opt == '2':
                        ShareZone()

        # INITIATING CONNECTION
        FIRST = False
        start_connection()
