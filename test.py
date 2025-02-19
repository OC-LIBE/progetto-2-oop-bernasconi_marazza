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

#        st.session_state["playing"] = False

        if 'Human' not in st.session_state:
            st.session_state['Human'] = game.human
        if "game" not in st.session_state:
            st.session_state["game"] = game
        

        if "bet" not in st.session_state:
            st.session_state.bet=10

        punta = st.button("Bet")
        if punta:
            print("bET button clicked")
            bet()
        else:
            game.first_turn(st.session_state.bet)
            game.second_turn(st.session_state.deck)
            st.image([card.image for card in game.dealer.hand], width=card_width)
            st.image([card.image for card in game.human.hand], width=card_width)
        

        

        st.image([card.image for card in game.human.hand], width=card_width)

        #if "draw_card" not in st.session_state:
        #    st.session_state["draw_card"] = st.button("draw_card")
        #if st.session_state["draw_card"]:
        #        game.human.hand_draw(game.deck)

#player = Player()
#player.draw(deck)
#st.image([card.image for card in player.hands], width=card_width)

@st.dialog("Bet!")
def bet():
    print("BEtting")
    st.write(f"How much do you want to bet?")
    bet = st.text_input("Bet: ")
    if st.button("Submit"):
        #st.session_state.bet = {"bet": bet}
        st.rerun()