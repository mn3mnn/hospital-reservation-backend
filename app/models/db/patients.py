from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.db.base import SQLBase

class Patient(SQLBase):
    __tablename__ = "patients"
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    email = Column(String, nullable=False)

    # user_id = Column(Integer, ForeignKey("public.users.id"), nullable=False)
    # user = relationship("User", back_populates="patient")