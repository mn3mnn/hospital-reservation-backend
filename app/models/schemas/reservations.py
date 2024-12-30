from pydantic import Field, field_validator
from typing import Optional, Dict, Any, List
from app.models.schemas.base import BaseSchemaModel

class ReservationOut(BaseSchemaModel):
    id: int
    doctor_id: int
    patient_id: int
    branch_id: int
    session_id: int

    has_shock_therapy: bool
    week_day: str
    time: str
    status: str


class ReservationIn(BaseSchemaModel):
    doctor_id: int = Field(...)
    patient_id: int = Field(...)
    session_id: int = Field(...)
    branch_id: int = Field(...)

    week_day: str = Field(...)
    time: str = Field(...)

    has_shock_therapy: bool = Field(...)
