import streamlit as st
from card import Card
from deck import Deck
from player import Player, Human, Dealer

class Game:
    def __init__(self,fake = False, win = False, pari = False):
        self.deck = Deck(6, fake)
        self.human = Human()
        self.dealer = Dealer()
        self.win = win
        self.pari = pari
    def humandeal(self):
        cards = self.deck.draw()
        self.human.hand.append(cards)
        return self.human.hand

    def dealerdeal(self):
        cards = self.deck.draw()
        self.dealer.hand.append(cards)
        return self.dealer.hand

    def first_turn(self, bet):
        if bet <= self.human.money:
            self.human.puntata(bet)
            self.bet = bet
        else:
            return "Puntata non valida"

    def second_turn(self):
        self.human.hand_draw(self.deck)
        self.dealer.hand_draw(self.deck)
        self.human.hand_draw(self.deck)
        self.dealer.hand_draw(self.deck)

    def third_turn(self, draw = False):
        self.human.hand_draw(self.deck)

    def fourth_turn(self):
        while self.check_score()[1] < 17:
            self.dealerdeal()

    def ritorno(self):
        if self.pari == True:
            self.human.money += self.bet
        elif self.win == True:
            self.human.money += self.bet * 2
        elif self.win == False:
            self.human.money = self.human.money
        
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
    
    def check_win(self):
        if self.check_score()[0] > 21:
            self.win = False
        elif self.check_score()[0] == self.check_score()[1] and self.check_score()[0] <= 21:
            self.pari = True
        elif self.check_score()[0] < self.check_score()[1] and self.check_score()[1] <= 21:
            self.win = False
        else:
            self.win = True

    def reset(self):
        self.human.fold()
        self.dealer.fold()

    def test_gioca(self):
        self.deck.shuffle()
        soldi = input("Puntata: ")
        if int(soldi) > self.human.money:
            print("Puntata non valida")
            return
        self.first_turn(int(soldi))
        self.second_turn()
        for card in self.human.hand:
            print(f"human:", card.card_scores)
        while self.check_score()[0] <= 21:
            pesca = input("Vuoi pescare (0) o lasciare (1): ")
            if int(pesca) == 0:
                self.third_turn(True)
                for card in self.human.hand:
                    print(f"human:", card.card_scores)
            elif int(pesca) == 1:
                break
        for card in self.human.hand:
            print(f"human:", card.card_scores)
        self.fourth_turn()
        for card in self.dealer.hand:
            print(f"dealer:",  card.card_scores)
        self.check_win()
        self.ritorno()
        print(self.human.money)
        print(self.check_score())
        self.reset()