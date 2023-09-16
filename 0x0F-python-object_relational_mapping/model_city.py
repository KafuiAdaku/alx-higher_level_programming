#!/usr/bin/python3
"""A module that defines an ORM `City`"""
from model_state import Base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+mysqldb://root:root@localhost:3306/cities")
Session = sessionmaker(bind=engine)

class City(Base):
    """A class that defines cities in a state"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
