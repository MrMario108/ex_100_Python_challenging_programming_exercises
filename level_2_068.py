# Question 68

# Level 2

# Please write a program using generator to print the even numbers between 0
# and n in comma separated form while n is input by console.
# Example: If the following n is given as input to the program: 10
# Then, the output of the program should be: 0,2,4,6,8,10

# Hints: Use yield to produce the next value in generator.

# In case of input data being supplied to the question, it should be assumed
# to be a console input.

def gen_even_num(n):
    for i in range(0, n+1, 2):
        yield str(i)


n = int(input('Enter a number: '))
int(",".join(list(gen_even_num(n))))

# Solution from web

# def EvenGenerator(n):
#     i=0
#     while i<=n:
#         if i%2==0:
#             yield i
#         i+=1


# n=int(input('put: '))
# values = []
# for i in EvenGenerator(n):
#     values.append(str(i))

# print(",".join(values))
