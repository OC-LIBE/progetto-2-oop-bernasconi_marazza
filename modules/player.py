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
    def __init__(self, name = "Player", hand = [], money = 1000, bet = 0):
        super().__init__(name = "Player", hand = [])
        self.money = money
        self.bet = 0
    
    def puntata(self, bettings):
        self.money = self.money - bettings

    def ritorno(self, bettings, win = bool):
        if win == True:
            self.money += bettings * 2
        if win == False:
            self.money = self.money
            

class Dealer(Player):
    def __init__(self, name = "Player", hand = [], flipped = True):
        super().__init__(name = "Player", hand = [])

    def draw(self, deck):
        score1 = 0
        score2 = 0
        for i in self.hand:
            score1 += i[0]
            score2 += i[1]
        while score1 < 17 and score2 <17:
            self.hand.append(deck.draw())