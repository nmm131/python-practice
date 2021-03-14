"""
Created on Mar 14, 2021

@author: N8
"""

from functools import wraps


def get_next_multiple(num, count=2):
    while True:
        new_count = count
        new_num = 0
        while new_count > 0:
            new_num = new_num + num
            new_count = new_count-1
        count = count+1
        yield new_num


def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True


def get_next_prime(num):
    for val in range(num + 1, 1000):
        if is_prime(val):
            yield val


def double_result(function):
    @wraps(function)
    def inner(*args, **kwargs):
        return function(*args, **kwargs) * 2
    return inner


@double_result
def add(a, b):
    return a + b


def only_even_parameters(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        if any([arg for arg in args if arg % 2 != 0]):
            return "Please add even numbers"
        return fn(*args, **kwargs)
    return inner


@only_even_parameters
def subtract(a, b):
    return a - b


def sum_index(collection):
    total = 0
    for index, val in enumerate(collection):
        total = total + index
    return total


if __name__ == "__main__":
    multiple = get_next_multiple(2)
    print(next(multiple))
    print(next(multiple))
    print(next(multiple))
    print()
    gen = get_next_prime(13)
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print()
    print(add(5, 5)) # @double_result
    print()
    print(subtract(7, 3)) # @only_even_parameters
    print(subtract(4, 2)) # @only_even_parameters
    print()
    print(sum_index([1, 2, 3, 4]))
