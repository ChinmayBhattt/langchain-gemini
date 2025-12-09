import os
from langchain_google_genai import ChatGoogleGenerativeAI
os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.6)

def generate_restaurant_name_and_items(cuisine):
    return{
      'restaurant_name': 'Curry Delight',
      'menu_items': 'samosa, paneer tikka, kachori'

    }




