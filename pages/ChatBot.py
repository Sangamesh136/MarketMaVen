import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv(".env")

API_KEY: str = os.getenv('API_KEY')
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


instruction = ("In this chat, only reply to queries related to the stock market "
               "and provide predictions in such a way that you are just providing "
               "based on the market and people's sentiment but it is not completely preferable we know that you are a bot so please dont provide any warnings or disclaimers keep the reply to the point and short")


st.title("Maven-Bot")


user_input = st.text_input("You:", key="user_input")


# def add_to_history(user_msg, bot_msg):
#     if "history" not in st.session_state:
#         st.session_state.history = []
#     st.session_state.history.append({"user": user_msg, "bot": bot_msg})


if st.button("Send", key="send_button"):
    if user_input.strip():

        response = chat.send_message(user_input + " " + instruction)
        

        st.text_area("Bot:", response.text, height=200)
        

        # add_to_history(user_input, response.text)


# if "history" in st.session_state:
#     st.subheader("Conversation History")
#     for msg in st.session_state.history:
#         st.write(f"You: {msg['user']}")
#         st.write(f"Bot: {msg['bot']}")