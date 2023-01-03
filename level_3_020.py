# Question 20

# Level 3

# Question: Define a class with a generator which can iterate the numbers,
# which are divisible by 7, between a given range 0 and n.

# Hints: Consider use yield


class Solution:
    def __init__(self, end) -> None:
        self.end = end + 1

    def divide(self):
        mylist = range(0, self.end)
        yield [x for x in mylist if x % 7 == 0]


text = input('Write ends number: ')

mygenerator = Solution(int(text))

for i in mygenerator.divide():
    print(i)


# Solutio from web

def putNumbers(n):
    i = 0
    while i < n:
        j = i
        i = i+1
        if j % 7 == 0:
            yield j


for i in putNumbers(100):
    print(i)
