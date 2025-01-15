import streamlit as st
from modules.card import Card
from modules.deck import Deck

st.set_page_config(
   layout="wide",
)
card_width=95


number_of_decks = st.number_input("Number of decks", min_value=1, max_value=10, value=1)

deck = Deck(number_of_decks)


st.markdown(f"## Deck created with {number_of_decks} deck/s")

#st.image([card.image for card in deck.cards], width=card_width)

st.markdown("## Shuffling deck")
shuffle_button = st.button("Shuffle")
if shuffle_button:
    deck.shuffle()
st.image([card.image for card in deck.cards], width=card_width)
st.image(Card.flipped("2C"), width = card_width)

give_card = st.button("Give")

if give_card:
    deck.give()
st.image([card.image for card in deck.cards], width=card_width)

home = st.button("Home", use_container_width= True)
if home:
    st.switch_page("home.py")