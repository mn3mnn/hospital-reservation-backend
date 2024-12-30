from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.models.db.base import SQLBase

class Doctor(SQLBase):
    __tablename__ = "doctors"
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)

    # user_id = Column(Integer, ForeignKey("public.users.id"), nullable=False)
    # user = relationship("User", back_populates="doctor")

class DoctorBranch(SQLBase):
    __tablename__ = "doctors_branches"
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, ForeignKey("public.doctors.id"), nullable=False)
    branch_id = Column(Integer, ForeignKey("public.branches.id"), nullable=False)

    schedule = Column(JSON)  # Store schedule as JSON in the database
    #
    # doctor = relationship("Doctor", back_populates="doctor_branch")
    # branch = relationship("Branch", back_populates="doctor_branch")

