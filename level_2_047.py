# Question 47

# Level 2

# Write a program which can map() and filter() to make a list whose elements
# are square of even number in [1,2,3,4,5,6,7,8,9,10].

# Hints Use map() to generate a list. Use filter() to filter elements of a
# list. Use lambda to define anonymous functions.

values_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squere_list = list(map(lambda x: x**2, values_list))
even_list = list(filter(lambda x: x % 2 == 0, squere_list))

print(even_list)


# Solution from web

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evenNumbers = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, li)))

print(evenNumbers)
