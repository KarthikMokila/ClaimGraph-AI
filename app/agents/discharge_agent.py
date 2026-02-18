from app.core.llm import get_llm
from app.schemas.discharge import DischargeSummary
from app.schemas.state import ClaimState



llm = get_llm()


async def discharge_agent_node(state: ClaimState) -> ClaimState:
    segregated = state.get("segregated_pages", {})

    discharge_pages = segregated.get("discharge_summary", [])

    if not discharge_pages:
        return {"discharge_data": None}
    
    combined_text = "\n\n".join(discharge_pages)

    prompt =f"""

            You are an information extraction system.
            Extract the following information from the provided text:
            - Patient Name
            - Date of Birth
            - Policy Number
            - ID Number
            - Diagnosis
            - Treatment Given
            - Discharge Date
            - Physician Name

            If any of the above information is not present, return null for that field.

            Document Content:
            {combined_text}


                    """

    structured_llm = llm.with_structured_output(DischargeSummary)
    result = await structured_llm.ainvoke(prompt)

    return {"discharge_data": result.model_dump()}