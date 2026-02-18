from pydantic import BaseModel
from typing import Optional, List


class DischargeSummary(BaseModel):
    patient_name: Optional[str] = None
    date_of_birth: Optional[str] = None
    policy_number: Optional[str]= None
    id_number: Optional[str]= None
    diagnosis: Optional[str] = None
    treatment_given: Optional[str] = None
    discharge_date: Optional[str] = None
    physician_name: Optional[str] = None




