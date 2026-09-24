import asyncio

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
# load_mcp_tools function is responsible for taking the tools which are exposed through the MCP server 
# and transform it into a Langchain tool so we can use them into the LangGraph/LangChain agent.
from langchain_mcp_adapters.tools import load_mcp_tools
# from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
# ClientSession is responsible for MCP server communication, every client connects to an MCP server via a session.
# StdioServerParameters is a pydantic class which has the fields of commands and args which represent how to run the MCP server, 
# so the client needs to know how to run the MCP server whether to run with Python, Nodejs, Docker and so on.
from mcp import ClientSession, StdioServerParameters
# stdio_client It's gonna communicate to the MCP server through the transport of the standard input/output.
from mcp.client.stdio import stdio_client

load_dotenv()

llm = ChatOllama(temperature=0, model="qwen3:8b")


#### Note: The file main-updated-version.py is the up-to-date version of this code. ####


stdio_server_params = StdioServerParameters(
    command = "python", # It means that the MCP server(math_server.py) we intend to run is implemented in Python.
    args = ["/Users/ahmedmamdouh/Desktop/ai-agents/udemy/mcp-crash-course/servers/math_server.py"], # The path to the MCP server we need to run.
    # We don't need to define 'transport' here as the StdioServerParameters class means the transport is stdio.
)

async def main():
    async with stdio_client(stdio_server_params) as (read, write):
        async with ClientSession(read_stream=read, write_stream=write) as session:
            await session.initialize()
           
            print("session initialized")
            
            # load_mcp_tools is gonna Load all available MCP tools and convert them to LangChain tools.
            tools = await load_mcp_tools(session)
            
            print(tools)

            agent = create_agent(llm, tools)

            result = await agent.ainvoke(
                {"messages": [HumanMessage(content="What is 54 + 2 * 3?")]}
            )

            print(result["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
