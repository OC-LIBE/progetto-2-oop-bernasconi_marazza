from modules.card import Card
from modules.deck import Deck
import streamlit as st

class Player:
    def __init__(self, hand = [], money= 1000):
        self.hand = hand
        self.money= money
    
    def draw(self, deck):
        if len(deck) == []:
            return False
        else:
            carta = [deck[0], deck[2]]
            self.hand.append([deck[0], deck[2]])
            deck.remove([deck[0], deck[2]])
            return carta