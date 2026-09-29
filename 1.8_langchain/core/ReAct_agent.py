from langgraph.prebuilt import create_react_agent
from core.models import create_model
from tools.image_gen import generate_image
from tools.search import web_search
from tools.voice import text_to_speech

SYSTEM_PROMPT = """You are a helpful multimodel assistant with tools for image analysis,
image generation, web search, and text_to_speech.

Only call a tool when the request genuinely needs it:
- analyze_image: only when an image has been uploaded and the user is asking about it:
- generate_image: only when the user explicity asks you to create, draw, or visualize something.
- web_search: only for current events, recent news, or facts you wouldn't reliably know.
- text_to_speech: only when the user explicity asks fpr audio or spoken output.

for everything else, greetings, general knowledge, explanations, conversation, answer dire
without calling any tool.
"""

def build_multimodel_agent():
    model = create_model()
    tools = [generate_image, web_search, text_to_speech]
    return create_react_agent(model, tools, prompt=SYSTEM_PROMPT)
ReAct_agent = build_multimodel_agent()




result = ReAct_agent.invoke({'message': [('user', 'generate an image of yamal')]})


# web search
#result =ReAct_agent.invoke({'message': [('user', 'give me latest news on spaceX')]})
print(result['message'][-1].content)

