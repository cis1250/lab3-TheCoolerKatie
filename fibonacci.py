#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

textInput = input("Enter a positive integer: ")

val = 1
num = 0

num1 = 0
num2 = 0
sum = 0

while val == 1:
    try:
        num = int(textInput)
        if num > 0:
            val = 2
    except ValueError:
        textInput = input("Please enter a positive integer: ")


for i in range(num):
    if i == 0:
        print("0")
    if i == 1:
        print("1")
        num1 = 1
    else:
        sum = num1 + num2
        print(sum)
    num2 = num1
    num1 = sum

    if i == 1:
        num1 = 1
        num2 = 1


done = input("Complete.")
