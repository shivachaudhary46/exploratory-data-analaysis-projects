#multiple inheritance 
#Person parent class 
class Person:
    def person_data(self, name, age):
       
        print("hello from the person class")
        print("the name is:", name, "and the age is", age)

#company parent class 
class Company:
    def company_data(self, comp_name, location):
        
        print("welcome to the company !")
        print("The company name is", comp_name, "located in", location)

#Employee child class 
class Employee(Person, Company):
    def employee_details(self, salary, skill):
        print("welcome to the employee class ")
        print("the employee has skill", skill, "salary of", salary)

# objects for employee
Employee1 = Employee()

Employee1.person_data('shiva', 19)
Employee1.company_data('fusemachines', 'jawalakhel')
Employee1.employee_details(500000, 'machine learning engineer')