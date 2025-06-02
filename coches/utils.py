def normal_str(string):
    return string.strip().lower().replace(' ', '_')           

def promt_no_empty(text):
    while True:
        value = normal_str(input(text))
        if value:
            return value

def promt_no_empty_ints(text):
    while True:
        value = (input(text))
        if value:
            return value    

def pretty_str(string):
    return string.title().replace('_', ' ')