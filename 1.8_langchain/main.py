#getting started with langchain(way to talk to llms as a developer as a developer)


# 1 how to connect to llms usning langchain
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()  # Load Google API key from .env file 
model = init_chat_model("groq:qwen/qwen3.6-27b", temperature=0.7) 

#what is temperature? it is a parameter that controls the randomness of the model's output. A higher temperature (e.g., 1.0) will result in more diverse and creative responses, while a lower temperature (e.g., 0.2) will produce more focused and deterministic outputs.
#.invoke(): bassically pass input to a model and get output from it.
# runable()

response = model.invoke("WHO IS JUESUS CHRIST") 
#to print just the text you use
print(response.content)

