from pydantic import Field, field_validator
from typing import Optional, Dict, Any, List
from app.models.schemas.base import BaseSchemaModel
from datetime import time


class TimeSchedule(BaseSchemaModel):
    start_time: time
    end_time: time

    class Config:
        json_encoders = {
            time: lambda v: v.strftime('%H:%M:%S')  # Convert time to string
        }



class DoctorSchedule(BaseSchemaModel):
    monday: Optional[TimeSchedule] = None
    tuesday: Optional[TimeSchedule] = None
    wednesday: Optional[TimeSchedule] = None
    thursday: Optional[TimeSchedule] = None
    friday: Optional[TimeSchedule] = None
    saturday: Optional[TimeSchedule] = None
    sunday: Optional[TimeSchedule] = None

    class Config:
        json_encoders = {
            time: lambda v: v.strftime('%H:%M:%S')  # Convert time to string
        }




class DoctorOut(BaseSchemaModel):
    id: int
    first_name: str
    last_name: str

class DoctorBranchIn(BaseSchemaModel):
    branch_id: int
    schedule: DoctorSchedule

    class Config:
        json_encoders = {
            time: lambda v: v.strftime('%H:%M:%S')  # Convert time to string
        }


class DoctorScheduleOut(BaseSchemaModel):
    branch_id: int
    schedule: DoctorSchedule

class DoctorIn(BaseSchemaModel):
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: str = Field(...)
    # password: str = Field(...)
    phone: str = Field(...)

    doctor_branches: List[DoctorBranchIn] = Field(...)

