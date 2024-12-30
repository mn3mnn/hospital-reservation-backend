from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.models.db.base import SQLBase

class Session(SQLBase):
    __tablename__ = "sessions"
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)


class Reservation(SQLBase):
    __tablename__ = "reservations"
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String, nullable=False)
    status = Column(String, nullable=False)
    has_shock_therapy = Column(Boolean, nullable=False)

    doctor_id = Column(Integer, ForeignKey("public.doctors.id"), nullable=False)
    patient_id = Column(Integer, ForeignKey("public.patients.id"), nullable=False)
    branch_id = Column(Integer, ForeignKey("public.branches.id"), nullable=False)
    session_id = Column(Integer, ForeignKey("public.sessions.id"), nullable=False)

    # doctor = relationship("Doctor", back_populates="reservation")
    # patient = relationship("Patient", back_populates="reservation")