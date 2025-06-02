import random
from utils import pretty_str

hp_ratio = {
    'atmospheric': [70,100],
    'turbo': [100,130],
    'supercharged': [90,120]
}


def calculate_hp(type, capacity):
    percentage = random.randint(hp_ratio[type][0],hp_ratio[type][1])


    hp = float(capacity) * float(percentage)
    return f'{hp:.0f}'

class Car:  

    def __init__(self, type, brand, model,year,kilometrage):
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

    def __repr__(self):
        return (f"{pretty_str(self.brand)} {pretty_str(self.model)} {self.year} - {self.kilowatts} kilowatts with {(self.range_km)}km range and a mileage of {self.kilometrage}KMs")  

class CombustionCar(Car):


    def __init__(self, brand, model,year,kilometrage,engine_type, engine_capacity):
        super().__init__('electric',brand, model,year,kilometrage)
        self.engine_type = engine_type
        self.engine_capacity = engine_capacity
        self.hp = 'not available for now'
        #self.hp = calculate_hp(engine_type, engine_capacity)


        def engine_modify(self, new_engine_type):
            self.engine_type = new_engine_type
            self.hp = (calculate_hp(new_engine_type, self.engine_capacity))

    def __repr__(self):
        return (f"{pretty_str(self.brand)} {pretty_str(self.model)} {self.year} - {self.engine_capacity}l {pretty_str(self.engine_type)} with a total of {self.hp} and a mileage of {self.kilometrage}")  