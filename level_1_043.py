# Question 43

# Level 1

# Write a program to generate and print another tuple whose values are even
# numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

# Hints:

# Use "for" to iterate the tuple Use tuple() to generate a tuple from a list.


def print_tuple(i):
    temp_list = []
    for j in i:
        if j % 2 == 0:
            temp_list.append(j)

    new_tupla = tuple(temp_list)

    print(new_tupla)


print_tuple((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
