import streamlit as st
from modules.card import Card
from modules.deck import Deck
from modules.player import Player, Human, Dealer

class Game:
    def __init__(self, deck, human, dealer):
        self.deck = Deck(6).shuffle()
        self.player = human
    
    def start(self, human, dealer, deck):
        human.hand_draw(deck)
        dealer.hand_draw(deck)
        human.hand_draw(deck)
        dealer.hand_draw(deck)
    
    def first_turn(self, human, deck, bet):
        