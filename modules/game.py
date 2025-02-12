import streamlit as st
from modules.card import Card
from modules.deck import Deck
from modules.player import Player, Human, Dealer

class Game:
    def __init__(self,fake = False):
        self.deck = Deck(6, fake)
        self.human = Human()
        self.dealer = Dealer()
    
    def humandeal(self):
        cards = self.deck.draw()
        self.human.hand.append(cards)
        return self.human.hand

    def dealerdeal(self):
        cards = self.deck.draw()
        self.dealer.hand.append(cards)
        return self.dealer.hand

    def first_turn(self, bet):
        self.human.puntata(bet)
        self.bet = bet

    def second_turn(self):
        self.human.hand_draw(self.deck)
        self.dealer.hand_draw(self.deck)
        self.human.hand_draw(self.deck)
        self.dealer.hand_draw(self.deck)

    def ritorno(self, win = bool):
        if win == True:
            self.human.money += self.bet * 2
        if win == False:
            self.human.money = self.money
        
    def check_score(self):
        scorehuman = 0
        aceh = 0
        scoredealer = 0
        aced = 0
        for i in self.human.hand:
            if i.card_scores[1] == 11:  
                aceh += 1
                scorehuman += 11 
            else:
                scorehuman += i.card_scores[0]

        while scorehuman > 21 and aceh > 0:
            scorehuman -= 10  
            aceh -= 1

        for i in self.dealer.hand:
            if i.card_scores[1] == 11:  
                aced += 1
                scoredealer += 11 
            else:
                scoredealer += i.card_scores[0]

        while scoredealer > 21 and aced > 0:
            scoredealer -= 10  
            aced -= 1
        return scorehuman, scoredealer