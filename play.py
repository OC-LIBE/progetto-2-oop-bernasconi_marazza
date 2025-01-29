import streamlit as st
from modules.card import Card
from modules.deck import Deck
from modules.player import Player, Human, Dealer
from modules.game import Game

st.set_page_config(
   layout="wide",
)
card_width=95



number_of_decks = st.number_input("Number of decks", min_value=1, max_value=10, value=1)

if 'deck' not in st.session_state:
    st.session_state.deck=Deck(number_of_decks)




st.markdown(f"## Deck created with {number_of_decks} deck/s")

#st.image([card.image for card in deck.cards], width=card_width)

st.markdown("## Shuffling deck")
shuffle_button = st.button("Shuffle")
if shuffle_button:
    st.session_state.deck.shuffle()
    st.image([card.image for card in st.session_state.deck.cards], width=card_width)
    st.image(Card.flipped("2C"), width = card_width)

if "playing" not in st.session_state:
    st.session_state["playing"] = True
if st.session_state["playing"]:
    start = st.button("Start")
    if start:
        st.session_state["playing"] = False
        game = Game()
        if 'Human' not in st.session_state:
            st.session_state['Human'] = game.human
        if "game" not in st.session_state:
            st.session_state["game"] = game
        if "bet" not in st.session_state:
            st.session_state["bet"] = st.select_slider("Puntata", options=range(1,(game.human.money + 1)), value= (game.human.money + 1)//2,)
            bet = st.session_state["bet"]

        game.first_turn(bet)
        st.image([card.image for card in game.human.hand], width=card_width)

        if "draw_card" not in st.session_state:
            st.session_state["draw_card"] = st.button("draw_card")
        if st.session_state["draw_card"]:
                game.human.hand_draw(game.deck)

#player = Player()
#player.draw(deck)
#st.image([card.image for card in player.hands], width=card_width)

home = st.button("Home", use_container_width= True)
if home:
    st.switch_page("home.py")