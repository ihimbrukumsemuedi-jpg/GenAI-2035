from .models import create_model
from langchain_core.prompts import ChatPromptTemplate

announcement_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that summarizes announcements in a concise manner."),
    ("human", """Create an announcement for the following information: Audience: {audience}, Tone: {tone}, Announcement_details: {announcement_details} 
    Make sure to keep the announcement concise and clear, and use a tone that is appropriate for the audience.""")
])
