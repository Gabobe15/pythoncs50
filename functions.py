# def magac(to="world"):
#     print(f"Hello, {to} ")
# magac()
# name = input("What is your name? ").capitalize().strip() # we have the function before the input, so it's going to display the default values first 
# magac(name)


# square value 

# write a nested function 
# def main():
#     x = int(input("what is x? "))
#     print("x square is,",square(x)) 

# def square(n):
# # return the input of x
#     # return n * n
#     # return n ** 2  
#     return pow(n, 2)

# main()


def salaan(s="Abdirahman"):  # passing parameter 
    print(f"Hello, {s}")
salaan()
name = input("What is your name? ").capitalize()
salaan(f"Hello, {name}") #argument

