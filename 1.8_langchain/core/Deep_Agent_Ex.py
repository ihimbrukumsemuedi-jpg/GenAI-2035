import os 

from dotenv import load_dotenv
load_dotenv()

from langchain_tavily import TavilySearch
from langchain_core.tools import tool
from langchain.chat_models import init_chat_model

search_calls = 0


@tool
def research_search(query: str, max_results: int = 1, topic: str = "general") -> str:
    """Search the web for research information.
    
    Args:
        query: The search query.
        max_results: Number of results to return (default 1).
        topic: Category filter - one of "general", "news", or "finance".
    """
    global search_calls
    if search_calls >= 1:
        return "Search limit reached. Use the first search results and write the summary."
    search_calls += 1
    search = TavilySearch(max_results=max_results, topic=topic)
    results = search.invoke(query)
    return str(results)[:1500]

@tool
def open_file(file_path: str = "", content: str = "") -> str:
    """Compatibility response for models that request an open-file tool."""
    if not file_path:
        return "No file path was supplied. Continue with the available tools."
    return content or f"File '{file_path}' has no supplied content. Continue with the available tools."



from deepagents import (
    GeneralPurposeSubagentProfile,
    HarnessProfile,
    create_deep_agent,
    register_harness_profile,
)        

MODEL_NAME = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")

register_harness_profile(
    f"groq:{MODEL_NAME}",
    HarnessProfile(
        excluded_tools=frozenset(
            {"ls", "read_file", "edit_file", "delete", "glob", "grep", "execute", "task"}
        ),
        general_purpose_subagent=GeneralPurposeSubagentProfile(enabled=False),
    ),
)

model= init_chat_model(f"groq:{MODEL_NAME}, max_tokens=768")

RESEARCHER_PROMPT = """Use research_search exactly once . Then write one cited summary
under 150 words with write_file and stop. Do not make more searches or add details.
Use only the returned facts and avoid speculation."""
agent = create_deep_agent(
    model=model,
    tools=[research_search, open_file],
    system_prompt=RESEARCHER_PROMPT,
)

if __name__ == "__main__":
    for chunk in agent.stream(
        {"messages": [{"role": "user", "content": "Research SMR companies, requlatory status, and expect"}]},
        stream_mode=RESEARCHER_PROMPT,
    ):
        todos = chunk.get("todos", [])
        if todos:
            print("Current todo state:")
            for t in todos:
                print(f" [{t['status']}] {t['content']}")
        if chunk.get("messages"):
            last = chunk["messages"][-1]
            if hasattr(last, "content") and last.content:
                print("Agent:", last.content[:200])        

