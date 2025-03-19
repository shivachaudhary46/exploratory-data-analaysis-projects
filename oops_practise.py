
#create the class Person and name, age, id as a parameter
class Person:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def display_person(self):
        print(f"name: {self.name} | age: {self.age} | id: {self.id}")


#create a instance 
person1 = Person('anje', 29, 100)
person2 = Person('shiva', 19, 101)
person3 = Person('jevis', 90, 102)

person1.display_person()
person2.display_person()
person3.display_person()