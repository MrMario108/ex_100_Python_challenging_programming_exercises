# Question 100

# Level 2

# Write a program to solve a classic ancient Chinese puzzle: We count 35 heads
# and 94 legs among the chickens and rabbits in a farm. How many rabbits and
# how many chickens do we have?

# Hint: Use for loop to iterate all possible solutions.

heds = 30
legs = 60

chikensLegs = heds * 2
rabbitsLegs = legs - chikensLegs
rabits = rabbitsLegs/2
chikens = (legs - rabits*4)/2

print('Chikens: ', chikens, 'Rabits: ', rabits)


# Solution from web


def solve(numheads, numlegs):
    ns = 'No solutions!'
    for i in range(numheads+1):
        j = numheads-i
        if 2*i+4*j == numlegs:
            return i, j
    return ns, ns


numheads = 30
numlegs = 60
solutions = solve(numheads, numlegs)
print(solutions)
