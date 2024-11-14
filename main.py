# simplest form of state in LangGraph
# 1. Basic State Definition
from typing import TypedDict

class BasicState(TypedDict):
    count: int
  
#  2. Complex State Structures or sophisticated state structures
# LangGraph allows us to create complex states that can hold various types of information:
from typing import TypedDict, Annotated
from langchain_core.messages import HumanMessage, AIMessage

class ComplexState(TypedDict):
    count: int
    messages: Annotated[list[HumanMessage | AIMessage], add_messages]
