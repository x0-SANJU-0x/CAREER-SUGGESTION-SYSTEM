import streamlit as st
import json
from streamlit_lottie import st_lottie
import requests
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain import PromptTemplate, HuggingFaceHub, LLMChain
from dotenv import load_dotenv
st.set_page_config(
    page_title="AI BASED CAREER GUIDANCE",
    page_icon="👋",
    )


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_hello = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_M9p23l.json")
st.title("Made with ❤️ by EdXperts")

st_lottie(
        lottie_hello,
        speed=1,
        reverse=False,
        loop=True,
        quality="low", # medium ; high
        height=None,
        width=None,
        key=None,
    )

#im = Image.open(r"C:\Users\sanch\OneDrive\Desktop\multipage\a.jpg") 
#st.sidebar.image(im,caption='main')
st.sidebar.success("Select a page above")