#!/usr/bin/python3
"""defines a City model
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

Base = declarative_base()


class City(Base):
    """represont a City from database

     __tablename__: the name of sql table
    id (sqlalchemy.Integer): The City's id
    name (sqlalchemy.String): The City's name
    state_id (sqlalchemy.Integer): foreign key to states.id
   """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(String(128), ForeignKey('states.id'))
