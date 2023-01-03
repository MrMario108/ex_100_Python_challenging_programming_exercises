# Question 45

# Level 2

# Write a program which can filter even numbers in a list by using filter
# function. The list is: [1,2,3,4,5,6,7,8,9,10].

# Hints:

# Use filter() to filter some elements in a list. Use lambda to define
# anonymous functions.


values_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_list = list(filter(lambda x: x % 2 == 0, values_list))

print(even_list)
