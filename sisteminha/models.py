from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base

class Truck(Base):
    __tablename__ = 'trucks'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    value = Column(Float, nullable=False)
    available = Column(Boolean, default=True)
