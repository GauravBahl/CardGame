from Hand import Hand

class BlackJackHand(Hand):

    def __init__(self):
        self.scores = []
        super(self)
    
    # There are mutiple possible scores for blacjack
    # hand, since aces have mutiple values.
    # Return the maximum possible score that's under 21
    # or the lowest score that's over 
    def score(self):
        self.scores = self.possible_scores()
        max_under = -1
        min_over = 1
        for s in self.scores:
            if (s > 21 and s < min_over):
                min_over = s
            elif(s<=21 and s > max_under):
                max_under = s
    
    def possible_scores(self):
        return self.scores

    def busted(self):
        return self.score

    def is_blackjack(self):
        return self.scores == 21
    
