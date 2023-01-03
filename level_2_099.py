# Question 99

# Level 2

# Please write a program which prints all permutations of [1,2,3]

# Hints: Use itertools.permutations() to get permutations of list.

import itertools

nums = [1, 2, 3]

print(list(itertools.permutations(nums)))
