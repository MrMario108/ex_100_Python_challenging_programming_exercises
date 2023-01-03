# Question 32

# Level 1

# Define a function that can accept an integer number as input and print the
# "It is an even number" if the number is even, otherwise print "It is an
# odd number".

# Hints:

# Use % operator to check if a number is even or odd.

def is_even(num):
    if num % 2 == 0:
        print("It is an even number")
    else:
        print("It is an odd number")


is_even(266)
