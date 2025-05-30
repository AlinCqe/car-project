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


    def __init__(self, brand, model, engine_type, engine_capacity):
        self.brand = brand
        self.model = model
        self.engine_type = engine_type
        self.engine_capacity = engine_capacity
        self.hp = calculate_hp(engine_type, engine_capacity)

    def __repr__(self):
        base = (f"{pretty_str(self.brand)} {pretty_str(self.model)} - {self.engine_capacity}l {pretty_str(self.engine_type)} with a total of {self.hp} HP")

        return base

    def engine_modify(self, new_engine_type):
        self.engine_type = new_engine_type
        self.hp = (calculate_hp(new_engine_type, self.engine_capacity))

