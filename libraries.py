# libraries - modules same thing 
# package - third party library 
# cowsay 


# pip is package manager 

# random library 
# random.choice
# random.randint

# statics library 
# average - mean 
# mode - frequent number
# median - middle number


# sys -  means sytem 
# sys.argv
# sys.exit 

# third party - packages 
# cowsay
# request - is api package 


# IndexError - if you have error in indexing 

import random
import statistics
import sys

# number = random.randint(1,10)
# print(number)

# shuffle
 
# list 
# cards = ["jack", "queen", "king"]

# shuffle 
# random.shuffle(cards)

# loop 
# for card in cards:
#     print(card)


# statistics 
# average = statistics.median([100, 80, 70, 100,60])
# print(average)



# argv - argument variables - which show the commandline stored 

# print("Hello, my name is", sys.argv[0])

# try except method 
'''
try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
    
'''

# try condition 
'''

# check for errors 
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")  ## system exit, unless it would have shown us error removing else statement 
# print name 
# else: sys.exit is going handle indexerror 
print("Hello, my name is", sys.argv[1])

'''
# adding loops and slice 

'''

if len(sys.argv) < 2:
    sys.exit("too few arguments")
# looping 
# slice - we are starting from index 1 leaving out the file name 
for arg in sys.argv[1:]:
    print("Hello,", arg)
    
'''
