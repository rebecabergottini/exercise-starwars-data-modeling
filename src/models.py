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
    name = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False)
    birth_year = Column(String(50), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    population = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    speed = Column(String(250), nullable=False)
 

class FavoritesCaracters(Base):
    __tablename__ = 'favoritesCaracters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))


class FavoritesPlanets(Base):
    __tablename__ = 'favoritesPlanets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))


class FavoritesVehicles(Base):
    __tablename__ = 'favoritesVehicles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
