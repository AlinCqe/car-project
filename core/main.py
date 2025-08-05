from .utils import normal_str, promt_no_empty, pretty_str, delete_row_from_csv, int_exist_positive, float_exist_positive
from .car import CombustionCar, ElectricCar
from dB.dB import save_combustion_car, save_electric_car, show_cars, delete_car, modify_car_aspration



class GarageManager:
    def __init__(self):
        self.garage = {}

    def add_car(self, car):
        
        if car.car_type == 'combustion':

            save_combustion_car(car)

            return('Car added successfully')

        if car.car_type == 'electric':
            save_electric_car(car)
            return('Car added successfully')


    def show_cars(self):    

        return show_cars()


    def delete_car(self, car_nickname):

        if delete_car(car_nickname):
            return True
        else:
            return False
        


    def modify_aspiration(self, car_nickname, new_aspiration):

        return modify_car_aspration(car_nickname, new_aspiration)

