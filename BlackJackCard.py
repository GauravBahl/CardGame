from Card import Card

class BlackJackCard(Card):
    
    def __init__(self, value, suit):
        super(value, suit)

    def get_value(self):
        if self.is_ace():
            return 1
        elif(self.value>=11 and self.value<=13):
            return 10
        else:
            return self.value

    def is_ace(self):
        return self.value == 1
    
    def max_value(self):
        if (self.is_ace()): return 11
        else: return self.value

    def min_value(self):
        if(self.is_ace()): return 1
        else: return self.value

    def is_face_card(self):
        return self.value>=11 and self.value<=13
    

        