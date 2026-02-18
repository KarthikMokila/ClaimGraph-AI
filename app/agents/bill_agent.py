from app.core.llm import get_llm
from app.schemas.bill import ItemizedBill
from app.schemas.state import ClaimState


llm = get_llm()
async def bill_agent_node(state: ClaimState) -> ClaimState:
    segregated = state.get("segregated_pages", {})

    bill_pages = segregated.get("itemized_bill", [])


    if not bill_pages:
        state["itemized_bill"] = None
        return state
    
    combined_text = "\n\n".join(bill_pages)


    prompt = f"""
                You are a financial document extraction system.
                Extract all the bill line items from the document.

                for each item extract:
                - description
                - amount (numeric only)

                Return structured output

                Document content:
                {combined_text}

            """
    
    structured_llm = llm.with_structured_output(ItemizedBill)

    result = structured_llm.invoke(prompt)

    items = result.items

    total_amount = sum(
        item.amount for item in items if item.amount is not None
    )

    state["bill_data"] = {
        "items": [item.model_dump() for item in items],
        "total_amount": total_amount
    }

    return state


