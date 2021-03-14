"""
Created on Mar 14, 2021

@author: N8
"""

import re
import csv
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
    return None


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


def print_names():
    with open(CSV_FILE) as file:
        reader = csv.DictReader(file)
        for row in reader:
            print("{} {}".format(row['first_name'], row['last_name']))
    return None


def add_name():
    with open(CSV_FILE, 'a', newline='') as file:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(file, fieldnames)
        first_name = input("Please specify a first name: ")
        last_name = input("Please specify a last name: ")
        writer.writerow(dict(first_name=first_name, last_name=last_name))
    return None

