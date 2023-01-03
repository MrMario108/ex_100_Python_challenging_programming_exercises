# Question 35

# Level 1

# Define a function which can generate a dictionary where the keys are numbers
# between 1 and 20 (both included) and the values are square of keys. The
# function should just print the values only.

# Hints:

# Use dict[key]=value pattern to put entry into a dictionary. Use ** operator
# to get power of a number. Use range() for loops. Use keys() to iterate keys
# in the dictionary. Also we can use item() to get key/value pairs.


def create_dict():
    new_dict = {}
    for i in range(1, 21):
        new_dict[i] = i**2

    for i in new_dict.keys():
        print(new_dict[i], end=', ')


create_dict()


# Solution from web

# def printDict():
# 	d=dict()
# 	for i in range(1,21):
# 		d[i]=i**2
# 	for (k,v) in d.items():
# 		print(v)

# printDict()
