from app.schemas.state import ClaimState

async def aggregator_node(state: ClaimState) -> ClaimState:
    final_output = {
        "claim_id": state.get("claim_id"),
        "identity": state.get("identity_data"),
        "discharge_summary": state.get("discharge_data"),
        "bill": state.get("bill_data")
    }
    return {"final_output": final_output}