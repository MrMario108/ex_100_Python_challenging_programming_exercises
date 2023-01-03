# Question 25

# Level 1

# Question: Define a class, which have a class parameter and have a same
# instance parameter.

# Hints: Define a instance parameter, need add it in init method You can init
# a object with construct parameter or set the value later

class Example:
    name = 'MrMario108'

    def __init__(self, age):
        self.age = age


b = Example(40)

print(f'Name: {b.name} age: {b.age}')
