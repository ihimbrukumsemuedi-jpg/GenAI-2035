from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


chat_prompt=ChatPromptTemplate([
    ("system", "you are a helpful Ai. adopt the following persona and tone throughout the conversation: {persona}"),
    (MessagesPlaceholder("history")),
    ("human", "{input}")
])