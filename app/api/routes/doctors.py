from typing import List

from fastapi import APIRouter, Depends
from app.services.doctors import DoctorService
from app.models.schemas.doctors import DoctorOut, DoctorIn, DoctorScheduleOut
from app.core.dependencies import get_doctor_service

router = APIRouter(prefix="/doctors", tags=["doctors"])


@router.get("/", response_model=List[DoctorOut])
async def get_doctors(service: DoctorService = Depends(get_doctor_service)):
    """
    Get all doctors
    """
    return await service.get_doctors()

@router.get("/{doctor_id}", response_model=DoctorOut)
async def get_doctor_by_id(doctor_id: int, service: DoctorService = Depends(get_doctor_service)):
    """
    Get doctor by id
    """
    return await service.get_doctor_by_id(doctor_id)

@router.get("/{doctor_id}/schedule", response_model=List[DoctorScheduleOut])
async def get_doctor_schedule(doctor_id: int, service: DoctorService = Depends(get_doctor_service)):
    """
    Get doctor by id
    """
    return await service.get_doctor_schedule(doctor_id)


@router.post("/", response_model=DoctorOut)
async def create_doctor(doctor: DoctorIn, service: DoctorService = Depends(get_doctor_service)):
    """
    Create a new doctor
    """
    return await service.create_doctor(doctor)

@router.put("/{doctor_id}", response_model=DoctorOut)
async def update_doctor(doctor_id: int, doctor: DoctorIn, service: DoctorService = Depends(get_doctor_service)):
    """
    Update a doctor
    """
    return await service.update_doctor(doctor_id, doctor)

@router.delete("/{doctor_id}")
async def delete_doctor(doctor_id: int, service: DoctorService = Depends(get_doctor_service)):
    """
    Delete a doctor
    """
    return await service.delete_doctor(doctor_id)


