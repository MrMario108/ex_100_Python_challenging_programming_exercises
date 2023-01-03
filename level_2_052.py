# Question 52

# Level 2

# Define a class named Circle which can be constructed by a radius.
# The Circle class has a method which can compute the area.

# Hints:

# Use def methodName(self) to define a method.

import math


class Circle():
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return math.pi * self.radius**2


new_circle = Circle(5)
area = new_circle.compute_area()
print(area)
