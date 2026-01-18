from typing import List
from pydantic import BaseModel, Field

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
# from langchain.tools import tool
from langchain.messages import HumanMessage
from tavily import TavilyClient
from langchain_tavily import TavilySearch

load_dotenv()

tavily = TavilyClient()

class Source(BaseModel):
    """Schema for a source used by the agent"""
    
    url:str = Field(..., description="The URL of the source")
    
class AgentResponse(BaseModel):
    """Schema for the agent response"""
    
    answer: str = Field(..., description="The final answer from the agent")
    sources: List[Source] = Field(default_factory=list, description="List of sources used to generate the answer")

llm = ChatOpenAI()
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)

def main():
    print("Hello from langchain-course!")
    
    result = agent.invoke({"messages": [HumanMessage(content="search for 3 casino game studios with a GDK")]})
    print(result)   

if __name__ == "__main__":
    main()
