#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

# keep asking until the user enters a valid positive number
while True:
    user_input = input("How many Fibonacci numbers do you want? ")  # asking the user for the amount of terms
    if user_input.isdigit():  # checking if the input is only digits
        number = int(user_input)  # changing the input into an integer
        if number > 0:  # making sure the number is greater than 0
            break  # exit the loop if valid input
        else:
            print("Please enter a number greater than 0.")  # message if the number is 0 or negative
    else:
        print("Please enter a valid number.")  # message if the input is not a number

# defining the first 2 numbers in the Fibonacci sequence
a = 0
b = 1

# printing the Fibonacci sequence
for i in range(number):  # loop runs for the number of terms the user entered
    print(a, end=" ")  # printing the current number on one line with spaces
    next_number = a + b  # calculating the next number
    a = b  # moving forward in the sequence
    b = next_number  # updating b to the next number

