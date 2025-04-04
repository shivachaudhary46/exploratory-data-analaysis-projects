#class for the person
class person():
    name = 'jevis';
    age = 12;
    friends = 'samprad';
    job = 'programmer';
    hobby = 'biker';
    def info(self):
        print(f'{self.name} is {self.age} and has job of {self.job}.')
        print(f'{self.name} hobby is {self.hobby} as well as has friends like {self.friends}')

    def speak(self):
        print(f'{self.name} always speak vulger');
#object can have many unique properties 
#same method  
#method are action 
#function which do work
#self is written to those object which , where method are being called 
#self is key

#a = object 1
a = person();

#parent was not in defaulst -------------inheritance
a.parent = 'kalpana shrestha';
print(a.parent);

a.name = 'shiva';
a.hobby = 'travelling';
a.age = 18;
a.friends = None;
a.job = 'data scientist / analyst / vloger'
a.info();
a.speak

#default properties is not written in object,  it shows none
b = person();
b.name = 'samprad'
b.friends = 'anjelika';
b.friends = 'samprad'
b.name = 'anje';
b.age = 34;
b.job = 'makeup artist'
b.hobby = 'part time modeling'

b.info();
b.speak();

print('\n');
#next class 
class car():
    name = 'lamborgini';
    tyre = 4;
    owner = 'Volkswagen Group';
    engine = '600cc';
    def info(self):
        print(f'the {self.name} is owned by {self.owner}');
        print(f'the {self.name} has engine of {self.engine}');

car1 = car();
car1.name = 'audi';
car1.owner = 'shiva chaudhary';
car1.engine = '350cc';
car1.tyre = True;

car1.info();

#constructor theory
#paramatical constructor 
#default constructor

class defination():
    def __init__(self) -> None:
        print('this always operate without any command ');

# obj = defination();


class family():
    def __init__(self, name, mom, brother, me, father ) -> None:
        self.parent_n = name;
        self.myself = me ;
        self.brother = brother;
        self.mom = mom
        self.father = father

    def info(self):
        print(f'the family has 4 people shiva = {self.myself}, sanjeev = {self.brother}, sarita = {self.mom}, arjun = {self.father}')

obj1 = family('shiva', 'arjun', 'sarita', 'sanjeev', 'narayan');
obj1 = family(name = 'parents', mom = 'sarita', brother = 'sanjeev', me = 'shiva', father = 'arjun');
obj1.info();

class car():
    def __init__(self, car1, car2) -> None:
        self.car1 = car1
        self.car2 = car2

    def info(self):
        print(f'first car name is {self.car1}\nsecond car name is {self.car2}');

obj2 = car("audi000", "lamborgini");
obj2.info();

#decorator in python

def decorator_function(function):
    def decorated():
        print('good morning sweetheart');
        function();
        print('this is printing in the last');
    return decorated;

@decorator_function
def hello():
    print('this game is hello world');

hello();

#decorator function which takes function as argument and return function
def decorator_function(fx):
    def decorated():
        #first
        print("hello good morning");

        #second
        fx();

        #third
        print("good afternoon sweetheart");
    return decorated;

# @decorator_function
def add():
    print("hello world from shiva chaudhary")
    a = 3;
    b = 2;
    print(a+b);

#another syntax of decorator function calling 
decorator_function(add)()

#passing arguments in decorator function
def decorator_function1(function):
    def decorated(*args ):
        a = [*args];
        # b = [*kwargs];
        print(f'the sum of {a} going to happen: ');
        print(type(a));
        function(*args);
        print(f'the sum of {a} is finished');
        print(type(a));
    return decorated;

@decorator_function1
def add1(a, b):
    print(f'the sum of {a} and {b} is',a+b);
    print(type(a));
    print(type(b));

add1(2, 2);
print('\n');

def decorator_function2(furnished):
    def unfurnished(*value_a, **value_b):
        print(f'a = {value_a}', type(value_a));
        print(f'a = {value_a}', type(value_b));
        furnished(*value_a, *value_b)
        print(f'finished');
        print(f'a = {value_a}', type(value_a));
        print(f'a = {value_a}', type(value_b));
    return unfurnished;

@decorator_function2
def mul(a, b):
    print(f'{a} * {b} = {a*b}');
    print(type(a));
    print(type(b));

mul(2, 3);

#import logging
import logging
def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated
@log_function_call
def my_function(a, b):
    return a + b

#logging module
import logging

#there are five levels of logging in module 
#debug
#info
#warning
#error
#critical

logging.debug('this is debug message');
logging.info('this is info about shiva chaudhary');
logging.error('this is error message');
logging.warning('this is warning message');
logging.critical('this is critical message');

#debug
#info
#error
#warning
#critical

# import logging
# def log_function_call(func):
#     def decorated(*args, **kwargs):
#         logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
#         result = func(*args, **kwargs)
#         logging.info(f"{func.__name__} returned {result}")
#         return result
#     return decorated
# @log_function_call
# def my_function(a, b):
#     return a + b

# my_function(3, 3);

#root error message 
import logging;

def logging_function_error(function):
    def decorated(*args, **kwargs):
        logging.error(f'caliing {function.__name__} is being logged with a = {args} and b = {kwargs}')
        logging.info(f'{function.__name__} is being logged with a = {args} and b = {kwargs}')
        result = function(*args, **kwargs);
        logging.error(f'calling {function.__name__} has returned value = {result}');
        logging.info(f'{function.__name__} has returned value = {result}');
    return decorated;

@logging_function_error
def mul(a, b):
    return a * b

mul(3, 3);

#use of constructor
class movies():
    def __init__(self, name, caste) -> None:
        self.name = name;
        self.caste = caste;

    def action(self):
        print(f'{self.name} {self.caste}');
obj1 = movies('shiva', 'chaudhary');
# print(obj1);#class main movies object
obj1.action();

#use of enscapsulation 
#getter and setter
class person():
    #constructor 
    #value can be written while defining object though parameter
    def __init__(self, value) -> None:
        self._value = value;

    def info(self):
        print(f'this is comming through constructor, name = {self._value}');

    #getter value can be set in the default class
    #getter is method to create the property of the class
    @property
    def Ten_person(self):
        return 10 * ('\n', self._value);

    @Ten_person.setter
    def Ten_person(self, new_value):
        self._value = new_value * 10;

object1 = person('Anjelika rimal');
object2 = person('jevis shrestha');

object1.info();
object1.info();
object1 = person('samprad adhikari');
print(object1.Ten_person);
object1.Ten_person = 'anjelika rimal';
print(object1.Ten_person);
object1.info();
#_value = properties of object1, object2 for class person() 
# print(object1._value);
# print(object2._value);

# #number
# object3 = person(100);
# object3.info();
# print(object3.Ten_person);
# object3.info();

# object3.Ten_person = 34;

# object3.info();
# print(object3.Ten_person);
# object3.Ten_person;


