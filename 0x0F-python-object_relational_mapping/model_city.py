#!/usr/bin/python3
"""
Module containing the class definition of a City.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

class City(Base):
    """
    Class representing a city in the MySQL database.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

if __name__ == "__main__":
    print("This module defines a City class.")

