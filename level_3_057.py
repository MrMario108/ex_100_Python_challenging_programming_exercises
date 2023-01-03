# Question 57

# Level 3

# Define a custom exception class which takes a string message as attribute.

# Hints:

# To define a custom exception, we need to define a class inherited from
# Exception.


class MyException(Exception):
    def __init__(self, message):
        self.message = message


try:
    raise MyException("This is my exception !!!")
except MyException as me:
    print(me)


# Solution from web

# class MyError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

# error = MyError("something wrong")
