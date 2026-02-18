from app.core.llm import get_llm
from app.schemas.segregator import BatchClassification
from app.schemas.state import ClaimState
from typing import Dict, List


llm = get_llm()


async def segregator_node(state: ClaimState) -> ClaimState:
    pages = state["pages"]

    # Prepare combined input
    combined_text = ""
    for index, page_text in enumerate(pages):
        combined_text += f"\n\nPage {index}:\n{page_text}\n"

    prompt = f"""
                You are a medical document classifier.

                Classify EACH page below into exactly one of the following categories:

                - claim_forms
                - cheque_or_bank_details
                - identity_document
                - itemized_bill
                - discharge_summary
                - prescription
                - investigation_report
                - cash_receipt
                - other

                Return structured output containing:
                page_number and document_type for each page.

                Pages:
                {combined_text}
                """

    structured_llm = llm.with_structured_output(BatchClassification)

    result = await structured_llm.ainvoke(prompt)

    segregated: Dict[str, List[str]] = {}

    for item in result.pages:
        page_number = item.page_number
        doc_type = item.document_type

        if doc_type not in segregated:
            segregated[doc_type] = []

        segregated[doc_type].append(pages[page_number])

    return {"segregated_pages": segregated}
