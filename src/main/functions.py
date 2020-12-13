'''
Created on Nov 4, 2020

@author: N8
'''

def difference(x, y):
    return x - y

def product(x, y):
    return x * y

def print_day(x):
    try:
        return ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][x-1]
    except IndexError as e:
        return None

def last_element(x):
    try:
        return x[-1]
    except IndexError as e:
        return None

def number_compare(x, y):
    if x > y:
        return "First is greater."
    elif y > x:
        return "Second is greater."
    return "Numbers are equal."

def single_letter_count(x, y):
    return x.lower().count(y.lower())

