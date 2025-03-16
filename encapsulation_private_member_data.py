#

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age #private member 

    #getting the age 
    def get_age(self):
        return self.__age
    
    #setting the age 
    def set_age(self, age):
        self.__age = age
    
person1 = Person('Messi', 56)

print(f"Name : {person1.name}, age : {person1.get_age()}")

person1.set_age(90)

print(f"Name : {person1.name}, age : {person1.get_age()}")