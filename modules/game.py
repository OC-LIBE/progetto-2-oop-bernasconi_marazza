import streamlit as st
from modules.card import Card
from modules.deck import Deck
from modules.player import Player, Human, Dealer

class Game:
    def __init__(self):
        self.deck = Deck(6)
        self.human = Human()
        self.dealer = Dealer()
    
    def humandeal(self, rang):
        for i in range(rang):
            self.human.hand.append(self.deck.draw())

    def dealerdeal(self,rang):
        for i in range(rang):
            self.human.hand.append(self.deck.draw())

    def first_turn(self, bet):
        self.human.puntata(bet)

    def second_turn(self):
        self.human.hand_draw(self.deck)
        self.dealer.hand_draw(self.deck)
        self.human.hand_draw(self.deck)
        self.dealer.hand_draw(self.deck)

    def bet(self, bettings):
        self.bet = bettings