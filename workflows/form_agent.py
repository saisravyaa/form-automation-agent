from langgraph.graph import StateGraph
from tools.api_ninja import get_address_data

# Node function
def fetch_address(state: dict) -> dict:
    address = state.get("address")
    print("Fetched address from state:", address)
    address_info = get_address_data(address)
    state["address_info"] = address_info
    return state

def create_form_agent():
    graph = StateGraph(dict)  # Use plain dict
    graph.add_node("FetchAddress", fetch_address)
    graph.set_entry_point("FetchAddress")
    graph.set_finish_point("FetchAddress")
    return graph.compile()
