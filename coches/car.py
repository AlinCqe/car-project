import random
from utils import pretty_str

hp_ratio = {
    'atmospheric': [70,100],
    'turbo': [100,130],
    'supercharged': [90,120]
}


def calculate_hp(type, capacity):
    percentage = random.randint(hp_ratio[type][0],hp_ratio[type][1])
    print(percentage)
    hp = float(capacity) * float(percentage)
    return f'{hp:.0f}'

class Car:  

    def __init__(self, type, brand, model,year,km, ):
        self.brand = brand
        self.model = model
        self.year = year
        self.km = km


    def __repr__(self):
        raise NotImplementedError("Subclasses must implement this method")
        #base = (f"{pretty_str(self.brand)} {pretty_str(self.model)} - {self.engine_capacity}l {pretty_str(self.engine_type)} with a total of {self.hp} HP")

        return base


class ElectricCar(Car):
    def __init__(self, brand, model,year,km, kilowatts, range):
        super().__init__('electric',brand, model,year,km)
        self.kilowatts = kilowatts
        self.range = range


class CombustionCar(Car):


    def __init__(self, brand, model,year,km,engine_type, engine_capacity):
        super().__init__('electric',brand, model,year,km)
        self.engine_type = engine_type
        self.engine_capacity = engine_capacity
        self.hp = calculate_hp(engine_type, engine_capacity)


        def engine_modify(self, new_engine_type):
            self.engine_type = new_engine_type
            self.hp = (calculate_hp(new_engine_type, self.engine_capacity))

    def __repr__(self):
        (f"{pretty_str(self.brand)} {pretty_str(self.model)} - {self.engine_capacity}l {pretty_str(self.engine_type)} with a total of {self.hp} HP")  # ADD KM AND YEAR TO IT