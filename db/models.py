from enum import Enum
from sqlalchemy import Column, Integer, Enum as Enum_s, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Car(Base):
    __tablename__ = 'car'

    car_id = Column(Integer, primary_key = True)

    park = Column(Text, nullable = False)
    description = Column(Text, nullable = False)
    name = Column(Text, nullable = False)
    number = Column(Text, nullable = False)
    driver_id = Column(Integer)
