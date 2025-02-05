from modules.game import Game

game = Game()
game.deck.shuffle()
game.humandeal(2)
print(game.human.hand)
