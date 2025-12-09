import streamlit as st
import langchain_helper
import os
from langchain_google_genai import ChatGoogleGenerativeAI
import getpass
from sect_key import GEMINI_API_KEY


st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine",("Indian", "Italian", "Mexican", "Arabic", "American"))


if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'])
    menu_items = response['menu_items'].split(",")
    st.write("*****Menu Items*****")
    for item in menu_items:
        st.write("-", item)



