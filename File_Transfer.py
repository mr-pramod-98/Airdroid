import os
import subprocess


class Send():

        # INITIALIZING "conn"
        def __init__(self, connection, path, name):

                global conn_OR_socket, Path, SENDER_NAME
                conn_OR_socket = connection
                Path = path
                SENDER_NAME = name

                '''========================================== THREAD SEND ==========================================='''

        # DEFINITION OF CLASS "send"
        class send():

                def run(self):

                        try:
                                print(Path)
                                file = open(Path, 'rb')

                                # SENDING DATA OF THE FILE IN A LOOP
                                for data in file:
                                        conn_OR_socket.send(data)
                                conn_OR_socket.send(bytes("FILE EXIT".encode()))
                                print("file sent")
                                file.close()

                        except:
                                print("file could not be transfered")
                                print("pleas try again")
                                conn_OR_socket.send(bytes("TRANSFERED FILED".encode()))

        def start(self):

                # CREATING OBJECT FOR CLASS "send"
                file_out = Send.send()
                file_out.run()

class Receive():

        def __init__(self, connection, path):

                global conn_OR_socket, Path
                conn_OR_socket = connection

                # PATH CREATION FOR THE RECEIVING FILE
                Path_list = path.split("\\")
                Path = "C:\\Airdroid\\" + Path_list[-1]

                # CREATING DIRECTORY TO STORE THE RECEIVED FILE
                os.chdir("/")
                print(os.getcwd())
                subprocess.Popen("mkdir Airdroid", shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

                '''========================================= THREAD RECIVE =========================================='''

        # DEFINITION OF CLASS "receive"
        class receive():

                def run(self):

                        try:
                                file = open(Path, 'wb')
                                print("file opened at the path : ", Path)

                                while True:
                                        data = conn_OR_socket.recv(1024)

                                        if "TRANSFERED FILED" in str(data):
                                                # WRITING "data" ON TO THE FILE
                                                print("transfer failed")
                                                file.close()
                                                break

                                        if "FILE EXIT" not in str(data):
                                                # WRITING "data" ON TO THE FILE
                                                file.write(data)
                                        else:
                                                # CLOSE THE FILE WHEN "FILE EXIT" MESSAGE IS RECEIVED
                                                print("file received")
                                                file.close()
                                                break
                        except:
                                print("transfer failed")
                                file.close()

        def start(self):

            # CREATING OBJECT FOR CLASS "send"
            file_in = Receive.receive()
            file_in.run()
