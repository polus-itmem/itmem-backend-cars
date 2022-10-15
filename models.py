from enum import Enum
from typing import List, Optional
from strenum import StrEnum

from pydantic import BaseModel


class ModelId(BaseModel):
    id: int


class CarType(BaseModel):
    description: str


class Car(BaseModel):
    id: int

    park: str
    type: CarType
    name: str
    number: str
    driver_id: int
