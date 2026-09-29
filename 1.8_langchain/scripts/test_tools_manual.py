from core.tools import tools_by_name


def run_tool(tool_name, arguments):
    """Run a tool from the tools_by_name dictionary."""
    tool = tools_by_name[tool_name]
    return tool.invoke(arguments)


def tool_calling_loop(question, llm):
    """
    Run the LLM/tool-calling loop for a natural-language question.
    """
    from langchain_core.messages import HumanMessage, ToolMessage

    messages = [HumanMessage(content=question)]

    while True:
        response = llm.invoke(messages)

        print("\nMODEL RESPONSE:")
        print(response)

        messages.append(response)

        # No tools required
        if not response.tool_calls:
            print("\nFINAL ANSWER:")
            print(response.content)
            break

        # Execute every tool requested by the model
        for tool_call in response.tool_calls:
            tool_name = tool_call["name"]
            tool_args = tool_call["args"]

            print(f"\nCalling tool: {tool_name}")
            print(f"Arguments: {tool_args}")

            if tool_name not in tools_by_name:
                print(f"Unknown tool: {tool_name}")
                continue

            result = tools_by_name[tool_name].invoke(tool_args)

            print(f"Tool result: {result}")

            messages.append(
                ToolMessage(
                    content=str(result),
                    tool_call_id=tool_call["id"],
                )
            )


def main():
    # Replace this with the LLM/agent you created during the online session.
    #
    # Example:
    #
    # llm = ChatOpenAI(model="...")
    # llm = llm.bind_tools(list(tools_by_name.values()))

    from langchain_openai import ChatOpenAI

    llm = ChatOpenAI()

    llm = llm.bind_tools(list(tools_by_name.values()))

    questions = [
        # Question 1 requires one tool
        "When is module 1.8 due?",

        # Question 2 requires two different tools
        "How many students are in module 1.5 and when is it due?",

        # Question 3 requires two different tools
        "Can I take module 1.8 if I completed module 1.5, "
        "and what sessions are scheduled in room A101?",
    ]

    for question in questions:
        print("\n" + "=" * 60)
        print(f"QUESTION: {question}")
        print("=" * 60)

        tool_calling_loop(question, llm)

    # Test a question that requires NO tool
    print("\n" + "=" * 60)
    print("NO-TOOL TEST")
    print("=" * 60)

    no_tool_question = "What is a neural network?"

    tool_calling_loop(no_tool_question, llm)


if __name__ == "__main__":
    main()