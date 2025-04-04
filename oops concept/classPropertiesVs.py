class employee():

    #same for all employeee
    company_name = 'apple'
    
    no_of_employee = 0;
    def __init__(self, name, surname) -> None:
        self.name = name;
        self.surname = surname;
        employee.no_of_employee += 1;#updated when class object is made
        employee.salary = 500000  
    def showInfo(self):
        print(f'{self.no_of_employee} employee name is {self.name} {self.surname} and from {self.company_name} and earns {employee.salary}');

object1 = employee('shiva', 'chaudhary');

#first priority instance properties
#second priority class properties

#updated
employee.company_name = 'youtube.com'

#instance variable/ properties
object1.name = 'samprad'
object1.surname = 'adhikari';

#not updated hai but it has created new instance properties and it gets first priority
object1.company_name = 'google'

#not updated not made because in the method we use employee syntax so not updated
object1.salary = 20000;
#instance method
object1.showInfo();

object2 = employee('jevis', 'shrestha');
#instance method
object2.showInfo();

object3 = employee('anjelika', 'rimal');
object3.showInfo();


#class method 
class god():
    name = 'gautam buddha';
    def __init__(self, name = 'saraswoti') -> None:
        self._name = name;
        
    @classmethod
    def classMethod(cls, newname):
        cls.name  = newname;

    def showInfo(self):
        self.company_name = 'apple';
        print(f'the name of the god is {self.name} and {self.company_name}');

obj = god();
obj.classMethod('shiva bhagwan')
obj.showInfo()

#class method can be a proper way to update the class properties
#from the function

class employe():
    company_name = 'apple';
    no_of = 0;
    def showResult(self):
        print(f'the name of employe is {self.name} and works for the {self.company_name}, {employe.company_name} {self.no_of}');

    #new methods like first arguments act as the self and another argument act as the new argument comming from method
    def notclassMethod(fine, new):
        fine.company_name = new;

    @classmethod
    def classMethod1(fine, new, no_of):
        fine.company_name, fine.no_of = new, no_of;

obj = employe();
obj.name = 'jevis'
obj.notclassMethod('tesla');
obj.classMethod1('google', 3);
obj.showResult();


class person():
    def __init__(self, name, salary, post) -> None:
        self._name = name
        self._salary = salary;
        self._post = post;
    
    #additional constructor
    @classmethod
    def im_from_str(class_name, string):
        return class_name(string.split('-')[0], int(string.split('-')[1]) , string.split('-')[2])

    def showRslt(self):
        print(f'my name is {self._name} , {self._salary}, {self._post}');

string = 'jevis-300-programmer';

#if we do this for each person or instance = hard core❌
obj = person(string.split('-')[0], int(string.split('-')[1]), string.split('-')[2]);
# print(obj._name, obj._salary, obj._post);
obj1 = person.im_from_str(string);
print(obj1._name, obj1._salary, obj1._post);


#import bata string aairako xa 
# print(string.split('-')[0]);
# print(string.split('-')[1]);
# print(string.split('-')[2]);

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))

person = Person.from_string("John Doe, 30")
print(person.name, person.age)

string = 'shiva chaudhary, 30, founding manager of brothers co'
name, age, job = string.split(',');
print(name, age, job);

class person():
    def __init__(self, name, age) -> None:
        self._name = name;
        self._age = age;

    @classmethod
    def from_im_string(class_name, string):
        name, age = string.split(',');
        return class_name(name, int(age));

string = 'shiva chaudhary, 18';

#❌
# instance = person();
instance = person.from_im_string(string);
print(instance._name, instance._age);

import os;
path = 'C:/Users/user/OneDrive/Documents/python basics/cutter'
if not os.path.exists(path):
    os.mkdir(path);

