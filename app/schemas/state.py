from typing import TypedDict, Dict, List, Optional

class ClaimState(TypedDict):
    claim_id: str
    pages: List[str]

    segregated_pages : Dict[str, List[str]]

    identity_data: Optional[dict]
    discharge_data: Optional[dict]
    bill_data: Optional[dict]

    final_output: Optional[dict]



