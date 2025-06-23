import random
from api_project.utils import pretty_str

hp_ratio = {
    'atmospheric': [70,100],
    'turbo': [100,130],
    'supercharged': [90,120]
}


def calculate_hp(aspiration_type, capacity):   
    # Calculates combustion car hp with aspiration type and capacity    
    percentage = random.randint(hp_ratio[aspiration_type][0],hp_ratio[aspiration_type][1])
    hp = float(capacity) * float(percentage)
    return f'{hp:.0f}'

class Car:  

    def __init__(self, car_type, brand, model,year,kilometrage):
        self.car_type = car_type
        self.brand = brand
        self.model = model
        self.year = year
        self.kilometrage = kilometrage


    def __repr__(self):
        raise NotImplementedError("Subclasses must implement this method")

       


class ElectricCar(Car):
    def __init__(self, brand, model,year,kilometrage,kilowatts, range_km):
        super().__init__('electric',brand,model,year,kilometrage)
        self.kilowatts = kilowatts
        self.range_km = range_km
        self.hp = f'{int(self.kilowatts) * 1.341:.0f}'

    def __repr__(self):
        return (f"{self.year} {pretty_str(self.brand)} {pretty_str(self.model)} - {self.kilowatts} kilowatts ({self.hp} hp) with {(self.range_km)} km range and a current mileage of {self.kilometrage} km")  




class CombustionCar(Car):


    def __init__(self, brand, model,year,kilometrage,engine_type, engine_capacity):
        super().__init__('combustion',brand, model,year,kilometrage)
        self.engine_type = engine_type
        self.engine_capacity = engine_capacity
        self.hp = calculate_hp(engine_type, engine_capacity)


    def __repr__(self):
        return (f"{self.year} {pretty_str(self.brand)} {pretty_str(self.model)} - {self.engine_capacity}l {self.engine_type} with a total of {self.hp} hp and a current mileage of {self.kilometrage} km")  
    



    def engine_modify(self, new_engine_type):
        # Change engine aspiration and recalcultates hp - input checks are done in main.py
        self.engine_type = new_engine_type
        self.hp = (calculate_hp(new_engine_type, self.engine_capacity))


