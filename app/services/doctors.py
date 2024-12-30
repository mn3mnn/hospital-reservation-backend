from typing import List, Sequence

from app.models.schemas.doctors import DoctorIn, DoctorOut, DoctorScheduleOut
from app.repos.doctors import DoctorRepository

class DoctorService:
    def __init__(self, repo: DoctorRepository):
        self.repo = repo

    async def get_doctors(self) -> List[DoctorOut]:
        doctors = await self.repo.get_doctors()
        return [DoctorOut.model_validate(doctor) for doctor in doctors]

    async def get_doctor_by_id(self, doctor_id: int) -> DoctorOut:
        doctor = await self.repo.get_doctor_by_id(doctor_id)
        return DoctorOut.model_validate(doctor) if doctor else None

    async def get_doctor_schedule(self, doctor_id: int) -> List[DoctorScheduleOut]:
        schedule_outs = await self.repo.get_doctor_schedule(doctor_id)
        return [DoctorScheduleOut.model_validate(s) for s in schedule_outs]

    async def create_doctor(self, doctor: DoctorIn) -> DoctorOut:
        created_doctor = await self.repo.create_doctor(doctor)
        return DoctorOut(**created_doctor.__dict__)

    async def update_doctor(self, doctor_id: int, doctor: DoctorIn) -> DoctorOut:
        updated_doctor = await self.repo.update_doctor(doctor_id, doctor)
        return DoctorOut.model_validate(updated_doctor) if updated_doctor else None

    async def delete_doctor(self, doctor_id: int) -> None:
        await self.repo.delete_doctor(doctor_id)
