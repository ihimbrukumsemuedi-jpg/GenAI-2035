# We are going to be doing our tool call here:
# we need to import tools from utils

from utils.tools import get_module_deadline, count_students_in_module, check_prerequisite, get_room_schedule
from .models import create_model
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

tools=[get_module_deadline, count_students_in_module, check_prerequisite, get_room_schedule]

llm=create_model().bind_tools(tools)
#print(llm)
tools_by_name={t.name: t for t in tools}

# we are going t be constructing a message list [HumanMessage, AiMessage, SystemMessage, ToolMessage]

messages=[HumanMessage("How many students are in the CNN module and what what is the dealine and when is it schedule")]
ai_response=llm.invoke(messages)
print(f"Ai response is: {ai_response}")

# tool_calls=[{'name': 'count_students_in_module', 'arg': {'module_name': 'CNN module'},'get_module_deadline', 'args': {'module_name': 'CNN module'}, 'id': 'f3c8d007-a1ef-487e-'}]

messages.append(ai_response)
#for us to be able to pass this tool info our llm, we need to run a loop:
for tool in ai_response.tool_calls:
    tool_fn=tools_by_name[tool["name"]]
    result=tool_fn.invoke(tool["args"])
    print(f"tool result is: {result}")
    messages.append(ToolMessage(content=result, tool_call_id=tool["id"]))

final=llm.invoke(messages)
print(final.content)