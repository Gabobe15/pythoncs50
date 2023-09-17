# while loop 

# increment  

'''
i = 0
while i < 3:
    print("Code")
    i += 1
   
 '''   
# decrement 
'''

i = 3
while i != 0:
    print("Gabobe")
    i -= 1
    
'''

# for loop 
'''

for i in [0,1,2]:
    print("moow")
    
'''

# another way of doing it - you can put your range easily

'''
for i in range(10): 
    print("play,", + (i + 1))
    
'''

# not recommended way of doing it 

'''
print("abdow\n" * 6, end="")

'''

# we want to keep asking for input value if the input is less than zero else we are going to print out result 
'''
while True:
    n = int(input("what is the value of n? "))
    if n > 0:
        break

for _ in range(n):
    print("football")
    
'''

# _ can be used when you don't want to declare your variable 


# we want to keep asking for input value if the input is less than zero else we are going to print out result -- using function

'''

def main():
    number = get_number()  # this function will get input value
    meow(number) # accept value and print out 
    
def get_number():
    while True:
        n = int(input("What is n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("cool")

main()


'''


# list - arrays 
# students = ["Abdi", "Shamso", "Ali", "Mohamud"]

'''

for student in students:
    print(student)

'''
'''
for i in range(len(students)):
    print(i + 1, students[i])
    
'''

# dictionary (dic)  - objects 
'''
students = {
    "Abdi": ' Eastleigh',
    "Aisho": ' Eastleigh',
    "Ali": ' Eastleigh',
    "Aliya": ' Pangani',
    
}

for student in students:
    print(student, students[student], sep=":")
    
'''

# array of object 

'''

students = [
    {
        "name": "Abdirahman",
        "house": "Eastleigh",
        "patronus": "yanyuur"
    },
    {
        "name": "Omar",
        "house": "Eastleigh",
        "patronus": "yanyuur"
    },
    {
        "name": "Fatuma",
        "house": "Eastleigh",
        "patronus": "yanyuur"
    },
    {
        "name": "Ali",
        "house": "Eastleigh",
        "patronus": None
    }
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")

'''

# printing square 3 by 3 
'''

def main():
    print_square(4)

def print_square(size):
    
    # for each row in square
    for i in range(size):
        
        # for each brick in brick 
        for j in range(size):
            
            # print brick 
            print("#", end="")
        print()
    
main()
    
'''

def main():
    print_square(4)

def print_square(size):
    for i in range(size):
        print("#" * size)
    print() 
    
main()
    