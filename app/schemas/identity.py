from pydantic import BaseModel
from typing import List, Optional

class IdentityInfo(BaseModel):
    patient_name: Optional[str] = None
    date_of_birth: Optional[str] = None
    policy_number: Optional[str]= None
    id_number: Optional[str]= None
    