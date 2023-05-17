# Create a class
class tv_controller():
    max_vol = 100
    min_vol = 0
    max_chan = 30 
    min_chan = 1
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
        while(True):
            volume_command = input("""\\\\ CHANGE THE VOLUME LEVEL ////
                               Volume + 'UP'
                               Volume - 'DOWN'
                               RETURN 'R'""")
            if volume_command == ">":
                if self.volume >= max_vol:
                    print("Wah! The Tellie is already at max volume! My ears!")
                else:
                    self.volume += 1
                    print("Volume is now " + self.volume)
            elif volume_command == "<":
                if self.volume <= min_vol:
                    print("The Tellie is already at min volume! I can't hear a thing.")
                else:
                    self.volume -= 1
                    print("Volume is now " + self.volume)
            else:
                break
            
                
            
            
        
            
        