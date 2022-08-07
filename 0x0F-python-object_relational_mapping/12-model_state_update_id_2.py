#!/usr/bin/python3
""" change State objects name in id 2
from the database hbtn_0e_6_usa
"""
import sqlalchemy
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1],
                            argv[2],
                            argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id).all():
        if (state.id == 2):
            state.name = "New Mexico"
    session.commit()
    session.close()
