# classes you own data in python and give them values 
class Student:
    def __init__(self, name, house, patrnous):
        if not name:
            raise ValueError("Missing name")
        if house not in ["afmadow", "dhoobley", "kismayo", "nairobi"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patrnous = patrnous
        
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self):
        if self.patrnous == "Stage":
            return "horse"
        elif self.patrnous == "Otter":
            return "shoe"
        elif self.patrnous == "Jack Russell terrier":
            return "Cat"
        else:
            return "magic spell"
    
def main():
    student = get_student()
    print("Expecto patrnous")
    print(student.charm())
     
    
def get_student():
#    name = input("Name: ")
#    house = input("House: ")
#    student = Student(name, house)
#    return student

# two 
   name = input("Name: ")
   house = input("House: ")
   patrnous = input("patrnous: ")
   return Student(name, house, patrnous)
  
if __name__ == "__main__":
    main()


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
    

