from pydantic import Field, field_validator
from typing import Optional, Dict, Any, List
from app.models.schemas.base import BaseSchemaModel

class PatientOut(BaseSchemaModel):
    id: int
    name: str
    email: str
    phone_number: str

class PatientIn(BaseSchemaModel):
    name: str = Field(...)
    email: str = Field(...)
    phone_number: str = Field(...)
