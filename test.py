from modules.game import Game

win = True
game = Game()
game.deck.shuffle()
game.first_turn(200)
game.second_turn()
while game.check_score()[1] < 17:
    game.dealerdeal()

for card in game.human.hand:
    print(f"human:", card.card_scores)
for card in game.dealer.hand:
    print(f"dealer:",  card.card_scores)
game.ritorno(win)
print(game.human.money)
print(game.check_score())