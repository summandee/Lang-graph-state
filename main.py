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

# 4. Simple Graphs with State
 ## Now that we understand the basics of state and how to modify it, let’s see how we can use state in a LangGraph:
from langgraph.graph import StateGraph, END

def create_simple_graph():
    workflow = StateGraph(BasicState)
    
    def increment_node(state: BasicState):
        return {"count": state["count"] + 1}
    
    workflow.add_node("increment", increment_node)
    workflow.set_entry_point("increment")
    workflow.add_edge("increment", END)
    
    return workflow.compile()

### This simple graph demonstrates the fundamental structure of a LangGraph workflow:

### 1. We create a StateGraph using our BasicState.
2. We define a node function (increment_node) that modifies the state.
3. We add this node to our graph and set it as the entry point.
4. We create an edge from our node to the END of the graph.
5. Finally, we compile our workflow.
6. While this graph may seem basic, it serves as the foundation for more complex workflows.
