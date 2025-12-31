import streamlit as st
from helper import *
st.set_page_config(
    Page_title="בוט שיעורי בית",
    Page_icon='🤓'
)
setRTL()

st.title("בוט שיעורי בית")

API_KEY = getAPIkey()

Message("AI","היי איך אפשר לעזור לך?")
userinput = st.chat_input("השאלה שלך")
if userinput:
    Message("User",userinput)