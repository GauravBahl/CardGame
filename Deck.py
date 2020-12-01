from Suit import Suit
from CardValue import CardValue
from Card import Card
import random

class Deck:
    def __init__(self):
        self.cards = [
            Card(value, suit) for value in CardValue for suit in Suit
        ]

    def getAllCards(self):
        return self.cards

    def show(self):
        print(len(self.cards))
        for c in self.cards:
            print(c.show())

    def shuffle(self):
        random.shuffle(self.cards)
    