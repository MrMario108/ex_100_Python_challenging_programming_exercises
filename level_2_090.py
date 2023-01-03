# Question 90

# Level 2

# By using list comprehension, please write a program generate a 3, 5, 8 3D
# list whose each element is 0.

# Hints: Use list comprehension to make a list.


my_list = [[[0 for x in range(8)] for x in range(5)] for x in range(3)]

print(my_list)
