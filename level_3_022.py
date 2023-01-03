# Question 22
# Level 3

# Question: Write a program to compute the frequency of the words from the
# input. The output should output after sorting the key alphanumerically.
# Suppose the following input is supplied to the program: New to Python or
# choosing between Python 2 and Python 3? Read Python 2 or Python 3. Then,
# the output should be: 2:2 3.:1 3?:1 New:1 Python:5 Read:1 and:1 between:1
# choosing:1 or:2 to:1

# Hints In case of input data being supplied to the question, it should be
# assumed to be a console input.


text = input('Enter your sentence: ')

set_of_words = set(text.split(' '))
dict_of_words = {}

for i in set_of_words:
    dict_of_words[i] = text.count(i)

words = sorted(set_of_words)
for w in words:
    print("%s:%d" % (w, dict_of_words[w]), end=" ")

# Solution from web

# freq = {}   # frequency of words in text
# line = input()
# for word in line.split():
#     freq[word] = freq.get(word,0)+1

# words = freq.keys()
# words = sorted(words)

# for w in words:
#     print("%s:%d" % (w,freq[w]))
