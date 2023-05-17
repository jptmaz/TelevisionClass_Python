# Create a class called TV
class TV_Controller():
    # Add TV variables
    max_vol = 100
    min_vol = 0
    channel_list = ["RBS", "Hiwaga", "RBS Dula", "RBS Sports", "RBS Balita", "RBS Musika", "RBS Variety"]
    channel_list = len(channel_list)
    
    # Create a special init method
    def __init__(self, screen = "OFF", volume = 7 , channel = "RBS"):
        # Set all the instance variables
        self.screen = screen
        self.volume = volume
        self.channel = channel
    # Create a method for when the television is turned on
    def TV_On(self):
        if self.screen == "ON":
            print("Your tellie is ON.")
        else:
            self.screen = "ON"
            print("Your tellie is being opened.")
    # Create a method for when the television is turned off
    def TV_close(self):
        if self.screen == "OFF":
            print("Your tellie os OFF.")
        else:
            self.screen = "OFF"
            print("Your tellie is closing now.")
    # Create a method to change the volume of the television
    def TV_Change_Volume(self):
        
    # Create a method to change the channel the television is on