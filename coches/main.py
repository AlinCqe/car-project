from utils import normal_str, promt_no_empty, pretty_str, delete_row_from_csv, int_exist_positive, float_exist_positive
from car import CombustionCar, ElectricCar
import csv


class GarageManager:
    def __init__(self):
        self.garage = {}

    def get_garage(self):
        return self.garage


    def load_csv_garaje(self):
        # Reads data from csv file and stores objects for Combustion cars
        with open('combustion_garaje.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in  reader:
                if not row:
                    pass

                nickname = row['nickname']       
                self.garage[nickname] = CombustionCar(row['brand'], row['model'], row['year'],row['kilometrage'], row['aspiration'], row['engine_capacity'] )

        # Reads data from csv file and stores objects for Electric cars
        with open('electric_garaje.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in  reader:
                if not row:
                    pass
                    
                nickname = row['nickname']
                self.garage[nickname] = ElectricCar(row['brand'], row['model'], row['year'],row['kilometrage'], row['kilowatts'], row['range_km'] )



    def add_car(self):
        
        # Inputs + checks

        nickname = promt_no_empty('Enter car nickname: ')  

        while True:
            car_type =  promt_no_empty('Enter car typpe: Electric | Combustion: ')
            if car_type not in {'electric','combustion'}:
                continue
            break
        brand = promt_no_empty('Enter car brand: ')

        model = promt_no_empty('Enter car model: ')

        year = int_exist_positive('Enter car year: ')

        kilometrage = int_exist_positive('Enter car kilometrage: ')
        '''
        while True:
            try:
                kilometrage = int(promt_no_empty('Enter car kilometrage: '))
                if kilometrage and kilometrage >= 1:
                    break
            except ValueError:
                pass
'''

        # APPENDS TO THE CSV DEPENDING ON TYPE OF CAR
            
        if car_type == 'combustion':
            # More inputs + checks
            engine_capacity = float_exist_positive(('Engice capacity in cc format: '))
            
            while True:
                aspiration = input('Engine type (Atmospheric/Turbo/Supercharged): ')
                if normal_str(aspiration) not in aspirations:
                    print('Not available')
                    continue
                break

            # Appends to the csv file 
            with open('combustion_garaje.csv', 'a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=filednames_combustion)
                writer.writerow({'nickname': nickname, 'brand': brand, 'model': model,'year': year,'kilometrage': kilometrage,'aspiration': aspiration,'engine_capacity': engine_capacity }) 
                
            # Appends to the dict
            self.garage[nickname] = CombustionCar(brand, model, year,kilometrage,aspiration,engine_capacity)                        

            print('Car added successfully')


        if car_type == 'electric':
            
            # More inputs + checks
            kilowatts = int_exist_positive('Enter car power in KW: ')
            range_km = int_exist_positive('Enter car range at full charge in KM: ')

            # Appends to the csv file 
            with open('electric_garaje.csv', 'a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=filednames_electric)
                writer.writerow({'nickname': nickname, 'brand': brand, 'model': model,'year': year,'kilometrage': kilometrage,'kilowatts': kilowatts,'range_km': range_km })    

            # Appends to the dict
            self.garage[nickname] = ElectricCar(brand, model, year,kilometrage,kilowatts,range_km)                        

            print('Car added successfully')






    def show_cars(self):    

        current_cars = []
        print('Current cars: \n')

        # Prints each car in the garage
        for name in self.garage:
            print(f" - {pretty_str(name)}: {self.garage[name]}")

            # Appends the car name in to a list
            current_cars.append(normal_str(name))

        print() 

        # Returns that list of names to other functions
        return current_cars   



    def delete_car(self):

        current_cars = self.show_cars()
        print('Select wich one: ')

        # inputs + checks
        while True:
            car = normal_str(input())
            if car not in current_cars:
                print('Car not in the list')
                continue
            break

        # REMOVE THE DATA FROM THE CSV FILE
        for nickname in current_cars:
            if self.garage[nickname].car_type == 'combustion':     #gets the type of car
                delete_row_from_csv('combustion_garaje.csv', car, filednames_combustion)

            if self.garage[nickname].car_type == 'electric':
                delete_row_from_csv('electric_garaje.csv', car, filednames_electric) 

        # REMOVE THE DATA FROM THE DICT
        del self.garage[car] 
        print('Car has been deleted\n')


    
    def modify_aspiration(self):

        # Inputs + checks
        print('Select which one: ')
        while True:
            car = normal_str(input())
            if car not in combustion_cars:
                print('Car not in the list')
                continue
            if self.garage[car].car_type == 'electric':
                print('That is an electric car')
                continue
            break

        while True:
            new_aspiration = normal_str(input('New type of engine: '))
            if not new_aspiration in aspirations:
                print('Unavailable engine type')
            else:
                break

        # Update car object in dict
        self.garage[car].engine_modify(new_aspiration)
        print(f'Engine type was changed to {new_aspiration}\n')

        # Update car object in csv
        updated_rows = []
        with open('combustion_garaje.csv') as file:
            rows = csv.DictReader(file)
            for row in rows:
                if row['nickname'] == car:
                    row['aspiration'] = new_aspiration
                updated_rows.append(row)
                    
        with open('combustion_garaje.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=filednames_combustion)
            writer.writeheader()
            writer.writerows(updated_rows)



garage = GarageManager()


filednames_combustion = ['nickname', 'brand', 'model','year','kilometrage','aspiration','engine_capacity']
filednames_electric = ['nickname', 'brand', 'model','year','kilometrage', 'kilowatts','range_km']







available_tasks = {'add_car', 'show_cars', 'delete_car', 'modify_engine_aspiration'}
aspirations = {'atmospheric', 'turbo', 'supercharged'}
dict_cars = {}
combustion_cars = []
def main():
    
    garage.load_csv_garaje()

    while True:

        task = normal_str(input('Add car | Show cars | Delete car | Modify engine aspiration: \n'))
        if task not in available_tasks:
            print('Not availible')
            continue

        if task == 'add_car':
            garage.add_car()

        if task == 'show_cars':

            if garage.get_garage():
                garage.show_cars()  
            else:
                print('No avalible Cars')

        if task == 'delete_car':

            if not garage.get_garage():
                print('Not available cars')
            else:
                garage.delete_car()
                
        if task == 'modify_engine_aspiration':

            with open('combustion_garaje.csv', 'r') as f:           
                reader = csv.DictReader(f)

                print('Current combustion cars: \n')

                # Prints all combustion cars in the CSV
                for row in reader:
                    car_nickname = row['nickname']
                    print(f' - {car_nickname} : {garage.garage[car_nickname]}')
                    combustion_cars.append(row['nickname'])
                print()

            # If no combustion cars are found
            if not combustion_cars:
                print('Not available cars')
                continue


            garage.modify_aspiration()
            
        

main()



