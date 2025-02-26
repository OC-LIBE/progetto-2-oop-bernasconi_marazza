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




if "game" not in st.session_state:
    game = st.session_state["game"] = True
if st.session_state.game:
    game = Game()    
    game.deck.shuffle()


if "playing" not in st.session_state:
        st.session_state["playing"] = False
if "starting" not in st.session_state:
    st.session_state.starting = True

if st.session_state.starting:
    start = st.button("Start")
    if start:
        st.session_state.starting = False
        st.session_state["playing"] = True

if st.session_state["playing"]:   
    if not game.bet:
        soldi_puntati = st.number_input("Inserisci una puntata", 
                                            min_value=0, max_value=game.human.money)
        if st.button("Punta"):
            game.first_turn(soldi_puntati)
    if game.bet:
        st.write("Hai puntato " + str(game.bet))
        st.write(game.human.money, game.bet)
        st.session_state["playing"] = False
        game.second_turn()
    if game.human.hand.len() != 0:
        st.image(for card in game.human.hand.card, width=card_width)
    
st.write(st.session_state)
home = st.button("Home", use_container_width= True)
if home:
    st.switch_page("home.py")