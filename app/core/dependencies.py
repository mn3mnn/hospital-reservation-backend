from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.repos.branches import BranchRepository
from app.repos.doctors import DoctorRepository
from app.repos.patients import PatientRepository
from app.repos.reservations import ReservationRepository
from app.services.branches import BranchService

from app.services.doctors import DoctorService
from app.services.patients import PatientService
from app.services.reservations import ReservationService


# DATABASE DEPENDENCIES
from app.core.db import get_db_async


# REPOSITORIES DEPENDENCIES

def get_doctor_repo(db: AsyncSession = Depends(get_db_async)) -> DoctorRepository:
    return DoctorRepository(db=db)

def get_patient_repo(db: AsyncSession = Depends(get_db_async)) -> PatientRepository:
    return PatientRepository(db=db)

def get_reservation_repo(db: AsyncSession = Depends(get_db_async)) -> ReservationRepository:
    return ReservationRepository(db=db)

def get_branch_repo(db: AsyncSession = Depends(get_db_async)) -> BranchRepository:
    return BranchRepository(db=db)



# SERVICES DEPENDENCIES

def get_doctor_service(repo: DoctorRepository = Depends(get_doctor_repo)) -> DoctorService:
    return DoctorService(repo=repo)

def get_patient_service(repo: PatientRepository = Depends(get_patient_repo)) -> PatientService:
    return PatientService(repo=repo)

def get_reservation_service(repo: ReservationRepository = Depends(get_reservation_repo)) -> ReservationService:
    return ReservationService(repo=repo)

def get_branch_service(repo: BranchRepository = Depends(get_branch_repo)) -> BranchService:
    return BranchService(repo=repo)