#class to rename files 
class rename_files():
    def __init__(self, old_name, new_name) -> None:
        self.path = 'C:/Users/user/OneDrive/Documents/python basics/cutter'
        self.i = int(0)
        self._old = old_name;
        self._new = new_name;

    @classmethod
    #class constructor
    def im_from_str(class_name, string):
        o, n = string.split('-');
        return class_name(o, n);

    @property
    def get(self):
        #getting the new and old
        return self._old, self._new;

    @get.setter
    def set(self, o_n):
        #setting new to old
        self._old = o_n;

        for self.file in os.listdir(path):
            self.my_dest = 'new' + str(self.i) + '.img';

            #old name
            self.my_sour = os.path.join(self.path, self.file);

            #new name
            self.my_dest = os.path.join(self.path, self.my_dest);

            #rename
            os.rename(self.my_sour, self.my_dest);

            self.i += int(1);
            print(self.i);

    #method 
    def call_n_info(self):
        print(f'file name renamed of {self.i} {self.my_dest}');


file1 = rename_files.im_from_str('shiva.png-jevis.png');
print(file1._old, file1._new);

file2 = rename_files('samprad.png', 'jevis.png');
print(file2._old, file2._new);

file2.set = 'new0.png';
file2.set = 'shiva.png';
file2.set = 'shiva1.png';
file2.set = 'shiva2.png';
file2.set = 'shiva3.png';

class person():
    def __init__(self, name, age) -> None:
        self.__name = name;
        self.__age = int(age)

#defining object
obj = person('jevis', 23);

#__dict__ attribute
print(obj.__dict__);
obj.__class__('shiva', 18)
print(obj);

#help method 
# print(help(obj));

#help will describe the all the method and attribute and properties of the class, or function in which has been called 

print(obj.__dir__());

print('\n');
x = [1, 2];
print(x.__dir__());

y = 1.323;
print(y.__dir__());

#direct add 
print(y.__add__(1))
print(y.__float__());
print(y.__ceil__());
print(y.__getstate__());

# print(help(x.__add__))

class person():
    def __init__(self, name , sex) -> None:
        self.name = name;
        self.sex = sex;

obj = person('anjelika', 'female');
print(obj.__class__('shiva', 'male'));
print(obj.__dict__);

print(obj.name, obj.sex);
# print(help(obj));

print('\n');
#super key words()

#super keywords in the inheritance 
class manager:
    def manager_info(self):
        print(f'Manager - {self.name} earns {self.salary} from the {self.company_name}');

    def ceo_info(self):
        print(f'ceo - {self.name} earns {self.salary} from the {self.company_name}');


class employee(manager):
    def __init__(self, name, salary, company_name) -> None:
        self.name = name;
        self.salary = salary;
        self.company_name = company_name;

    def employee_info(self):
        print(f'employee - {self.name} earns {self.salary} from the {self.company_name}');

        #employee self.name, self.salary, self.company_name pass hunxa  
        super().manager_info();

#manager_method takes the properties which has been called in the class 
objManager = manager();
objManager.name = 'anje';
objManager.salary= '500';
objManager.company_name = 'cedro finance';
# objManager.manager_info();
# objManager.ceo_info();   

obj = employee('shiva', '100000000', 'apple');

#super 
obj.employee_info();

#inherit
obj.ceo_info();


#example of the multi level inhetitance 
class person1():
    def __init__(self, name, employee_id) -> None:
        self._name = name;
        self._employee_id = employee_id;

class person2(person1):
    def __init__(self, name, employee_id, job) -> None:
        self._job = job;
        super().__init__(name, employee_id);

#inherit from person2
class person3(person2):
    def __init__(self, name, employee_id, job, age) -> None:
        self._age = age;
        super().__init__(name, employee_id, job)

jevis = person2('jevis', 201, 'pathao');
print(jevis._name, jevis._employee_id, jevis._job);

shiva = person3('shiva', 301, 'appleceo', 21);
print(shiva._name, shiva._employee_id, shiva._age, shiva._job);


#import package of the clss
from dunderMethod import Employee;

samprad = Employee('samprad', 301);

#str method 
print(str(samprad));

#repr method 
print(repr(samprad));

#len method 
print(len(samprad));

#call method 
samprad();

