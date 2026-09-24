import asyncio

from dotenv import load_dotenv
# from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_ollama import ChatOllama

load_dotenv()

llm = ChatOllama(temperature=0, model="qwen3:8b")


#### Note: # You should run the server first before running this file: uv run servers/weather_server.py & uv run servers/math_server.py ####

async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": [
                    "/Users/ahmedmamdouh/Desktop/ai-agents/udemy/mcp-crash-course/servers/math_server.py"
                ],
                "transport": "stdio", # Each server defined here must include 'transport' with one of: 'stdio', 'sse', 'websocket', 'http'.
            },
            "weather": {
                "url": "http://localhost:8000/sse",
                "transport": "sse", # Each server defined here must include 'transport' with one of: 'stdio', 'sse', 'websocket', 'http'.
            },
        }
    )

    tools = await client.get_tools()

    agent = create_agent(llm, tools)

    # result = await agent.ainvoke({"messages": "What is 2 + 2?"})

    result = await agent.ainvoke(
        {"messages": "What is the weather in San Francisco?"}
    )

    print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
