# handling ValueError 
 
'''
try:
    x = int(input("what's x? "))
    print(f"x is {x}")

except ValueError:
    print("x is not an integer")
'''
    
# or 
'''

try:
    x = int(input("what's x? "))

except ValueError:
    print("x is not an integer")
    
else:
    print(f"x is {x}")  # it is going to execute the code no matter what
    
'''

# creating loop until a correct input

'''

while True:
    try:
    x = int(input("what's x? "))

    except ValueError:
    print("x is not an integer")
    
    else:
        break

 print(f"x is {x}")  # it is going to execute the code no matter what
 
 '''
 
def main():
    x = get_init("What's x? ")
    print(f"x is {x}")
    
def get_init(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass 
        # it pass if we don't get the correct value meaning it is not going to display and keeps asking for input again and again.
        
main()
 