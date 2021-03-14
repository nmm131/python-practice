"""
Created on Mar 14, 2021

@author: N8
"""


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
