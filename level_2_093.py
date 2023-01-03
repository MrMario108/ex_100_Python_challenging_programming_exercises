# Question 93

# Level 2

# With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a
# program to make a list whose elements are intersection of the above given
# lists.

# Hints: Use set() and "&=" to do set intersection operation.


list_1 = set([1,3,6,78,35,55]) 
list_2 = set([12,24,35,24,88,120,155])

list_1 &= list_2

print(list(list_1))
