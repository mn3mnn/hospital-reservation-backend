import json
from typing import List, Sequence, Optional

from sqlalchemy import select
from app.models.schemas.doctors import DoctorIn, DoctorOut, DoctorSchedule, DoctorBranchOut, DoctorBranchIn
from app.repos.base import BaseRepository
from app.models.db.doctors import Doctor, DoctorBranch

class DoctorRepository(BaseRepository):
    async def get_doctors(self) -> List[DoctorOut]:
        stmt = select(Doctor)
        result = await self.db.execute(stmt)
        doctors = result.scalars().all()
        return [DoctorOut.model_validate(doctor) for doctor in doctors]

    async def get_doctor_by_id(self, doctor_id: int) -> Optional[DoctorOut]:
        doctor = await self.get_by_id(Doctor, doctor_id)
        if doctor:
            return DoctorOut.model_validate(doctor)
        return None

    async def create_doctor(self, doctor: DoctorIn) -> Doctor:
        doctor_db = Doctor(**doctor.model_dump(exclude={"doctor_branches"}))
        self.db.add(doctor_db)
        await self.db.commit()
        await self.db.refresh(doctor_db)

        if doctor.doctor_branches:
            await self.create_doctor_branch_schedule(doctor_db.id, doctor.doctor_branches)

        return doctor_db

    async def update_doctor(self, doctor_id: int, doctor: DoctorIn) -> DoctorOut:
        doctor_db = await self.get_by_id(Doctor, doctor_id)
        if not doctor_db:
            return None

        for field, value in doctor.model_dump(exclude={"doctor_branches"}).items():
            setattr(doctor_db, field, value)

        await self.db.commit()
        await self.db.refresh(doctor_db)
        return DoctorOut.model_validate(doctor_db)

    async def create_doctor_branch_schedule(self, doctor_id: int, branches: List[DoctorBranchIn]) -> None:
        for branch in branches:
            branch_data = DoctorBranch(
                doctor_id=doctor_id,
                branch_id=branch.branch_id,
                schedule=json.dumps(branch.schedule.model_dump())
            )
            self.db.add(branch_data)
        await self.db.commit()

    async def get_doctor_schedule(self, doctor_id: int) -> List[DoctorBranchOut]:
        stmt = select(DoctorBranch).where(DoctorBranch.doctor_id == doctor_id)
        result = await self.db.execute(stmt)
        branches = result.scalars().all()
        return [DoctorBranchOut(
            doctor_id=branch.doctor_id,
            branch_id=branch.branch_id,
            schedule=DoctorSchedule.model_validate(json.loads(branch.schedule))
        ) for branch in branches]

