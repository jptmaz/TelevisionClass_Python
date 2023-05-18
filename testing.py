from television import tv_controller

def main():
    TV = tv_controller()
    
    print("""Welcome to Tellie (a.k.a your TELLIEvision, ;) get it?
Control your Tellie's system here like you would a remote (Perhaps you lost your remote? Don't worry it happens, look under your couch.)
          [[[''''''' TELLIE SYSTEM ''''''']]]
          1. TV ON
          2. TV OFF
          3. Change Volume
          4. Change Channel
          5. TV status
          """)
    
    while(True):
        remote_command = input(str("Enter the number of the function you want to do: "))
        if remote_command == "1":
            TV.tv_open()
        elif remote_command == "2":
            TV.tv_close()
        elif remote_command == "3":
            TV.tv_volume()
        elif remote_command == "4":
            TV.tv_channel()
        elif remote_command == "5":
            print(TV)
        else:
            print("I do not understand would you like to try again? YES or NO?")
            tryagain_tv = input("= ").upper()
            if tryagain_tv == "YES":
                True
            elif tryagain_tv == "NO":
                break
            else:
                print("I do not understand the command, please input it once more.")
                print("Would you like to try again?")
                tryagain_tv_errorcommand = input("= ").upper()
                if tryagain_tv_errorcommand == "YES":
                    True
                else:
                    break

if __name__ == "__main__":
    main()
            