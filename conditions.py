
'''
x = int(input("what is x? "))
y = int(input("what is y? "))

'''

# if condition
''''
    if x < y:
        print('x is less than y')

    if x > y:
        print('x is greater than y')
        
    if x == y:
        print('x is equal to y')

'''
    
    
# elif - if and  elif conditions
"""
if x < y:
    print('x is less than y')

elif x > y:
    print('x is greater than y')
    
elif x == y:
    print('x is equal to y')

"""

# if, elif and else conditions 

"""

if x < y:
    print('x is less than y')

elif x > y:
    print('x is greater than y')
    
else:
    print('x is equal to y')
    
"""

# or - condition 
"""

if x > y or x < y:
    print("x is not equal to y")
else:
    print('x is equal to y')

"""

    
# shorthand 
"""
if x != y:
    print('x is not equal to y')
else:
    print('x is equal to y')
    
"""
    
# or 
'''

if x == y:
    print('x is equal to y')
else:
    print('x is not equal to y')


'''


# grade 


# score = int(input('Score: '))


'''

if score >= 90 and score <= 100:
    print('Score: A')
elif score >= 80 and score < 90:
    print('Score: B')
elif score >= 70 and score < 80:
    print('Score: C')
elif score >= 60 and score < 70:
    print('Score: D')
else:
    print('Score: F')
    
'''

# shorthand or shorted way of doing the same 

'''

if score < 0 or score > 100:
    print('invalid')
elif score >= 90:
    print('Score: A')
elif score >= 80:
    print('Score: B')
elif score >= 70:
    print('Score: C')
elif score >= 60:
    print('Score: D')
elif score >= 0:
    print('Score: F')
    

'''
# parity - a number can be even or odd 

# x = int(input("What the value of x? "))

'''

if x % 2 == 0:
    print("Even number")
else:
    print("Odd number")
    
'''

# bool - boolean it can be either False or True 

#creating function for even and odd values 
'''

def main():
    x = int(input("what values of x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
        
def is_even(n):
    
    #if n % 2 == 0:
    #    return True
    #else:
    #    return False

    
    # or 
    
    # return True if n % 2 == 0 else False
    
    # or 
    
    return n % 2 == 0

main()
        

'''

# if conditions 

name = input("what's your name? ")

'''

if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("who?")
    
'''

# or 

'''

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("who?")
    
'''

# switch like case in python (match) 
'''

match name:
    case "Harry":
        print("Gryffindor")
    case "Hemione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print('Slytherin')
    case _: # who even case is not handle answer with who? / it is like else statement.
        print("who? ")
        
'''

# or 

match name:
    case "Harry" | "Hemione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print('Slytherin')
    case _: # who even case is not handle answer with who? / it is like else statement.
        print("who? ")