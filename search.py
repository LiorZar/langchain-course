from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool
from langchain.messages import HumanMessage
from tavily import TavilyClient
from langchain_tavily import TavilySearch

load_dotenv()

tavily = TavilyClient()

@tool
def search(query: str) -> str:
    """
    Tool that searchs over the internet using Tavily.
    Args:
        query (str): The search query.
    Returns:
        str: The search results.
    """
    print(f"Performing search for query: {query}")
    # Simulate a search operation (replace with actual search logic)
    return tavily.search(query=query, max_results=3)

llm = ChatOpenAI(model="gpt-5")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-course!")
    
    result = agent.invoke({"messages": [HumanMessage(content="search for 3 casino game studios with a GDK")]})
    print(result)   

if __name__ == "__main__":
    main()
