from typing import List

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location: str) -> str:
    """Get weather for location."""

    return "Hot as hell"

if __name__ == "__main__":
    mcp.run(transport="sse") # This is the SSE transport, we will communicate with this MCP server(wather server) through SSE, it's a server-to-client communication.
