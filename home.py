import streamlit as st

gioca = st.button("Gioca", use_container_width= True)
if gioca:
    st.switch_page("play.py")