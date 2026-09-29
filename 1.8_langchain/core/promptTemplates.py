    # get the model in and amke sure it works
from .models import create_model
from config import QWEN
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser



model= create_model(QWEN)
parser=StrOutputParser()


# prompt_template->model->convert_To_String

prompt=ChatPromptTemplate.from_messages([
    ("system", "you are a concise teaching assistant, answer in {max_sentence} sentences"),
    ("human", "{question}")
])
chain=prompt | model | parser
result=chain.invoke({
    "max_sentence": 5,
    "question": "what is the difference between CNN and ANN?"
})
print(result)












# we are going to be using something called:: ChatPromptTemplate to create prompt template
#from langchain_core.prompts import ChatPromptTemplate
# a good example of  prompt template

# describe this {football_player} in one sentence
# given this {data} about this school, answer related question ask by the user

#model = create_model(QWEN)

#prompt_template = ChatPromptTemplate.from_messages(
 #   [
        #system message : a message given to the model in order for it to determine how to respond to the user
        # human message : a message given to the model by the user of the app
#        ("system", "Please in one sentence describe this {football_player} and give a brief history of his career, and also provide a list of his achievements in football."),
 #       ("human", "{question}")
  #  ]
#)

#football_player = input("Enter the name of a football player: ")
#question = input("Enter your question about the football player: ")

#chain = prompt_template | model
#result=chain.invoke({
 #   "football_player": football_player,
  #  "question": question
#})

#print(result)


#prompt_template.invoke(2{
 #   "football_player": "Lionel Messi",
  #  "question"
#})

