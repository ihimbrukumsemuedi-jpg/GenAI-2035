from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
import os
from config import DEFAULT_MODEL, DEFAULT_TEMPERATURE

load_dotenv()  # Load Google API key from .env file 
# a function a reusable function[ its going to be sude in any file in our project ]

def create_model(model_name:str=DEFAULT_MODEL):
    #this function will return the model as output
    return init_chat_model(model_name, temperature=DEFAULT_TEMPERATURE)
    pass
# create_model()