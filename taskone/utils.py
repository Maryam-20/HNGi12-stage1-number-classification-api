import json
from os import error
import requests
          
def check_is_prime(number):
    if number < 2:  
        return False
    for i in range(2, abs(number)):  
        if number % i == 0:
            return False
    return True

def check_is_perfect(number):
    number = int(number)
    num = 0
    if number < 1:  
        return False

    if number >= 1:
        for i in range(1, number):
            if (number % i) == 0:
                num += i

        
        if num == number:
            
            return True
        else:
            
            return False
    else:
        
        return False


def check_properties(number):
    number_str = str(abs(number))  
    num = 0

    if abs(number) >= 1:
        for num_iterator in number_str:
            power = pow(int(num_iterator), len(number_str))
            num += power

        armstrong = "armstrong" if num == abs(number) else "not armstrong"
    else:
        armstrong = "not armstrong"

    odd = "odd" if abs(number) % 2 != 0 else "even"

    return [armstrong, odd]

def get_digit_sum(number):
    return sum(int(digit) for digit in str(abs(number)))  

def get_fun_fact(number):
    number = abs(number)  
    url = f"http://numbersapi.com/{number}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return str(response.text) 
    else:
        return {"error": "Could not retrieve data"}


    
def generate_error_json_alphabet(value):
    if value.replace('.', '', 1).isdigit() or (value.startswith('-') and value[1:].replace('.', '', 1).isdigit()):
        error_dict = {"number": "float", "error": True}
    else:
        error_dict = {"number": "alphabet", "error": True}
    return json.dumps(error_dict)

def is_valid_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

