def correct_aspiration_type(aspiration: str) -> str:
    if aspiration.lower() not in {'atmospheric', 'turbo', 'supercharged'}:
        raise ValueError(f'{aspiration} is not a availabe aspiration type')
    return aspiration.lower()  




def positive_number_int(value: int) -> int:
    if not value >= 0:
        raise ValueError(f'Value must be positive')
    return value  

def positive_number_float(value: float) -> float:
    if not value >= 0:
        raise ValueError(f'Value must be positive')
    return value  

def greater_than_0_int(value: int) -> int:
    if not value > 0:
        raise ValueError(f'Value has to be greater than 0')
    return value  

def greater_than_0_float(value: float) -> float:
    if not value > 0:
        raise ValueError(f'Value has to be greater than 0')
    return value  





def electric_car_type(car_type:str) -> str:
    if not car_type.lower() == 'electric':
        raise ValueError(f'Car type has to be electric availabe')
    return car_type

def combustion_car_type(car_type:str) -> str:
    if not car_type.lower() == 'combustion':
        raise ValueError(f'Car type has to be combustion availabe')
    return car_type