import streamlit as st

st.header("BLACK JACK")

st.subheader("Regole del gioco:")

st.write("Il giocatore riceve 2 carte che dopo aver fatto una puntata diventano visibili a tutti. Il banco riceve 2 carte una visibile e l'altra girata.")
st.write("L'obiettivo del gioco è arrivare più vicino possibile a 21 senza superarlo. Il banco deve arrivare almeno a 17 punti.")
st.write("Il giocatore può scegliere se pescare una carta dal mazzo e quante volte, per cercare di arrivare a 21, se supera il 21 perde.")
st.write("Quando il giocatore ha finito il turno, tocca al banco, che a sua volta decide se e quante volte pescare.")
st.write("Il banco vince se arriva più vicino a 21 ripetto al giocatore o se questo supera il 21. Mentre il giocatore vince se il banco supera il 21 o non raggiunge il 17, oppure se è il più vicino a 21.")

name = st.text_input("name:")

gioca = st.button("Gioca", use_container_width= True)
if gioca:
    st.switch_page("play.py")


