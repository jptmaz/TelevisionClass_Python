# Create a class called TV
class TV_Controller():
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
    # Create a method to change the channel the television is on
    
    
    
        
    
    