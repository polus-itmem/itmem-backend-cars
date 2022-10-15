import time
from typing import Set, Any, List

from sqlalchemy import select
from db.models import Car


class WebQueryController:
    def __init__(self, session):
        self._session = session

    async def get_types(self) -> set[str]:
        cars: [Car] = (await self._session.execute(select(Car))).all()
        return set([i[0].description for i in cars])

    async def get_cars(self) -> List[Car]:
        cars: [Car] = (await self._session.execute(select(Car))).all()
        return [i[0] for i in cars]

    async def get_car(self, car_id: int) -> Car:
        car: Car = await self._session.get(Car, car_id)
        return car

    async def get_driver_car(self, user_id: int) -> List[Car]:
        cars: [Car] = (await self._session.execute(select(Car).where(Car.driver_id == user_id))).all()
        return [i[0] for i in cars]

    async def get_type_cars(self, car_type: str) -> List[Car]:
        cars: [Car] = (await self._session.execute(select(Car).where(Car.description == car_type))).all()
        return [i[0] for i in cars]
