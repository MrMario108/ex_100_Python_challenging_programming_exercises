# Question 41

# Level 1

# Define a function which can generate and print a tuple where the value are
# square of numbers between 1 and 20 (both included).

# Hints:

# Use ** operator to get power of a number. Use range() for loops. Use
# list.append() to add values into a list. Use tuple() to get a tuple from
# a list.

def create_tuple():
    new_list = []
    for i in range(1, 21):
        new_list.append(i**2)

    new_tuple = tuple(new_list)
    print(new_tuple)


create_tuple()


# Other solution


def create_tuple():

    new_list = (i**2 for i in range(1, 21))
    new_tuple = tuple(new_list)
    print(new_tuple)


create_tuple()
