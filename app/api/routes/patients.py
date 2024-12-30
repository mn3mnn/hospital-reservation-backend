from typing import List

from fastapi import APIRouter, Depends
from app.services.patients import PatientService
from app.models.schemas.patients import PatientIn, PatientOut
from app.core.dependencies import get_patient_service

router = APIRouter(prefix="/patients", tags=["patients"])


@router.get("/", response_model=List[PatientOut])
async def get_patients(service: PatientService = Depends(get_patient_service)):
    """
    Get all governments in Egypt without their geometries.
    """
    return await service.get_patients()

@router.get("/{patient_id}", response_model=PatientOut)
async def get_patient_by_id(patient_id: int, service: PatientService = Depends(get_patient_service)):
    """
    Get government by id
    """
    return await service.get_patient_by_id(patient_id)

@router.post("/", response_model=PatientOut)
async def create_patient(patient: PatientIn, service: PatientService = Depends(get_patient_service)):
    """
    Create a new government
    """
    return await service.create_patient(patient)

@router.put("/{patient_id}", response_model=PatientOut)
async def update_patient(patient_id: int, patient: PatientIn, service: PatientService = Depends(get_patient_service)):
    """
    Update a government
    """
    return await service.update_patient(patient_id, patient)

@router.delete("/{patient_id}")
async def delete_patient(patient_id: int, service: PatientService = Depends(get_patient_service)):
    """
    Delete a government
    """
    return await service.delete_patient(patient_id)
