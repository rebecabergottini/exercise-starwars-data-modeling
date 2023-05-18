import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    gender = Column(String(250))
    birth_year = Column(String(250), nullable=False)
    
    user_id = Column(Integer, ForeignKey('user.id')),
    user = relationship('User')

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    population = Column(String(250))
    diameter = Column(String(250), nullable=False)

    user_id = Column(Integer, ForeignKey('user.id')),
    user = relationship('User')

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    speed = Column(String(250), nullable=False)
    
    user_id = Column(Integer, ForeignKey('user.id')),
    user = relationship('User')

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)

    character_id = Column(Integer, ForeignKey('characters.id')),
    character = relationship('Characters')

    planet_id = Column(Integer, ForeignKey('planets.id')),
    character = relationship('Planets')

    vehicle_id = Column(Integer, ForeignKey('vehicles.id')),
    character = relationship('Vehicles')

    user_id = Column(Integer, ForeignKey('user.id')),
    character = relationship('User')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
