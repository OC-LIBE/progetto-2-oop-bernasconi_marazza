import random
from modules.card import Card
suits = ('Spades', 'Hearts', 'Clubs', 'Diamonds')


class Deck:
    def __init__(self, number_of_decks, fake = False):
        self.number_of_decks = number_of_decks
        self.cards = []
        self.fake = fake
        self.create(self.number_of_decks, self.fake)

    def __repr__(self):
        return 'Game deck has {} cards remaining'.format(len(self.cards))

    def create(self, number_of_decks, fake = False):
        if fake:
            self.cards = [Card(6, "Spades"),Card(6, "Spades"),Card(6, "Spades"), 
                         Card(6, "Spades"),Card(10, "Spades"),Card(10, "Spades"),Card(6, "Spades")]
        else:
            decks = [Card(rank, suit) for suit in suits for rank in range(1, 14)
                 for deck in range(number_of_decks)]
            self.cards.extend(decks)
                  
    def shuffle(self):
        self.cards = random.sample(self.cards, len(self.cards))

    def draw(self):
        if len(self.cards) == 0:
            return False
        drawn_card = self.cards[0]
        self.cards.remove(self.cards[0])
        print(len(self.cards))
        return drawn_card


    def reset(self):
        self.cards = []
        self.create(self.number_of_decks)

    @property
    def remaining(self):
        return len(self.cards)