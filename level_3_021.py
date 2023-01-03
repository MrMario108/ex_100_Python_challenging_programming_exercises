# Question 21

# Level 3

# Question A robot moves in a plane starting from the original point (0,0).
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# The trace of robot movement is shown as the following: UP 5 DOWN 3 LEFT 3
# RIGHT 2 ¡­ The numbers after the direction are steps. Please write a program
# to compute the distance from current position after a sequence of movement
# and original point. If the distance is a float, then just print the nearest
# integer. Example: If the following tuples are given as input to the program:
# UP 5 DOWN 3 LEFT 3 RIGHT 2 Then, the output of the program should be: 2

# Hints: In case of input data being supplied to the question, it should be
# assumed to be a console input.

moves_list = input('Enter the robot moves: ').split(' ')

i = 0
pos_y, pos_x = 0, 0
while i < len(moves_list):
    move = moves_list[i]
    i += 1

    step = int(moves_list[i])
    i += 1

    if move == 'UP':
        pos_y += step
    if move == 'DOWN':
        pos_y -= step
    if move == 'RIGHT':
        pos_x += step
    if move == 'LEFT':
        pos_x -= step


print('Number of moves to come back: ', abs(pos_y) + abs(pos_x))

# Solution from web

# import math
# pos = [0,0]
# while True:
#     s = input()
#     if not s:
#         break
#     movement = s.split(" ")
#     direction = movement[0]
#     steps = int(movement[1])
#     if direction=="UP":
#         pos[0]+=steps
#     elif direction=="DOWN":
#         pos[0]-=steps
#     elif direction=="LEFT":
#         pos[1]-=steps
#     elif direction=="RIGHT":
#         pos[1]+=steps
#     else:
#         pass
# print(pos[0], pos[1])

# here is mistake

# print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))
