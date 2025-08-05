from fastapi import FastAPI, HTTPException
from pydantic import BaseModel,AfterValidator, field_validator
import sqlite3
from typing import Annotated

from core.main import GarageManager
from .utils import correct_aspiration_type, positive_number_int, greater_than_0_int, greater_than_0_float
from dB.dB import create_tables


class BaseCar(BaseModel):
    car_type: str
    nickname: str
    brand: str
    model: str
    year: Annotated[int, AfterValidator(greater_than_0_int)] 
    kilometrage: Annotated[int, AfterValidator(positive_number_int)] 

class ElectricCar(BaseCar):
    car_type: str = 'electric'
    kilowatts: Annotated[int, AfterValidator(greater_than_0_int)] 
    range_km: Annotated[int, AfterValidator(greater_than_0_int)]

    @field_validator('car_type')
    def check_car_type(cls, value):
        print(value)
        if value.lower() != 'electric':
            raise ValueError('Car type must be electric')
        return value.lower()
    
class CombustionCar(BaseCar):
    car_type: str = 'combustion'
    aspiration: Annotated[str, AfterValidator(correct_aspiration_type)]
    engine_capacity: Annotated[float, AfterValidator(greater_than_0_float)]

    @field_validator('car_type')
    def check_car_type(cls, value):
        if value.lower() != 'combustion':
            raise ValueError('Car type must be combustion')
        return value.lower()





app = FastAPI()

garage_manager = GarageManager()

@app.on_event('startup')
def startup_even():
    create_tables()


@app.get('/showCars')
def get_cars():
    return garage_manager.show_cars()

@app.post('/addElectricCar')
def add_electric_car(car: ElectricCar):
    print(car.nickname)
    try:
        garage_manager.add_car(car=car)
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=409, detail=f'This is alredy a car in the garage with the nickname: {car.nickname}')
    return({'message': 'Electric car added succesfully'})


@app.post('/addCombustionCar')
def add_combustion_car(car: CombustionCar):
    print(car.nickname)
    try:
        garage_manager.add_car(car=car)
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=409, detail=f'This is alredy a car in the garage with the nickname: {car.nickname}')

    return({'message': 'Combustion car added succesfully'})


@app.delete('/deletecar/{car_nickname}')
def delete_car(car_nickname: str):      
    
    if garage_manager.delete_car(car_nickname):
            return({'message': 'Car succesfully deleted'}) 
    else:
        raise HTTPException(status_code=404, detail='This car is not in the garage')


@app.patch('/modifyengineaspiration/{car_nickname}+{new_aspiration}')
def modify_engine_aspiration(car_nickname: str, new_aspiration: Annotated[str, AfterValidator(correct_aspiration_type)]):

    return garage_manager.modify_aspiration(car_nickname=car_nickname,new_aspiration=new_aspiration)
    

