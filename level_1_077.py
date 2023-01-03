# Question 77

# Level 1

# Please write a program to output a random number, which is divisible by 5
# and 7, between 0 and 100 inclusive using random module and list
# comprehension.

# Hints: Use random.choice() to a random element from a list.

import random

print(random.choice([x for x in range(101) if x % 5 == 0 and x % 7 == 0]))
