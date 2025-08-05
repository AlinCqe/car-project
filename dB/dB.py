import sqlite3

def create_tables():
    with sqlite3.connect('cars.db') as conn:
        cars_cursor = conn.cursor()

        cars_cursor.execute("""
            CREATE TABLE IF NOT EXISTS electric_cars
            (car_nickname TEXT PRIMARY KEY,
            car_type TEXT,
            brand TEXT,
            model TEXT,
            year INTEGER,
            kilometrage INTEGER,
            kilowatts INTEGER,
            range_km INTEGER)
            """)


        cars_cursor.execute("""
            CREATE TABLE IF NOT EXISTS combustion_cars
            (car_nickname TEXT PRIMARY KEY,
            car_type TEXT,
            brand TEXT,
            model TEXT,
            year INTEGER,
            kilometrage INTEGER,
            aspiration TEXT,
            engine_capacity REAL)
        """)

def save_electric_car(car):
    
    with sqlite3.connect('cars.db') as conn:

        cars_cursor = conn.cursor()
        cars_cursor.execute("INSERT INTO electric_cars VALUES (?,?,?,?,?,?,?,?)", (car.nickname,car.car_type, car.brand, car.model, car.year,car.kilometrage,car.kilowatts,car.range_km))

        conn.commit()

def save_combustion_car(car):

    with sqlite3.connect('cars.db') as conn:

        cars_cursor = conn.cursor()
        cars_cursor.execute("INSERT INTO combustion_cars VALUES (?,?,?,?,?,?,?,?)", (car.nickname,car.car_type, car.brand, car.model, car.year,car.kilometrage,car.aspiration,car.engine_capacity))

        conn.commit()

def show_cars():

    with sqlite3.connect('cars.db') as conn:
        cars = []

        conn.row_factory = sqlite3.Row
        cars_cursor = conn.cursor()

        cars_cursor.execute("SELECT * FROM combustion_cars")
        combustion_cars_rows = cars_cursor.fetchall()

        for row in combustion_cars_rows:
            cars.append(dict(row))

        cars_cursor.execute("SELECT * FROM electric_cars")
        electric_cars_rows = cars_cursor.fetchall()

        for row in electric_cars_rows:
            cars.append(dict(row))

        return cars
    
def delete_car(car_nickname):
    with sqlite3.connect('cars.db') as conn:
        cars_cursor = conn.cursor()

        cars_cursor.execute("DELETE FROM combustion_cars WHERE car_nickname = ?", (car_nickname,))
        combustion_cars_row_count = cars_cursor.rowcount

        cars_cursor.execute("DELETE FROM electric_cars WHERE car_nickname = ?", (car_nickname,))
        electric_cars_row_count = cars_cursor.rowcount
        
        conn.commit()

        if combustion_cars_row_count == 0 and electric_cars_row_count == 0:
            return False
        else:
            return True

def modify_car_aspration(car_nickname, new_aspiration):

    if not combustion_car_exist(car_nickname):
        return False, {'status_code':404, 'detail': 'This car is not a combustion car in the garage'}

    if combustion_car_aspiration_type_match(car_nickname, new_aspiration):
        return False, {'status_code':409, 'detail': 'The current aspiration type is the same as new one'}

    with sqlite3.connect('cars.db') as conn:
        cars_cursor = conn.cursor()

        cars_cursor.execute("UPDATE combustion_cars SET aspiration = ? WHERE car_nickname = ?", (new_aspiration, car_nickname))
        
        conn.commit()

        return ({'message': 'Car engine aspiration changed succesfully'})
    


def combustion_car_exist(car_nickname):
    with sqlite3.connect('cars.db') as conn:
        cars_cursor = conn.cursor()

        cars_cursor.execute("SELECT car_nickname FROM combustion_cars")
        combustion_cars_nicknames = {row[0] for row in cars_cursor.fetchall()}

        if car_nickname in combustion_cars_nicknames:
            return True
        else:
            return False

def combustion_car_aspiration_type_match(car_nickname, new_aspiration):
    with sqlite3.connect('cars.db') as conn:

        cars_cursor = conn.cursor()

        cars_cursor.execute("SELECT aspiration FROM combustion_cars WHERE car_nickname= ?", (car_nickname,))
        old_aspiration = cars_cursor.fetchone()

        if old_aspiration[0] == new_aspiration:
            return True
        else:
            return False

