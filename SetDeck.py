from SetCard import SetCard
from Shape import Shape
from Shading import Shading
from Color import Color
from NumberShape import NumberShape
import random

class SetDeck:

    #This will initiate 81 cards of each type
    def __init__(self):
        self.cards = [
            SetCard(color, shape, shade, num_shape) for color in Color 
                for shape in Shape for shade in Shading for num_shape in NumberShape
        ]

    
    def show(self):
        for card in self.cards:
            print(card.show())

    def getAllCards(self):
        return self.cards

    def shuffle(self):
        random.shuffle(self.cards)
    