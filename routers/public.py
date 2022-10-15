from typing import List

from fastapi import APIRouter, Request

import models
from services.web_query import WebQueryController

router = APIRouter()


@router.get('/types', response_model = List[models.CarType])
async def get_types(request: Request):
    session: WebQueryController = request.scope['session']
    types = await session.get_types()
    return [models.CarType(description = i) for i in types]


@router.get('/get_cars', response_model = List[models.Car])
async def get_cars(request: Request):
    session: WebQueryController = request.scope['session']
    cars = await session.get_cars()
    return [models.Car(
        id = i.car_id,
        park = i.park,
        type = models.CarType(description = i.description),
        name = i.name,
        number = i.number,
        driver_id = i.driver_id
    ) for i in cars]


@router.post('/get_driver_car', response_model = List[models.Car])
async def get_driver_car(driver_id: models.ModelId, request: Request):
    session: WebQueryController = request.scope['session']
    cars = await session.get_driver_car(driver_id.id)
    return [models.Car(
        id = i.car_id,
        park = i.park,
        type = models.CarType(description = i.description),
        name = i.name,
        number = i.number,
        driver_id = i.driver_id
    ) for i in cars]


@router.post('/get_car', response_model = models.Car)
async def get_driver_car(car_id: models.ModelId, request: Request):
    session: WebQueryController = request.scope['session']
    car = await session.get_car(car_id.id)
    return models.Car(
        id = car.car_id,
        park = car.park,
        type = models.CarType(description = car.description),
        name = car.name,
        number = car.number,
        driver_id = car.driver_id
    )


@router.post('/get_car_types', response_model = List[models.Car])
async def get_car_types(car_type: models.CarType, request: Request):
    session: WebQueryController = request.scope['session']
    cars = await session.get_type_cars(car_type.description)
    return [models.Car(
        id = i.car_id,
        park = i.park,
        type = models.CarType(description = i.description),
        name = i.name,
        number = i.number,
        driver_id = i.driver_id
    ) for i in cars]

