from modules.game import Game

game = Game()
#game.deck.shuffle()
#game.first_turn(200)
#game.second_turn()
#game.third_turn(True)
#game.fourth_turn()
#for card in game.human.hand:
#    print(f"human:", card.card_scores)
#for card in game.dealer.hand:
#    print(f"dealer:",  card.card_scores)
#game.check_win()
#game.ritorno()
#print(game.human.money)
#print(game.check_score())
while game.human.money != 0:
    game.test_gioca()

