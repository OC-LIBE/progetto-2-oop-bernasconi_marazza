import streamlit as st
from modules.card import Card
from modules.deck import Deck
from modules.player import Player, Human

class Game:
    def __init__(self, deck, player):
        self.deck = Deck(6).shuffle()
        self.player = player

