# Question 7

# Level 2

# Question: Write a program which takes 2 digits, X,Y as input and generates a
# 2-dimensional array. The element value in the i-th row and j-th column of
# the array should be i*j. Note:  i=0,1.., X-1; j=0,1,¡­Y-1. Example Suppose
# the following inputs are given to the program: 3,5 Then, the output of
# the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

# Hints: Note: In case of input data being supplied to the question, it
# should be assumed to be a console input in a comma-separated form.

x = input('Write dimension: ').split(',')
created_array = []

for i in range(int(x[0])):
    temp = []

    for j in range(int(x[1])):
        temp.append(i*j)

    created_array.append(temp)

print(created_array)


# Solution from web

input_str = input("Write dimension: ")
dimensions = [int(x) for x in input_str.split(',')]
rowNum = dimensions[0]
colNum = dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row*col

print(multilist)
