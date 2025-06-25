from fastapi import FastAPI, HTTPException
from pydantic import BaseModel,AfterValidator, field_validator

from typing import Annotated

from core.main import GarageManager
from .utils import correct_aspiration_type, positive_number_int, greater_than_0_int, greater_than_0_float



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
# Creates a instance of the garaje and loads the cars from the csv files in to self.garaje
garage_manager = GarageManager()
garage_manager.load_csv_garaje()



# unnecesary endpoint, delete in the future
@app.get('/showCarsPretty')
def get_cars_pretty():
    return garage_manager.show_cars()


@app.get('/showCars')
def get_cars():
    return garage_manager.garage



@app.post('/addElectricCar')
def add_electric_car(car: ElectricCar):
    print(car.nickname)
    if car.nickname in garage_manager.garage.keys():
        raise HTTPException(status_code=409, detail=f'This is alredy a car in the garage with the nickname: {car.nickname}')
    garage_manager.add_car(car=car)
    return({'message': 'Electric car added succesfully'})



@app.post('/addCombustionCar')
def add_combustion_car(car: CombustionCar):
    print(car.nickname)
    if car.nickname in garage_manager.garage.keys():
        raise HTTPException(status_code=409, detail=f'This is alredy a car in the garage with the nickname: {car.nickname}')
    garage_manager.add_car(car=car)
    return({'message': 'Combustion car added succesfully'})





@app.delete('/deletecar/{car_nickname}')
def delete_car(car_nickname: str):      
    
    car_nicknames = garage_manager.garage.keys()
    print(car_nicknames)

    if car_nickname not in car_nicknames:
        raise HTTPException(status_code=404, detail='This car is not in the garage')

    garage_manager.delete_car(car_nickname=car_nickname, current_cars_nicknames=car_nicknames)
    return({'message': 'Car succesfully deleted'})




@app.patch('/modifyengineaspiration/{car_nickname}+{new_aspiration}')
def modify_engine_aspiration(car_nickname: str, new_aspiration: Annotated[str, AfterValidator(correct_aspiration_type)]):
    
    combustion_car_nicknames = [nickname for nickname in garage_manager.garage if garage_manager.garage[nickname].car_type == 'combustion']

    if car_nickname not in combustion_car_nicknames:
        raise HTTPException(status_code=404, detail='This car is not a combustion car in the garage')
    
    if garage_manager.garage[car_nickname].aspiration == new_aspiration:
        raise HTTPException(status_code=409, detail='The current aspiration type is the same as new one')

    garage_manager.modify_aspiration(car_nickname=car_nickname, new_aspiration=new_aspiration)
    return({'message': 'Car engine aspiration changed succesfully'})

