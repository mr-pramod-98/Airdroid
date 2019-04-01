import normal_mode
import advanced_mode

# EXECUTION STRARTS FROM HEAR - main()
class main():
    while True:
            opt = input("Menu:\n1.normal mode(chatting)\n2.advanved mode\n")

            # INITIATING NORMAL MODE
            if opt == '1':
                    normal = normal_mode.Mode(opt)
                    normal.start()

            # INITIATING ADVANCED MODE
            elif opt == '2':
                    advanced = advanced_mode.Mode(opt)
                    advanced.start()
            else:
                    print("invalid choice")
