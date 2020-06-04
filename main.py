import Server
import FileShare
import ShareZone


class Main:
    conn: str

    # CREATING CONNECTION BETWEEN SERVER AND CLIENT
    @staticmethod
    def start(n):

        obj = Server.networking()

        # CREATING THE SOCKET
        obj.create_socket()

        # BINDING PORT AND PUTTING PORT TO LISTEN MODE
        obj.bind_socket()

        # ESTABLISHING CONNECTION WITH THE CLIENT
        Main.conn = obj.socket_accept(n)

    '''============================= EXECUTION STARTS FROM HEAR - start_main()==================================='''

    @staticmethod
    def start_main():

        opt = input("Menu:\n1.FileShare\n2.ShareZone\n")

        # INITIATING NORMAL MODE
        if opt == '1':
            name = input("Enter your name : ").upper()

            Main.start(1)
            normal = FileShare.Mode(opt, Main.conn)
            normal.NormalStart(name)

        # INITIATING GROUP MODE
        elif opt == '2':
            while True:

                # "n" INDICATES NUMBER OF CONNECTION
                n = int(input("Enter number of connections(minimum 2 connections are required for group chat ): "))
                if n >= 2:
                    break
                else:
                    print("minimum of two connections are required")

            Main.start(n)
            group = ShareZone.Mode(n, opt, Main.conn)
            group.GroupStart()

        else:
            print("invalid choice")


'''=================== EXECUTES ONLY IF "main.py" IS EXECUTED AS THE FIRST FILE TO BE EXECUTED ======================'''

if __name__ == "__main__":

    # INITIATING "StartMain" (access static-methods using class-name)
    Main.start_main()
