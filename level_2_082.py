# Question 82

# Level 2

# Please write a program to compress and decompress the string "hello world!
# hello world!hello world!hello world!".

# Hints: Use zlib.compress() and zlib.decompress() to compress and decompress
# a string.

import sys
import zlib

value = b"hello world!hello world!hello world!hello world!"
compressed_value = zlib.compress(value, 9)
print(compressed_value, sys.getsizeof(compressed_value))

value = zlib.decompress(compressed_value)
print(value, sys.getsizeof(value))
