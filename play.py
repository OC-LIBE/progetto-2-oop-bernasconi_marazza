import streamlit as st
from modules.card import Card
from modules.deck import Deck
from modules.player import Player, Human, Dealer
from modules.game import Game

st.set_page_config(
   layout="wide",
)
card_width=95


#st.image([card.image for card in deck.cards], width=card_width)


if "playing" not in st.session_state:
    st.session_state["playing"] = True
if st.session_state["playing"]:
    start = st.button("Start")
    if start:
        if "game" not in st.session_state:
            game = st.session_state["game"] = Game()
            game.deck.shuffle()
        puntata = st.slider("Puntata", 0, game.human.money)
        game.first_turn(puntata)


home = st.button("Home", use_container_width= True)
if home:
    st.switch_page("home.py")