from openai import OpenAI
import google.generativeai as genai

import streamlit as st


f = open("open-ai-key.txt")
key = f.read()
genai.configure(api_key=key)

model=genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    system_instruction="You are a Developer who debug a python codes and give optmized version of code  ")

st.header("GenAI App : Expert Python Code Debugger🧑‍💻")

st.text("Who helps you with your code journey")

st.subheader("Enter Your Python Codes and Fix the Bugs🥳")



prompt = st.text_area("Enter your python Code here :")


if st.button("DEBUG🐞") == True:
    

    response = model.generate_content(prompt)

    st.header("Review of Your Code🧐")

    st.write(response.text)
    