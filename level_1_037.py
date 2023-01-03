# Question 37

# Level 1

# Define a function which can generate and print a list where the values are
# square of numbers between 1 and 20 (both included).

# Hints:

# Use ** operator to get power of a number. Use range() for loops. Use
# list.append() to add values into a list.


def create_list():
    new_list = []
    for i in range(1, 21):
        new_list.append(i**2)

    print(new_list)


create_list()
