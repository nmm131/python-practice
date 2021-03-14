"""
Created on Mar 14, 2021

@author: N8
"""

import re
TEXT_FILE = 'student.txt'
CSV_FILE = 'users.csv'


def add_student(first_name):
    with open(TEXT_FILE, 'a') as file:
        file.write(first_name)
    return None


def find_student(first_name):
    with open(TEXT_FILE, 'r') as file:
        for name in file:
            if name == first_name:
                print("{} was found!".format(first_name))


def update_student(first_name, new_name):
    with open(TEXT_FILE, 'r+') as file:
        name = file.read()
        name = re.sub(first_name, new_name, name)
        file.seek(0)
        file.write(name)
        file.truncate()
    return None


def remove_student(first_name):
    with open(TEXT_FILE, 'r+') as file:
        name = file.read()
        name = re.sub(first_name, '', name)
        file.seek(0)
        file.write(name)
        file.truncate()
    return None


if __name__ == "__main__":
    add_student("New")
    find_student("Minta")
    update_student("Marry", "Update")
    remove_student("Seth")
