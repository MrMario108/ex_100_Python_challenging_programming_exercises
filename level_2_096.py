# Question 96

# Level 2

# Please write a program which count and print the numbers of each character
# in a string input by console.

# Example: If the following string is given as input to the program: abcdefgabc

# Then, the output of the program should be: a,2 c,2 b,2 e,1 d,1 g,1 f,1

# Hints: Use dict to store key/value pairs. Use dict.get() method to lookup a
# key with default value.

import collections

value = input('Please enter a value: ')

x = collections.Counter(value)

for i, v in dict(x).items():
    print(f"{i},{v}", end=" ")
