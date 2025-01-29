from modules.card import Card
from modules.deck import Deck
import streamlit as st

class Player:
    def __init__(self, name = "Player", hand = []):
        self.name = name
        self.hand = hand
    
    def hand_draw(self, deck):
        cards = deck.draw()
        self.hand.append(cards)
        return self.hand
        
    def fold(self, hand):
        self.hand = []

    def check_score(self):
        score = 0
        for i in self.hand:
            score += i
        return score
    

class Human(Player):
    def __init__(self, name = "Player", hand = [], money = 1000):
        super().__init__(name = "Player", hand = [])
        self.money = money

    def bet(self, bettings, win=bool):
        self.money = self.money - bettings
        win = True or False
        if win == True:
            self.money = self.money + bettings*2
        if win == False:
            self.money= self.money
    