import json
from typing import List, Sequence, Optional

from sqlalchemy import select
from app.models.schemas.doctors import DoctorIn, DoctorOut, DoctorSchedule, DoctorScheduleOut, DoctorBranchIn
from app.repos.base import BaseRepository
from app.models.db.doctors import Doctor, DoctorBranch

class DoctorRepository(BaseRepository):
    async def get_doctors(self) -> List[DoctorOut]:
        stmt = select(Doctor)
        result = await self.db.execute(stmt)
        doctors = result.scalars().all()
        return [DoctorOut(**doctor.__dict__) for doctor in doctors]

    async def get_doctor_by_id(self, doctor_id: int) -> Optional[DoctorOut]:
        doctor = await self.get_by_id(Doctor, doctor_id)
        if doctor:
            return DoctorOut.model_validate(doctor)
        return None

    async def create_doctor(self, doctor: DoctorIn) -> Doctor:
        async with self.db.begin():  # Start a single transaction block
            # Create the doctor object from the input model (excluding doctor_branches for now)
            doctor_db = Doctor(**doctor.model_dump(exclude={"doctor_branches"}))

            # Add doctor to the session
            self.db.add(doctor_db)

            # Commit changes to the doctor
            await self.db.flush()  # Flush to generate the doctor_db.id

            # If doctor_branches are provided, create the doctor_branches
            if doctor.doctor_branches:
                await self.create_doctor_branch_schedule(doctor_db.id, doctor.doctor_branches)

            # Refresh the doctor object to reflect any changes made during the transaction
            await self.db.refresh(doctor_db)

        # Return the created doctor object
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
                schedule=branch.schedule.model_dump_json()
            )
            self.db.add(branch_data)

    async def get_doctor_schedule(self, doctor_id: int) -> List[DoctorScheduleOut]:
        stmt = select(DoctorBranch).where(DoctorBranch.doctor_id == doctor_id)
        result = await self.db.execute(stmt)
        branches = result.scalars().all()
        return [DoctorScheduleOut(
            branch_id=branch.branch_id,
            schedule=DoctorSchedule.model_validate(json.loads(branch.schedule))
        ) for branch in branches]

