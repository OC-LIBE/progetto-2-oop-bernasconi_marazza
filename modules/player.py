from modules.card import Card
from modules.deck import Deck
import streamlit as st

class Player:
    def __init__(self, name = "Player", hand = []):
        self.name = name
        self.hand = hand
    
    def hand_draw(self, deck = object):
        cards = [deck.cards[0], deck.cards[2]]
        self.hand.append(cards)
        deck.remove(cards)
        return self.hand
        
    def fold(self, hand):
        self.hand = []