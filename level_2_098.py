# Question 98

# Level 2

# Please write a program which accepts a string from console and print the
# characters that have even indexes.
# Example: If the following string is given as input to the program:
# H1e2l3l4o5w6o7r8l9d
# Then, the output of the program should be: Helloworld

# Hints: Use list[::2] to iterate a list by step 2.

value = input("Please enter a string: ")

print(value[::2])
