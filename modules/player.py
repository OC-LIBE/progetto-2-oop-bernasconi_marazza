class player:
    def __init__(self, money):
        self.money= 1000
    
    def give(self):
        if len(self.cards) == 0:
            return False
        give_cards = self.cards[0,5]
        self.cards.remove(self.cards[0,5])
        return give_cards