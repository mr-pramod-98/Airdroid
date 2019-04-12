import Server
import normal_mode
import advanced_mode
import group_mode

class main():
        conn = " "

        # CREATING CONNECTION BETWEEN SERVER AND CLIENT
        def start(self,n):

                global conn
                obj = Server.networking()

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
                opt = input("Menu:\n1.normal mode(chatting)\n2.advanved mode\n3.group mmode\n")

                # INITIATING NORMAL MODE
                if opt == '1':

                        NAME = input("Enter your name : ")
                        NAME = NAME.upper()
                        m.start(n)
                        normal = normal_mode.Mode(opt, conn)
                        normal.NormalStart(NAME)

                # INITIATING ADVANCED MODE
                elif opt == '2':
                        m.start(n)
                        advanced = advanced_mode.Mode(opt,conn)
                        advanced.start()

                # INITIATING GROUP MODE
                elif opt == '3':
                        n = int(input("Enter number of connections: "))
                        m.start(n)
                        group = group_mode.Mode(n, opt, conn)
                        group.start()


                else:
                        print("invalid choice")


'''=================== EXECUTES ONLY IF "main.py" IS EXECUTED AS THE FIRST FILE TO BE EXECUTED ======================'''

if __name__ == "__main__":

        # CREATING OBJECT OF CLASS "main"
        m = main()

        # INITIATING "StartMain"
        m.StartMain()
