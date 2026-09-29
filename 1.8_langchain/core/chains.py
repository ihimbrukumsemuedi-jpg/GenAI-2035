#from .models import create_model
#from config import QWEN
#from langchain_core.output_parsers import StrOutputParser
#from .prompts import prompt 

#model = create_model()
#parser = StrOutputParser()

#announcement_chain = prompt | model | parser



import streamlit as st
# @st.cache_resources. ----> help store api calls temporarily
from langchain_core.output_parsers import StrOutputParser
from .prompt import chat_prompt
from .models import create_model
parser = StrOutputParser()


@st.cache_resource
def get_chat_chain():
    model=create_model()
    return chat_prompt | model | parser