from typing import List, Sequence

from app.models.schemas.reservations import ReservationIn, ReservationOut, SessionTypeOut, SessionTypeIn
from app.repos.reservations import ReservationRepository

class ReservationService:
    def __init__(self, repo: ReservationRepository):
        self.repo = repo

    async def get_reservations(self) -> List[ReservationOut]:
        reservations = await self.repo.get_reservations()
        return [ReservationOut.model_validate(reservation) for reservation in reservations]

    async def get_reservation_by_id(self, reservation_id: int) -> ReservationOut:
        reservation = await self.repo.get_reservation_by_id(reservation_id)
        return ReservationOut.model_validate(reservation) if reservation else None

    async def create_reservation(self, reservation: ReservationIn) -> ReservationOut:
        created_reservation = await self.repo.create_reservation(reservation)
        return ReservationOut(**created_reservation.__dict__)

    async def update_reservation(self, reservation_id: int, reservation: ReservationIn) -> ReservationOut:
        updated_reservation = await self.repo.update_reservation(reservation_id, reservation)
        return ReservationOut.model_validate(updated_reservation) if updated_reservation else None

    async def delete_reservation(self, reservation_id: int) -> None:
        await self.repo.delete_reservation(reservation_id)

    async def confirm_reservation(self, reservation_id: int) -> None:
        await self.repo.confirm_reservation(reservation_id)

    async def get_sessions(self) -> List[SessionTypeOut]:
        sessions = await self.repo.get_sessions()
        return [SessionTypeOut.model_validate(s) for s in sessions]

    async def create_session(self, session: SessionTypeIn) -> SessionTypeOut:
        created_session = await self.repo.create_session(session)
        return SessionTypeOut(**created_session.__dict__)
