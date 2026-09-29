from langchain.agents import create_agent
from core.tools import get_module_deadline, count_students_in_module, check_prerequisite, get_room_schedule

agent = create_agent(
    model=model,
    tools=[get_module_deadline, count_students_in_module, check_prerequisite, get_room_schedule]
    system_prompt="You are an operations assistant for a coding bootcamp. Use tools to answer factual question accurately."
)

#result = agent.invoke({"messages": [{"role": "user", "content": "When is the CNN module due?"}]})
#print(result["message"][-1].content)

for step in agent.stream({"message": [{"role": "user", "content": "How many students are in ANN?"}]})
  print(step)  # each step is a dict keyed by the node that just ran