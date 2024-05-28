from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
DATABASE_URL = 'sqlite:///trucks.db'

def get_engine():
    return create_engine(DATABASE_URL)

def get_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()

class Truck(Base):
    __tablename__ = 'trucks'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    value = Column(Float, nullable=False)
    available = Column(Boolean, default=True)

def init_db():
    engine = get_engine()
    Base.metadata.create_all(engine)
