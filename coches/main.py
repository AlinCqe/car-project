from utils import normal_str, promt_no_empty, pretty_str
from car import CombustionCar, ElectricCar
import csv


class GarageManager:
    def __init__(self):
        self.garage = {}

    def get_garage(self):
        return self.garage




    def load_csv_garaje(self):
    
        with open('combustion_garaje.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in  reader:
                if not row:
                    print('a')
                    pass
                print(row['nickname'] )
                nickname = row['nickname']       
                self.garage[nickname] = CombustionCar(row['brand'], row['model'], row['year'],row['kilometrage'], row['aspiration'], row['engine_capacity'] )

        with open('electric_garaje.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in  reader:
                if not row:
                    print('a')
                    pass
                    
                nickname = row['nickname']
                self.garage[nickname] = ElectricCar(row['brand'], row['model'], row['year'],row['kilometrage'], row['kilowatts'], row['range_km'] )






    def add_car(self):
        
        # INPUT + CHECKS

        nickname = promt_no_empty('Enter car nickname: ')  

        while True:
            type =  promt_no_empty('Enter car typpe: Electric | Combustion: ')
            if type not in {'electric','combustion'}:
                continue
            break
        brand = promt_no_empty('Enter car brand: ')

        model = promt_no_empty('Enter car model: ')

        year = promt_no_empty('Enter car year: ')

        while True:
            try:
                kilometrage = int(promt_no_empty('Enter car kilometrage: '))
                if kilometrage and kilometrage >= 1:
                    break
            except ValueError:
                pass

        # APPENDS TO THE CSV AND THE DICTIONARY DEPENDING ON TYPE OF CAR
            
        if type == 'combustion':
            
            while True:
                try:
                    engine_capacity = float(input('Engice capacity in cc format: '))
                    if engine_capacity > 0:
                        break
                    else:
                        continue

                except ValueError:
                    pass

            while True:
                aspiration = input('Engine tpye (Atmospheric/Turbo/Supercharged): ')
                if normal_str(aspiration) not in aspirations:
                    aspiration = None
                    print('Not available')
                    continue
                break

            #appends to the csv file 
            with open('combustion_garaje.csv', 'a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=filednames_combustion)
                writer.writerow({'nickname': nickname, 'brand': brand, 'model': model,'year': year,'kilometrage': kilometrage,'aspiration': aspiration,'engine_capacity': engine_capacity }) 
                
            #appends to the dict
            self.garage[nickname] = CombustionCar(brand, model, year,kilometrage,aspiration,engine_capacity)                        

            print('Car added successfully')

        if type == 'electric':

            while True:
                try:
                    kilowatts = int(input('Enter car power in KW: '))    
                    if kilowatts and kilowatts >= 1:
                        break
                except ValueError:
                    continue

            while True:
                try:
                    range_km = int(input('Enter car range at full charge in KM: '))
                    if range and range_km >= 1:
                        break
                except ValueError:
                    continue


            #appends to the csv file 
            with open('electric_garaje.csv', 'a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=filednames_electric)
                writer.writerow({'nickname': nickname, 'brand': brand, 'model': model,'year': year,'kilometrage': kilometrage,'kilowatts': kilowatts,'range_km': range_km })    

            #appends to the dict
            self.garage[nickname] = ElectricCar(brand, model, year,kilometrage,kilowatts,range_km)                        

            print('Car added successfully')






    def show_cars(self):
        current_cars = []

        print('Current cars: \n')

        for name in self.garage:
            print(f" - {pretty_str(name)}: {self.garage[name]}")

            current_cars.append(normal_str(name))

        print() 
        return current_cars   

    


    def delete_car(self):

        current_cars = self.show_cars()
        print('Select wich one: ')
        
        while True:
            car = normal_str(input())
            if car not in current_cars:
                print('Car not in the list')
                continue
            break


        
        # REMOVE THE DATA FROM THE CSV FILE
        for nickname in current_cars:
            print(self.garage[nickname])
            if self.garage[nickname].type == 'combustion':     #gets the type of car
                delete_row_from_csv('combustion_garaje.csv', car, filednames_combustion)

            if self.garage[nickname].type == 'electric':
                delete_row_from_csv('electric_garaje.csv', car, filednames_electric) 

        



            # REMOVE THE DATA FROM THE DICT
        
        del self.garage[car] 
        print('Car has been deleted\n')



    
    def modify_aspiration(self):
            
            current_cars = garage.show_cars()

            print('Select wich one: ')
            while True:
                car = normal_str(input())
                if car not in current_cars:
                    print('Car not in the list')
                    continue
                if self.garage[car].type == 'electric':
                    print('That is an electri car')
                    continue

                break

            while True:
                new_aspiration = normal_str(input('New type of engine: '))
                if not new_aspiration in aspirations:
                    print('Unavailable engine type')
                else:
                    break
            

            # Modify data from the dictionary 
            self.garage[car].engine_modify(new_aspiration)
            print(f'Engine type was changed to {new_aspiration}\n')

            # Modify data in the csv

            updated_rows =[]
            with open('combustion_garaje.csv') as file:
                rows = csv.DictReader(file)
                for row in rows:
                    if row['nickname'] == car:
                        row['aspiration'] = new_aspiration
                    updated_rows.append(row)
                    
            with open('combustion_garaje.csv', 'w',newline='') as file:
                writer = csv.DictWriter(file, fieldnames=filednames_combustion)
                writer.writeheader()
                writer.writerows(updated_rows)



garage = GarageManager()


filednames_combustion = ['nickname', 'brand', 'model','year','kilometrage','aspiration','engine_capacity']
filednames_electric = ['nickname', 'brand', 'model','year','kilometrage', 'kilowatts','range_km']


def delete_row_from_csv(filename, car_nickname, fieldnames):
    keep_list=[]
    with open(filename) as file:
        rows = csv.DictReader(file)
        for row in rows:
            if row['nickname'] != car_nickname:
                keep_list.append(row)
    
    with open(filename, 'w',newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(keep_list)

    




available_tasks = {'add_car', 'show_cars', 'delete_car', 'modify_aspiration'}
aspirations = {'atmospheric', 'turbo', 'supercharged'}
dict_cars = {}

def main():
    
    garage.load_csv_garaje()

    while True:

        task = normal_str(input('Add car | Show cars | Delete car | Modify engine aspiration: \n'))
        if not task in available_tasks:
            print('Not availible')


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
            if not garage.get_garage():
                print('Not available cars')
                continue
            garage.modify_aspiration()


    
            

main()



