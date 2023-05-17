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
    