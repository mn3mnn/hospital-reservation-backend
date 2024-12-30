from typing import List

from fastapi import APIRouter, Depends
from app.services.reservations import ReservationService
from app.models.schemas.reservations import ReservationIn, ReservationOut, SessionTypeOut, SessionTypeIn
from app.core.dependencies import get_reservation_service

router = APIRouter(prefix="/reservations", tags=["reservations"])

@router.get("/", response_model=ReservationOut)
async def get_reservations(service: ReservationService = Depends(get_reservation_service)):
    """
    Get all reservations
    """
    return await service.get_reservations()


@router.get("/sessions", response_model=List[SessionTypeOut])
async def get_sessions(service: ReservationService = Depends(get_reservation_service)):
    """
    Get all reservations
    """
    return await service.get_sessions()

@router.post("/sessions", response_model=SessionTypeOut)
async def create_session(session: SessionTypeIn, service: ReservationService = Depends(get_reservation_service)):
    """
    Get all reservations
    """
    return await service.create_session(session)



@router.get("/{reservation_id}", response_model=ReservationOut)
async def get_reservation_by_id(reservation_id: int, service: ReservationService = Depends(get_reservation_service)):
    """
    Get reservation by id
    """
    return await service.get_reservation_by_id(reservation_id)

@router.post("/", response_model=ReservationOut)
async def create_reservation(reservation: ReservationIn, service: ReservationService = Depends(get_reservation_service)):
    """
    Create a new reservation
    """
    return await service.create_reservation(reservation)

@router.put("/{reservation_id}", response_model=ReservationOut)
async def update_reservation(reservation_id: int, reservation: ReservationIn, service: ReservationService = Depends(get_reservation_service)):
    """
    Update a reservation
    """
    return await service.update_reservation(reservation_id, reservation)

@router.delete("/{reservation_id}")
async def delete_reservation(reservation_id: int, service: ReservationService = Depends(get_reservation_service)):
    """
    Delete a reservation
    """
    return await service.delete_reservation(reservation_id)

@router.post("/{reservation_id}/confirm", response_model=ReservationOut)
async def confirm_reservation(reservation_id: int, service: ReservationService = Depends(get_reservation_service)):
    """
    confirm a new reservation
    """
    return await service.confirm_reservation(reservation_id)

