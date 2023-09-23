# classes you own data in python and give them values 
# class Student:
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house
        
#     def __str__(self):
#         return f"{self.name} from {self.house}"
    
#     # getter 
#     @property
#     def name(self):
#         return self._name
    
#     @property
#     def house(self):
#         return self._house
    
#     # setter 
#     @name.setter
#     def name(self, name):
#         if not name:
#             raise ValueError("Missing name ")
#         self._name = name
    
#     @house.setter
#     def house(self, house):
#         if house not in ["afmadow", "dhoobley", "kismayo", "nairobi"]:
#             raise ValueError("invalid house")
#         self._house = house
    
    
# def main():
#     student = get_student()
#     print(student)
     
    
# def get_student():
#    name = input("Name: ")
#    house = input("House: ")
#    student = Student(name, house)
#    return student

# two 
#    name = input("Name: ")
#    house = input("House: ")
#    return Student(name, house)
  
# if __name__ == "__main__":
#     main()

# import random

# class Hat():
#     def __init__(self):
#         self.houses = ["12 street", "Section 3", "Section 3", "Jam street"]
    
#     def sort(self, name):
#         print(name, "is in", random.choice(self.houses))


# hat = Hat()
# hat.sort("harry")

# option two 
# class Hat():
    
#     houses = ["12 street", "Section 3", "Section 3", "Jam street"]
    
#     @classmethod
#     def sort(cls, name):
#         print(name, "is in", random.choice(cls.houses))
    
# Hat.sort("harry")




# class Student():
#     def __init__(self,name, house):
#         self.name = name
#         self.house = house
    
#     def __str__(self):
#         return f"{self.name} from {self.house}"
    
#     @classmethod
#     def get(cls):
#         name = input("Name: ")
#         house = input("House: ")
#         return cls(name, house)
   
# you can print directly or use main function todo the job for you  
# student = Student.get()
# print(student)
    
# def main():
#     student = Student.get()
#     print(student)
  
# if __name__ == "__main__":
#     main()

# if you matual paramater create a seperate class and use inheritance toward the children classes 

# class Wizard:
#     def __init__(self, name):
#         if not name:
#             raise ValueError("Missing name")
#         self.name = name
    
#     def __str__(self):
#         return f"{self.name}"
#     ...

# class Student(Wizard):
#     def __init__(self,name, house):
#         super().__init__(name)  # passing name from parrent
#         self.house = house
        
#     def __str__(self):
#         return f"{self.name} from {self.house}"
#     ...
    
# class Professor(Wizard):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject
    
#     def __str__(self):
#         return f"{self.name} from {self.subject}"
#     ...


# wizard = Wizard("jinijinow")
# student = Student("Abdirahman", "Ikhlas apartment")
# proffesor = Professor("Mohamed", "Computer programing")

# print(wizard)
# print(student)
# print(proffesor)



class Vault():
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        
    def __str__(self) :
        return f"{self.galleons} galleons, {self.sickles} sickles, {self.knuts} knuts"
    
    # operator overloading 
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)
        
potter = Vault(100, 50, 25)
print(potter)
weasley = Vault(100, 50, 25)
print(potter)

total = potter + weasley
print(total)








# functional 

# def main():
    # first approach 
    # name = get_name()
    # house = get_house()
    
    # second approach 
    # student = get_student()
    
    # let us write out own condition 
    # if student[0] == "gabobe":
    #     student[1] = "afmadow"
    
    # another way of writing condtion in dict 
    # if student['name'] == 'gabobe':
    #     student['house'] = 'afmadow'
    
    # printing things first approach 
    # print(f"{student[0]} from {student[1]}")
    
    # second approach 
    # print(f"{student['name']} from {student['house']}")
    
# first approach 
# def get_name():
#     return input("Name: ")

# def get_house():
#     return input("House: ")

# second approach 
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
    
    #if we use open and close bracket that means we are returning tuples which does not support assignment but if we use square bracket we are converting out data into list which we can overwrite 
    # return [name, house]
    
# third approach 
# def get_student():
#     student = {}
#     student['name'] = input("Name: ")
#     student['house'] = input("House: ")
#     return student

# fourth approach 
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return {'name': name, 'house': house}

# if __name__ == "__main__":
#     main()
    

