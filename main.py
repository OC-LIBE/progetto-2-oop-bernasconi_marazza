import streamlit as st

pg = st.navigation([st.Page("home.py", title= "Rules", default=True), st.Page("play.py", title="Gioco")], position= "hidden")
pg.run()