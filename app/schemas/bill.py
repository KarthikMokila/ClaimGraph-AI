from pydantic import BaseModel
from typing import List, Optional


class BillItem(BaseModel):
    description: Optional[str]= None
    amount: Optional[float] = None

class ItemizedBill(BaseModel):
    items: List[BillItem]


