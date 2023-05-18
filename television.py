# Create a class
class tv_controller():
    # Create a special init method
    def __init__(self, screen = "OFF", volume = 0, channel = 1):
        # Select all instance variables
        self.screen = screen
        self.volume = volume
        self.channel = channel
    # Create methods to turn the TV on and OFF
    def tv_open(self):
        if self.screen == "ON":
            print("Tellie is on already, silly!")
        else:
            self.screen = "ON"
            print("The Tellie is now on! What shall we do next?")
    def tv_close(self):
        if self.screen == "OFF":
            print("Tellie is off already, silly!")
        else:
            self.screen = "OFF"
            print("The Tellie is now off! It's not a good idea to spend so much time watching the Tellie, good job!")
            
    # Create method to change the volume of the TV
    def tv_volume(self):
        max_vol = 100
        min_vol = 0
        while(True):
            print(""""\\\\ CHANGE THE VOLUME LEVEL ////\nVolume + 'UP'\nVolume - 'DOWN'\nRETURN 'R'""")
            volume_command = input("= ").upper()
            if volume_command == str("UP"):
                if self.volume >= max_vol:
                    print("Wah! The Tellie is already at max volume! My ears!")
                else:
                    self.volume += 1
                    print("Volume is now " + str(self.volume))
            elif volume_command == "DOWN":
                if self.volume <= min_vol:
                    print("The Tellie is already at min volume! I can't hear a thing.")
                else:
                    self.volume -= 1
                    print("Volume is now " + str(self.volume))
            elif volume_command == "R":
                break
            else:
                print("I do not understand would you like to try again? YES or NO?")
                tryagain_volume = input("= ").upper()
                if tryagain_volume == "YES":
                    True
                elif tryagain_volume == "NO":
                    break
                else:
                    print("I do not understand the command, please input it once more.")
                    print("Would you like to try again?")
                    tryagain_volume_errorcommand = input("= ").upper()
                    if tryagain_volume_errorcommand == "YES":
                        True
                    else:
                        break
    
    # Create method to change the channel of the TV
    def tv_channel(self):
        max_chan = 30 
        min_chan = 1
        while(True):
            print("\\\\ CHANGE THE CHANNEL ////\nChannel + 'UP'\nChannel - 'DOWN'\nRETURN 'R'")
            channel_command = input("= ").upper()
            if channel_command == str("UP"):
                if self.channel >= max_chan:
                    print("You have reached the maximum channel")
                else:
                    self.channel + 1
                    print("The channel is now on channel " + str(self.channel))
            elif channel_command == "DOWN":
                if self.channel <= min_chan:
                    print("You have reached the minimum value")
                else:
                    self.channel - 1
                    print("The channel is now on channel " + str(self.channel))
            elif channel_command == "R":
                break
            else:
                print("I do not understand would you like to try again? YES or NO?")
                tryagain_channel = input("= ").upper()
                if tryagain_channel == "YES":
                    True
                elif tryagain_channel == "NO":
                    break
                else:
                    print("I do not understand the command, please input it once more.")
                    print("Would you like to try again?")
                    tryagain_channel_errorcommand = input("= ").upper()
                    if tryagain_channel_errorcommand == "YES":
                        True
                    else:
                        break
    
    # Create a method that lists out the TV status
    def __str__(self):
        return """....... TELLIE INFORMATION .......\nTellie is: {}\nTellie's Current Volume: {}\nTellie's Current Channel: {}""".format(self.screen, self.volume, self.channel)