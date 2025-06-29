import sys
import os
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from .utils import normal_str, promt_no_empty, pretty_str, delete_row_from_csv, int_exist_positive, float_exist_positive
from .car import CombustionCar, ElectricCar
import csv

# Get folder where car.py is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Build path to CSV files in the same folder for both electric and combustion cars
combustion_cars_csv_path = os.path.join(current_dir, 'combustion_garaje.csv')
electic_cars_csv_path = os.path.join(current_dir, 'electric_garaje.csv')

aspirations = {'atmospheric', 'turbo', 'supercharged'}

class GarageManager:
    def __init__(self):
        self.garage = {}

    def load_csv_garaje(self):
        # Reads data from csv file and stores objects for Combustion cars
        with open(combustion_cars_csv_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in  reader:
                if not row:
                    pass

                nickname = row['nickname']       
                self.garage[nickname] = CombustionCar(row['car_type'], row['brand'], row['model'], row['year'],row['kilometrage'], row['aspiration'], row['engine_capacity'] )

        # Reads data from csv file and stores objects for Electric cars
        with open(electic_cars_csv_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in  reader:
                if not row:
                    pass
                    
                nickname = row['nickname']
                self.garage[nickname] = ElectricCar(row['car_type'], row['brand'], row['model'], row['year'],row['kilometrage'], row['kilowatts'], row['range_km'] )


    def add_car(self, car):
        
        if car.car_type == 'combustion':
            
            # Appends to the csv file 
            with open(combustion_cars_csv_path, 'a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=filednames_combustion)
                writer.writerow({'nickname': car.nickname, 'car_type': car.car_type, 'brand': car.brand, 'model': car.model,'year': car.year,'kilometrage': car.kilometrage,'aspiration': car.aspiration,'engine_capacity': car.engine_capacity }) 
    
            # Appends to the dict
            self.garage[car.nickname] = CombustionCar(car.car_type,car.brand, car.model, car.year,car.kilometrage,car.aspiration,car.engine_capacity)                        

            return('Car added successfully')

        if car.car_type == 'electric':
         
            # Appends to the csv file 
            with open(electic_cars_csv_path, 'a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=filednames_electric)
                writer.writerow({'nickname': car.nickname, 'car_type': car.car_type,'brand': car.brand, 'model': car.model,'year': car.year,'kilometrage': car.kilometrage,'kilowatts': car.kilowatts,'range_km': car.range_km })    

            # Appends to the dict
            self.garage[car.nickname] = ElectricCar(car.car_type, car.brand, car.model, car.year,car.kilometrage,car.kilowatts,car.range_km)                        

            return('Car added successfully')


    def show_cars(self):    

        current_cars = []
        # Loads all the cars in the garage
        for name in self.garage:
            current_cars.append(f" - {pretty_str(name)}: {self.garage[name]}")

        return current_cars



    def delete_car(self, car_nickname, current_cars_nicknames):

        # REMOVE THE DATA FROM THE CSV FILE
        for nickname in current_cars_nicknames:
            if self.garage[nickname].car_type == 'combustion':    
                delete_row_from_csv(combustion_cars_csv_path, car_nickname, filednames_combustion)

            if self.garage[nickname].car_type == 'electric':
                delete_row_from_csv(electic_cars_csv_path, car_nickname, filednames_electric) 

        # REMOVE THE DATA FROM THE DICT
        del self.garage[car_nickname] 



    def modify_aspiration(self, car_nickname, new_aspiration):

        # Update car object in dict
        self.garage[car_nickname].engine_modify(new_aspiration)
        
        # Update car object in csv
        updated_rows = []
        with open(combustion_cars_csv_path) as file:
            rows = csv.DictReader(file)
            for row in rows:
                if row['nickname'] == car_nickname:
                    row['aspiration'] = new_aspiration
                updated_rows.append(row)
                    
        with open(combustion_cars_csv_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=filednames_combustion)
            writer.writeheader()
            writer.writerows(updated_rows)

        return{'message': f'Engine type was changed to {new_aspiration}'}

garage = GarageManager()

filednames_combustion = ['nickname', 'car_type','brand', 'model','year','kilometrage','aspiration','engine_capacity']
filednames_electric = ['nickname', 'car_type','brand', 'model','year','kilometrage', 'kilowatts','range_km']




