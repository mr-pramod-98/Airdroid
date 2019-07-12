import server
import FileShare
import ShareZone

class main():
        conn = " "

        # CREATING CONNECTION BETWEEN SERVER AND CLIENT
        def start(self, n):

                global conn
                obj = server.networking()

                # CREATING THE SOCKET
                obj.create_socket()

                # BINDING PORT AND PUTTING PORT TO LISTEN MODE
                obj.bind_socket()

                # ESTABLISHING CONNECTION WITH THE CLIENT
                conn = obj.socket_accept(n)


        '''============================= EXECUTION STRARTS FROM HEAR - StartMain()==================================='''

        def StartMain(self):

                global conn

                opt = input("Menu:\n1.FileShare\n2.ShareZone\n")

                # INITIATING NORMAL MODE
                if opt == '1':

                        NAME = input("Enter your name : ")
                        NAME = NAME.upper()
                        m.start(1)
                        normal = FileShare.Mode(opt, conn)
                        normal.NormalStart(NAME)

                # INITIATING GROUP MODE
                elif opt == '2':

                        while True:

                                # "n" INDICATES NUMBER OF CONNECTION
                                n = int(input("Enter number of connections(minimum of 2 connections are requried to activate group chat ): "))
                                if n >= 2:
                                        break
                                else:
                                        print("minimum of two connections are requried")
                        m.start(n)
                        group = ShareZone.Mode(n, opt, conn)
                        group.GroupStart()

                else:
                        print("invalid choice")


'''=================== EXECUTES ONLY IF "main.py" IS EXECUTED AS THE FIRST FILE TO BE EXECUTED ======================'''

if __name__ == "__main__":

        # CREATING OBJECT OF CLASS "main"
        m = main()

        # INITIATING "StartMain"
        m.StartMain()
