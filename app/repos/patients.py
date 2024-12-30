import json
from typing import List, Sequence, Optional

from sqlalchemy import select
from app.models.schemas.patients import PatientIn, PatientOut
from app.repos.base import BaseRepository
from app.models.db.patients import Patient

class PatientRepository(BaseRepository):
    async def get_patients(self) -> List[PatientOut]:
        stmt = select(Patient)
        result = await self.db.execute(stmt)
        patients = result.scalars().all()
        return [PatientOut(**patient.__dict__) for patient in patients]

    async def get_patient_by_id(self, patient_id: int) -> Optional[PatientOut]:
        patient = await self.get_by_id(Patient, patient_id)
        if patient:
            return PatientOut.model_validate(patient)
        return None

    async def create_patient(self, patient: PatientIn) -> Patient:
        patient_db = Patient(**patient.model_dump())
        self.db.add(patient_db)
        await self.db.commit()
        await self.db.refresh(patient_db)
        return patient_db

    async def update_patient(self, patient_id: int, patient: PatientIn) -> PatientOut:
        patient_db = await self.get_by_id(Patient, patient_id)
        if not patient_db:
            return None

        for field, value in patient.model_dump().items():
            setattr(patient_db, field, value)

        await self.db.commit()
        await self.db.refresh(patient_db)
        return PatientOut.model_validate(patient_db)
