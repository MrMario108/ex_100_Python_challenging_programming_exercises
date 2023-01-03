# Question 31

# Level 1

# Define a function that can accept two strings as input and print the string
# with maximum length in console. If two strings have the same length, then
# the function should print all strings line by line.

# Hints:

# Use len() function to get the length of a string


def compare_len_string(text_1, text_2):
    if len(text_1) > len(text_2):
        print(text_1)

    elif len(text_1) < len(text_2):
        print(text_2)

    else:
        print(text_1)
        print(text_2)


compare_len_string('123', '555')
