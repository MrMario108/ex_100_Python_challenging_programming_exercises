# Question 56

# Level 3

# Write a function to compute 5/0 and use try/except to catch the exceptions.
# Please raise a RuntimeError exception.

# Hints: Hints:

# Use try/except to catch exceptions.


def throws():
    return 5/0


try:
    throws()
except ZeroDivisionError:
    print("division by zero!")

except Exception:
    print('Caught an exception')

finally:
    print('In finally block for cleanup')
