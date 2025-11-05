from http.client import responses

import requests
import streamlit as st

def get_model1_response(input_text):
    responses = requests.post("http://127.0.0.1:8000/python/invoke",
                              json={'input': {"topic": input_text}})
    return responses.json()['output']


def get_model2_response(input_text):
    responses = requests.post("http://127.0.0.1:8000/cpp/invoke",
                              json={'input': {"topic": input_text}})
    return responses.json()['output']

st.title("LAngchain Demo With Ollama API")
input_text1 = st.text_input("Write a topic on which you want code in Python")
input_text2 = st.text_input("Write a topic on which you want code in C++")

if input_text1:
    st.write(get_model1_response(input_text1))

if input_text2:
    st.write(get_model1_response(input_text2))

