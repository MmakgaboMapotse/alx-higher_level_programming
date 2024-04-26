#!/usr/bin/python3
"""
Script to add the State object "Louisiana" to the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def add_state(username, password, database):
    """
    Adds the State object "Louisiana" to the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): MySQL database name.
    """
    # Connect to MySQL server
    engine = create_engine(f'mysql://{username}:{password}@localhost:3306/{database}')

    # Create a sessionmaker
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Create a new State object
    new_state = State(name="Louisiana")

    # Add the new state to the session
    session.add(new_state)

    # Commit the session to the database
    session.commit()

    # Print the new state's ID
    print("New state ID:", new_state.id)

    # Close the session
    session.close()

if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Add the State object "Louisiana" to the database
    add_state(username, password, database)

