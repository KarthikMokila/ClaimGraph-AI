from typing import Literal, List
from pydantic import BaseModel

class PageClassification(BaseModel):
    page_number: int
    document_type: Literal[
        "claim_forms",
        "cheque_or_bank_details",
        "identity_document",
        "itemized_bill",
        "discharge_summary",
        "prescription",
        "investigation",
        "cash_reciept",
        "other"
    ] 


class BatchClassification(BaseModel):
    pages: List[PageClassification]