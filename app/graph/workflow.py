from langgraph.graph  import StateGraph
from app.schemas.state import ClaimState
from app.agents.segregator import segregator_node
from app.agents.id_agent import id_agent_node
from app.agents.discharge_agent import discharge_agent_node
from app.agents.bill_agent import bill_agent_node
from app.services.aggregator import aggregator_node


def build_workflow():
    workflow = StateGraph(ClaimState)

    workflow.add_node("segregator", segregator_node)
    workflow.add_node("id_agent", id_agent_node)
    workflow.add_node("discharge_agent", discharge_agent_node)
    workflow.add_node("bill_agent", bill_agent_node)
    workflow.add_node("aggregator", aggregator_node)

    workflow.set_entry_point("segregator")

    workflow.add_edge("segregator", "id_agent")
    workflow.add_edge("segregator", "discharge_agent")
    workflow.add_edge("segregator", "bill_agent")


    workflow.add_edge("bill_agent", "aggregator")

    workflow.set_finish_point("aggregator")

    return workflow.compile()



async def run_claim_workflow(claim_id: str, pages: list[str]):
    workflow = build_workflow()

    initial_state = {
        "claim_id": claim_id,
        "pages": pages,
        "segregated_pages": {},
        "identity_data": None,
        "discharge_data": None,
        "bill_data": None,
        "final_output": None
    }

    result = await workflow.ainvoke(initial_state)
    return result['final_output']


