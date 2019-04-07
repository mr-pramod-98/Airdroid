import server
import normal_mode
import advanced_mode

class main():
        conn = ""
        s = ""

        # CREATING CONNECTION BETWEEN SERVER AND CLIENT
        def start(self):

                global conn,s
                s = obj = server.networking()

                # CREATING THE SOCKET
                obj.create_socket()

                # BINDING PORT AND PUTTING PORT TO LISTEN MODE
                obj.bind_socket()

                # ESTABLISHING CONNECTION WITH THE CLIENT
                conn, adderss = obj.socket_accept()


        # EXECUTION STRARTS FROM HEAR - main()
        def StartMain(self):

                global conn
                opt = input("Menu:\n1.normal mode(chatting)\n2.advanved mode\n")

                # INITIATING NORMAL MODE
                if opt == '1':
                        m.start()
                        normal = normal_mode.Mode(opt,conn,s)
                        normal.NormalStart()

                # INITIATING ADVANCED MODE
                elif opt == '2':
                        m.start()
                        advanced = advanced_mode.Mode(opt,conn)
                        advanced.start()

                else:
                        print("invalid choice")

'''================================================== STARTING MAIN ======================================================='''
                        
if __name__ == "__main__":

        # CREATING OBJECT OF CLASS "main"
        m = main()

        # INITIATING "StartMain"
        m.StartMain()
