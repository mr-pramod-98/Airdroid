import server
import normal_mode
import advanced_mode
import group_mode

class main():
        conn = " "

        # CREATING CONNECTION BETWEEN SERVER AND CLIENT
        def start(self,n):

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

                # "n" INDICATES NUMBER OF CLIENTS TO BE CREATED( "BY DEFAULT IT SHOULD BE 1" )
                n = 1
                opt = input("Menu:\n1.private chat\n2.group chat\n3.advance\n")

                # INITIATING NORMAL MODE
                if opt == '1':

                        NAME = input("Enter your name : ")
                        NAME = NAME.upper()
                        m.start(n)
                        normal = normal_mode.Mode(opt, conn)
                        normal.NormalStart(NAME)

                # INITIATING GROUP MODE
                elif opt == '2':

                        while True:

                                n = int(input("Enter number of connections(minimum of 2 connections are requried to activate group chat ): "))
                                if n >= 2:
                                        break
                                else:
                                        print("minimum of two connections are requried")
                        m.start(n)
                        group = group_mode.Mode(n, opt, conn)
                        group.GroupStart()

                # INITIATING ADVANCED MODE
                elif opt == '3':

                        m.start(n)
                        advanced = advanced_mode.Mode(opt,conn)
                        advanced.AdvanceStart()

                else:
                        print("invalid choice")


'''=================== EXECUTES ONLY IF "main.py" IS EXECUTED AS THE FIRST FILE TO BE EXECUTED ======================'''

if __name__ == "__main__":

        # CREATING OBJECT OF CLASS "main"
        m = main()

        # INITIATING "StartMain"
        m.StartMain()
