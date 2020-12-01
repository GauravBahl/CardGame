from Deck import Deck
from CardValue import CardValue
from Suit import Suit
from Hand import Hand
from BlackJackCard import BlackJackCard
from SetDeck import SetDeck
from Board import Board
from SetCard import SetCard
from Color import Color
from Shape import Shape
from Shading import Shading
from NumberShape import NumberShape
from itertools import combinations

# d = Deck()
# d.shuffle()
# d.show()

# h = Hand()
# h.add_card(CardValue.King, Suit.SPADE)
# h.show()

# d = SetDeck()
# d.shuffle()
# deck = d.getAllCards()


b = Board()
board = b.getBoard()
comb = combinations(board, 3)
count = 0
found = []
for c in list(comb):
    status = b.compareCards(c[0], c[1], c[2])
    if(status == True):
        count = count+1
        found.append(c)

print(count)
for com in found:
    print('{}, {}, {}'.format(com[0].show(), com[1].show(), com[2].show()))

# card1 = SetCard(Color.Purple, Shape.Squiggle, Shading.Open, NumberShape.One)
# card2 = SetCard(Color.Purple, Shape.Diamond, Shading.Stripped, NumberShape.Two)
# card3 = SetCard(Color.Purple, Shape.Oval, Shading.Solid, NumberShape.Three)
# caller = SetCard()
# result = caller.compareCards(card1, card2, card3)

# print(result)

