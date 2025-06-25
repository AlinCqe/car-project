import csv


def normal_str(string):

    # Format to store data
    return string.strip().lower().replace(' ', '_')           


def promt_no_empty(text):

    #Check for input not empty
    while True:
        value = normal_str(input(text))
        if value:
            return value


def pretty_str(string):

    # Format str for prints
    return string.title().replace('_', ' ')




def delete_row_from_csv(filename, car_nickname, fieldnames):

    # Deletes a row from csv file using car_nickname
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

    
def int_exist_positive(text):
            
    while True:
        try:
            number = int(input(text))
            if number and number >= 1:
                break
        except ValueError:
            continue
        
    return int(number)

def float_exist_positive(text):
            
    while True:
        try:
            number = float(input(text))
            if number and number >= 1:
                break
        except ValueError:
            continue
        
    return float(number)