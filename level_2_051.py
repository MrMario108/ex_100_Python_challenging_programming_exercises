# Question 51

# Level 2

# Define a class named American and its subclass NewYorker.

# Hints:

# Use class Subclass(ParentClass) to define a subclass.


class American:
    @staticmethod
    def printNationality(country):
        print(country)


class NewYorker(American):
    pass


American.printNationality('America')
NewYorker.printNationality('America')
