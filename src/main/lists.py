"""
Created on Nov 4, 2020

@author: N8
"""

# Given a list [1,2,3,4],
# print out all the values in the list.
print("Given a list [1,2,3,4], print out all the values in the list.")
number_list = [1, 2, 3, 4]
[print(num) for num in number_list]

# Given a list [1,2,3,4],
# print out all the values in the list multiplied by 20.
print("\nGiven a list [1,2,3,4], print out all the values in the list multiplied by 20.")
[print(num * 20) for num in number_list]
    
# Given a list ["Elie", "Tim", "Matt"],
# return a new list with only the first letter (["E", "T", "M"]).
print('\nGiven a list ["Elie", "Tim", "Matt"], return a new list with only the first letter (["E", "T", "M"]).')
word_list = ["Ellie", "Tim", "Matt"]
[print(person[0]) for person in ["Elie", "Tim", "Matt"]]

# Given a list [1,2,3,4,5,6],
# return a new list of all the even values ([2,4,6]).
print("\nGiven a list [1,2,3,4,5,6] return a new list of all the even values ([2,4,6]).")
number_list = [1, 2, 3, 4, 5, 6]
[print(num) for num in number_list if num % 2 == 0]

# Given two lists [1,2,3,4] and [3,4,5,6],
# return a new list that is the intersection of the two ([3,4]).
print("\nGiven two lists [1,2,3,4] and [3,4,5,6], return a new list that is the intersection of the two ([3,4]).")
number_list_1 = [1, 2, 3, 4]
number_list_2 = [3, 4, 5, 6]
[print(num) for num in number_list_1 if num in number_list_2]

# Given a list of words ["Elie", "Tim", "Matt"],
# return a new list with each word reversed and in lower case (['eile', 'mit', 'ttam']).
print("""\nGiven a list of words ["Elie", "Tim", "Matt"] return a new list with 
each word reversed and in lower case (['eile', 'mit', 'ttam']).""")
[print(word.lower() [::-1]) for word in word_list]

# Given two strings "first" and "third",
# return a new string with all the letters present in both words (["i", "r", "t"]).
print('\nGiven two strings "first" and "third", return a new string with all the '
      'letters present in both words (["i", "r", "t"]).')
string_1 = "first"
string_2 = "third"
[print(char) for char in string_1 if char in string_2]

# For all the numbers between 1 and 100,
# return a list with all the numbers that are divisible by 12 ([12, 24, 36, 48, 60, 72, 84, 96]).
print("\nFor all the numbers between 1 and 100, return a list with all the "
      "numbers that are divisible by 12 ([12, 24, 36, 48, 60, 72, 84, 96]).")
[print(num) for num in range(1, 100, 1) if num % 12 == 0]

# Given the string "amazing",
# return a list with all the vowels removed (['m', 'z', 'n', 'g']).
print("""\nGiven the string "amazing", return a list with all the vowels removed (['m', 'z', 'n', 'g']).""")
word_string = "amazing"
vowels = ["a", "e", "i", "o", "u"]
[print(char) for char in word_string if char not in vowels]

# Generate a list with the value [[0, 1, 2], [0, 1, 2], [0, 1, 2]].
print("\nGenerate a list with the value [[0, 1, 2], [0, 1, 2], [0, 1, 2]].")
[print([[i for i in range(0, 3, 1)] for num in range(0, 3, 1)])]

# Generate a list with the value:
# [
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# ]
print("""\nGenerate a list with the value:
[
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
].
""")
[print([[i for i in range(0, 10, 1)] for num in range(0, 10, 1)])]