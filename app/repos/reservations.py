import json
from typing import List, Sequence, Optional

from sqlalchemy import select
from app.models.schemas.reservations import ReservationIn, ReservationOut, SessionTypeOut, SessionTypeIn
from app.repos.base import BaseRepository
from app.models.db.reservations import Reservation, Session


class ReservationRepository(BaseRepository):
    async def get_reservations(self) -> List[ReservationOut]:
        stmt = select(Reservation)
        result = await self.db.execute(stmt)
        reservations = result.scalars().all()
        return [ReservationOut(**reservation.__dict__) for reservation in reservations]

    async def get_reservation_by_id(self, reservation_id: int) -> Optional[ReservationOut]:
        reservation = await self.get_by_id(Reservation, reservation_id)
        if reservation:
            return ReservationOut.model_validate(reservation)
        return None

    async def create_reservation(self, reservation: ReservationIn) -> Reservation:
        reservation_db = Reservation(**reservation.model_dump())
        self.db.add(reservation_db)
        await self.db.commit()
        await self.db.refresh(reservation_db)
        return reservation_db

    async def update_reservation(self, reservation_id: int, reservation: ReservationIn) -> ReservationOut:
        reservation_db = await self.get_by_id(Reservation, reservation_id)
        if not reservation_db:
            return None

        for field, value in reservation.model_dump().items():
            setattr(reservation_db, field, value)

        await self.db.commit()
        await self.db.refresh(reservation_db)
        return ReservationOut.model_validate(reservation_db)

    async def get_sessions(self) -> List[SessionTypeOut]:
        stmt = select(Session)
        result = await self.db.execute(stmt)
        sessions = result.scalars().all()
        return [SessionTypeOut(**s.__dict__) for s in sessions]

    async def create_session(self, session: SessionTypeIn) -> Session:
        session_db = Session(**session.model_dump())
        self.db.add(session_db)
        await self.db.commit()
        await self.db.refresh(session_db)
        return session_db
