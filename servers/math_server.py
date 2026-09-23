from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""

    return a * b

if __name__ == "__main__":
    mcp.run(transport="stdio") # This is the stdio transport, we will communicate with this MCP server(math server) through standard input/output and HTTP request, it's a client-to-server communication.
