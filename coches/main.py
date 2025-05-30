from utils import normal_str, promt_no_empty
from car import Car
import csv
'''

Hacer clase 'Car' con inputs de ['brand', 'model', 'type', 'hp']

funcion para anadir coches
funcion para modificar el type(aspriacion atmosferica o turbo) y que al cambiar que los hp se modificen tmb
atmospheric -> turbo +35%-45% hp
atmospheric -> supercharged +25%-35% hp
turbo -> atmospheric - 35%-45% hp
turbo -> supercharged  - 10%-20% hp
supercharged -> atmospheric - 25%-35% hp
supercharged -> turbo + 10%-20% hp


'''

def show_current_cars():

    current_cars = []

    print('Current cars: \n')

    for name in dict_cars:
        print(f" -{name.title().replace('_', ' ')}: {dict_cars[name]}") 
        current_cars.append(normal_str(name))

    print() 
    return current_cars         #return list of current cars to another functions #DRY

def add_car():
    
    # INPUT CHECKS
    nickname = promt_no_empty('Enter car nickname: ')  
    brand = promt_no_empty('Enter car brand: ')
    model = promt_no_empty('Enter car model: ')

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
        engine_type = input('Engine tpye (Atmospheric/Turbo/Supercharged): ')
        if normal_str(engine_type) not in engine_types:
            engine_type = None
            print('Not available')
            continue
        break


    # ADD DATA TO THE CSV FILE
    with open('garaje.txt', 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['nickname', 'brand', 'model', 'capacity', 'aspiration'])
        writer.writerow({'nickname': nickname, 'brand': brand, 'model': model, 'capacity': engine_capacity,'aspiration': engine_type})



    # ADD DATA TO THE DICT
    dict_cars[nickname] = Car(brand, model, engine_type, engine_capacity)                        


def delete_car():

    # REMOVE THE DATA FROM THE DICT
    current_cars = show_current_cars()
    print('Select wich one: ')
    while True:
        car = normal_str(input())
        if car not in current_cars:
            print('Car not in the list')

        print('Car has been deleted\n')
        del dict_cars[car]


        # REMOVE THE DATA FROM THE CSV FILE
        keep_list=[]
        with open('garaje.txt') as file:
            rows = csv.DictReader(file)
            for row in rows:
                if row['nickname'] != car:
                    keep_list.append(row)
        
        with open('garaje.txt', 'w',newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['nickname','brand','model','engine_type','engine_capacity'])
            writer.writeheader()
            for row in keep_list:
                writer.writerow(row)


        break





def modify_engine_type():
        
        current_cars = show_current_cars()

        print('Select wich one: ')
        while True:
            car = normal_str(input())
            if car not in current_cars:
                print('Car not in the list')
            else:
                break


        while True:
            new_engine_type = normal_str(input('New type of engine: '))
            if not new_engine_type in engine_types:
                print('Unavailable engine type')
            else:
                break

        dict_cars[car].engine_modify(new_engine_type)
        print(f'Engine type was changed to {new_engine_type}\n')



available_tasks = {'add_car', 'show_cars', 'delete_car', 'modify_engine_type'}
engine_types = {'atmospheric', 'turbo', 'supercharged'}
dict_cars = {}

def main():

    while True:

        task = normal_str(input('Add car | Show cars | Delete car | Modify engine type: \n'))
        if not task in available_tasks:
            print('Not availible')


        if task == 'add_car':
            add_car()

        if task == 'show_cars':

            if dict_cars:
                show_current_cars()  
            else:
                print('No avalible Cars')

        if task == 'delete_car':

            if not dict_cars:
                print('Not available cars')
            else:
                delete_car()
                
        if task == 'modify_engine_type':
            if not dict_cars:
                print('Not available cars')
                continue
            modify_engine_type()


    
            

main()



