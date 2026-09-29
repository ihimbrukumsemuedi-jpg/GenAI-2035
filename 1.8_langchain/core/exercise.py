from .models import create_model
from config import QWEN
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


model = create_model(QWEN)
parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ("system", "Give one-paragraph for {topic} and target audience should {audience}"),
    ("human", "{topic}")
])
topic = input("Enter the topic you want to learn about:")
audience = input("Enter the audience level you want:")

chain = prompt | model | parser 
result = chain.invoke({
    "topic": topic,
    "audience": audience
})
print(result)