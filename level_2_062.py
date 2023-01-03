# Question 62

# Level 2

# Write a program to read an ASCII string and to convert it to a unicode
# string encoded by utf-8.

# Hints:

# Use unicode() function to convert.

# In Python 3.6, they do not have a built-in unicode() method. Strings
# are already stored as unicode by default and no conversion is required

import codecs


print('a'.encode('utf-8'))

print(codecs.decode(b'a', 'utf-8'))

print(chr(112))

print(ord('p'))
