# Question 5

# Level 1

# Question: Define a class which has at least two methods: getString: to get a
# string from console input printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# Hints: Use init method to construct some parameters

class Question:
    def __init__(self):
        self.question = ''

    def getString(self):
        self.question = input("Write a string: ")

    def printString(self):
        print(self.question.upper())


test = Question()
test.getString()
test.printString()
