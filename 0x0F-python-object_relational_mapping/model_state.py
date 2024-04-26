#!/usr/bin/python3
"""
Module containing the class definition of a State and an instance Base = declarative_base().
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    Class representing a state in the MySQL database.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # Connect to MySQL server
    engine = create_engine('mysql://username:password@localhost:3306/database')

    # Create all tables
    Base.metadata.create_all(engine)

