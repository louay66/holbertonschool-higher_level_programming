#!/usr/bin/python3
""" list State objects name passed as argument
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
    NewState = State(name='Louisiana')
    session.add(NewState)
    for state in session.query(State).order_by(State.id).all():
        if (state.name == 'Louisiana'):
            port = True
            print("{}".format(state.id))
    session.commit()
    session.close()
