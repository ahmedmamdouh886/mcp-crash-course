import asyncio

from dotenv import load_dotenv
# from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_ollama import ChatOllama

load_dotenv()

llm = ChatOllama(temperature=0, model="qwen3:8b")


async def main():
    print("Hello Langchain MCP.")


if __name__ == "__main__":
    asyncio.run(main())

