#!/usr/bin/python3
""" just State objects that containt letter a
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
        if (state.name.find("a") != -1):
            print("{}: {}".format(state.id, state.name))
    session.close()