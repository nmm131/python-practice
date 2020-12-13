'''
Created on Nov 4, 2020

@author: N8
'''

# Declare a variable called first and assign it to the value "Hello World".
print('Declare a variable called first and assign it to the value "Hello World".')
first = "Hello World"
print(first)

# Write a comment that says "This is a comment."
print('\nWrite a comment that says "This is a comment.".')
print("This is a comment.")

# Log a message to the terminal that says "I AM A COMPUTER!"
print('\nLog a message to the terminal that says "I AM A COMPUTER!".')
print("I AM A COMPUTER!")

# Write an if statement that checks if 1 is less than 2 and if 4 is greater than 2. If it is, show the message "Math is fun."
print('\nWrite an if statement that checks if 1 is less than 2 and if 4 is greater than 2. If it is, show the message "Math is fun.".')
if 1 < 2 < 4:
    print("Math is fun.")

# Assign a variable called nope to an absence of value.
print("\nAssign a variable called nope to an absence of value.")
nope = None

# Use the language's "and" boolean operator to combine the language's "true" value with its "false" value.
print("""\nUse the language's "and" boolean operator to combine the language's "true" value with its "false" value.""")
print(True and False)

# Calculate the length of the string "What's my length?"
print("""\nCalculate the length of the string "What's my length?".""")
print(len("What's my length?"))

# Convert the string "i am shouting" to uppercase.
print('\nConvert the string "i am shouting" to uppercase.')
print("i am shouting".upper())

# Convert the string "1000" to the number 1000.
print('\nConvert the string "1000" to the number 1000.')
print(int("1000"))

# Combine the number 4 with the string "real" to produce "4real".
print('\nCombine the number 4 with the string "real" to produce "4real".')
print(str(4) + "real")

# Record the output of the expression 3 * "cool".
print('\nRecord the output of the expression 3 * "cool".')
print(3 * 'cool')

# Record the output of the expression 1 / 0.
print("\nRecord the output of the expression 1 / 0.")
# 1 / 0
print("ZeroDivisionError: division by zero")

# Determine the type of [].
print("\nDetermine the type of [].")
print(type([]))

# Ask the user for their name, and store it in a variable called name.
print("\nAsk the user for their name, and store it in a variable called name.")
name = input("What's your name?")

# Ask the user for a number.
# If the number is negative, show a message that says "That number is less than 0!"
# If the number is positive, show a message that says "That number is greater than 0!"
# Otherwise, show a message that says "You picked 0!.
print('\nAsk the user for a number. If the number is negative, show a message that says "That number is less than 0!" If the number is positive, show a message that says "That number is greater than 0!" Otherwise, show a message that says "You picked 0!".')
num = float(input("Pick a number."))
if num < 0:
    print("The number is less than 0!")
elif num > 0:
    print("The number is greater than 0!")
else:
    print("You picked 0!")

# Find the index of "l" in "apple".
print('\nFind the index of "l" in "apple".')
print("apple".find("l"))

# Check whether "y" is in "xylophone".
print('\nCheck whether "y" is in "xylophone".')
print("y" in "xylophone")

# Check whether a string called my_string is all in lowercase.
print("\nCheck whether a string called my_string is all in lowercase.")
my_string = "this string is all lowercase"
print('my_string = "this string is all lowercase"')
print(my_string.islower())