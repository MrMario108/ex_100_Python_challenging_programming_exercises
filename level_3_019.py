# Question 19

# Level 3

# Question: You are required to write a program to sort the (name, age, height)
# tuples by ascending order where name is string, age and height are numbers.
# The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name >age > score.
# If the following tuples are given as input to the program:
# Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85 Then, the output of the
# program should be: [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17'
# , '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

# Hints: In case of input data being supplied to the question, it should be
# assumed to be a console input. We use itemgetter to enable multiple sort keys

from functools import cmp_to_key
tuple_list = []

while True:
    s = input("Enter name, age, score: ")
    if not s:
        break
    tuple_list.append(tuple(s.split(",")))


def mine(a, b):
    if a[0] > b[0]:
        return 1
    elif a[1] < b[1]:
        return -1
    else:
        if a[1] > b[1]:
            return 1
        elif a[1] < b[1]:
            return -1
        else:
            if a[2] > b[2]:
                return 1
            elif a[2] < b[2]:
                return -1
            else:
                return 0


print(sorted(tuple_list, key=cmp_to_key(mine)))


# Solution from web
from operator import itemgetter, attrgetter

l = []
while True:
    s = input()
    if not s:
        break
    l.append(tuple(s.split(",")))

print(sorted(l, key=itemgetter(0, 1, 2)))
