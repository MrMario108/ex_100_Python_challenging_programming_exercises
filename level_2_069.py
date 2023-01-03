# Question 69

# Level 2

# Please write a program using generator to print the numbers which can be
# divisible by 5 and 7 between 0 and n in comma separated form while n is
# input by console.

# Example: If the following n is given as input to the program: 100
# Then, the output of the program should be: 0,35,70

# Hints: Use yield to produce the next value in generator.

# In case of input data being supplied to the question, it should be assumed
# to be a console input.

def generate_divisibles(num):
    for i in range(num+1):
        if i % 5 == 0 and i % 7 == 0:
            yield str(i)


num = int(input("Please enter a number: "))

print(','.join(list(generate_divisibles(num))))

# Solution from web

# def NumGenerator(n):
#     for i in range(n+1):
#         if i%5==0 and i%7==0:
#             yield i

# n=int(input())
# values = []
# for i in NumGenerator(n):
#     values.append(str(i))

# print(",".join(values))
