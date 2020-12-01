from Suit import Suit
from Card import Card

class Hand:

    def __init__(self):
        self.cards = []
    
    def add_card(self, value, suit):
        self.cards.append(Card(value, suit))
    
    def show(self):
        for c in self.cards:
            print(c.show())

