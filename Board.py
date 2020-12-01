from SetDeck import SetDeck

class Board:
    
    def __init__(self):
        deck = SetDeck()
        deck.shuffle()
        allCards = deck.getAllCards()
        self.board = allCards[0:12]

    def getBoard(self):
        return self.board
    
    def showBoard(self):
        for idx, c in enumerate(self.board):
            print(idx+1)
            c.show()

    def compareCards(self, card1, card2, card3):
        factor1 = False
        factor2 = False
        factor3 = False
        factor4 = False 

        if((card1.color == card2.color and 
            card1.color == card3.color and card2.color==card3.color) or
             (card1.color != card2.color and 
            card1.color != card3.color and card2.color != card3.color)):
            factor1 = True
        if((card1.shade == card2.shade and 
            card1.shade == card3.shade and card2.shade==card3.shade) or 
            (card1.shade != card2.shade and 
            card1.shade != card3.shade and card2.shade != card3.shade)):
            factor2 = True
        if((card1.shape == card2.shape and 
            card1.shape == card3.shape and card2.shape==card3.shape) or 
            (card1.shade != card2.shade and 
            card1.shape != card3.shape and card2.shape != card3.shape)):
            factor3 = True
        if((card1.num_shape == card2.num_shape and 
            card1.num_shape == card3.num_shape and card2.num_shape==card3.num_shape) or 
            (card1.num_shape != card2.num_shape and 
            card1.num_shape != card3.num_shape and card2.num_shape != card3.num_shape)):
            factor4 = True

        return factor1 and factor2 and factor3 and factor4
           

        
