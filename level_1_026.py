# Question 26:

# Level 1

# Define a function which can compute the sum of two numbers.

# Hints: Define a function with two numbers as arguments. You can 
# compute the sum in the function and return the value.


def sum(x, y):
    return int(x) + int(y)


numbers = input("Enter two numbers: ").split(",")

print(sum(numbers[0], numbers[1]))
