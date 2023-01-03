# Question 46

# Level 2

# Write a program which can map() to make a list whose elements are square of
# elements in [1,2,3,4,5,6,7,8,9,10].

# Hints Use map() to generate a list. Use lambda to define anonymous functions.


values_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squere_list = list(map(lambda x: x**2, values_list))

print(squere_list)
