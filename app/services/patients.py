from typing import List, Sequence

from app.models.schemas.patients import PatientOut, PatientIn
from app.repos.patients import PatientRepository


class PatientService:
    def __init__(self, repo: PatientRepository):
        self.repo = repo

    async def get_patients(self) -> List[PatientOut]:
        return await self.repo.get_patients()

    async def get_patient_by_id(self, patient_id: int) -> PatientOut:
        patient = await self.repo.get_patient_by_id(patient_id)
        return PatientOut.model_validate(patient) if patient else None

    async def create_patient(self, patient: PatientIn) -> PatientOut:
        created_patient = await self.repo.create_patient(patient)
        return PatientOut(**created_patient.__dict__)

    async def update_patient(self, patient_id: int, patient: PatientIn) -> PatientOut:
        updated_patient = await self.repo.update_patient(patient_id, patient)
        return PatientOut.model_validate(updated_patient) if updated_patient else None

    async def delete_patient(self, patient_id: int) -> None:
        await self.repo.delete_patient(patient_id)