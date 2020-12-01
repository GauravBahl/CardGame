from enum import Enum

class Card:


    def __init__(self, value, suit):
        self.suit = suit
        self.value = value
        self.available = False

    def show(self):
        print("{} of {}".format(self.value, self.suit))
    
    def isAvailable(self):
        return self.available
    
    def markUnavailable(self):
        self.available = False
    
    def markAvailable(self):
        self.available = True

