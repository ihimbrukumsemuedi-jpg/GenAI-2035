from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful, concise tutor"),
    MessagesPlaceholder("history"),
    ("human", "{input}"),
])