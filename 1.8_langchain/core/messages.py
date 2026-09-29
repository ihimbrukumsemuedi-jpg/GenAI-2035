from langchain.messages import SystemMessage, HumanMessage, AIMessage,ToolMessage
from .models import create_model

model=create_model()


messages = [
    SystemMessage("You are a helpful assistant."),
    HumanMessage("Hello, who are you?"),
    AIMessage("I am an AI created by OpenAI. How can I help you today?"),
    HumanMessage("I'd like to learn more about LangChain.")
]


response=model.invoke(messages)
print(response)