import json
from os import error
import requests
def get_fun_fact(number):
    url = f"http://numbersapi.com/{number}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return  str(response.text) 
    else:
        return {"error": "Could not retrieve data"}

def check_is_prime(number):
    if number >= 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
          
        return True
    else:
        return False
          

def check_is_perfect(number):

    num = 0

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
    num = 0
    if int(number) >= 1:
        for num_iterator in number:
            power = pow(int(num_iterator), len(number))
            num += power
        if num == int(number):
            
            armstrong = "armstrong"
        else:
            
            armstrong  = "not armstrong"
    else:
        armstrong = "not armstrong"
        
    
    if int(number) >= 1:
        if (int(number) % 2) != 0:
            odd  = "odd"
        else:
            odd = "even"
    else:
        odd = "less than 1"
        
    return list([armstrong, odd])

def get_digit_sum(number):
        return sum(int(digit) for digit in str(number))


    
def generate_error_json(number):
        if not isinstance(number, int):  
            error_dict = {"number": "alphabet", "error": True}
            return json.dumps(error_dict)
        