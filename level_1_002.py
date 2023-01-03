# Question 2

# Level 1

# Question: Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output
# should be: 40320

# Hints: In case of input # data being supplied to the question, it should be
# assumed to be a console input.


x = input("Write a numbers: ")

numbers_list = x.split(',')


def compute_factorial(x):
    if (x.isnumeric()):
        factorial = 1
        for i in range(1, int(x)+1):
            factorial *= i

        return str(factorial)


return_factorials_list = list(map(compute_factorial, numbers_list))
print(','.join(return_factorials_list))


# Solution from web:

def fact(x):
    if x == 0:
        return 1

    return x * fact(x - 1)


x = int(input())
print(fact(x))
