class number():

    #constructor
    def __init__(self, num1, num2, num3) -> None:
        self.num_1 = num1
        self.num_2 = num2
        self.num_3 = num3
    
    #getter 
    @property
    def calculator(self):
        lists = [self.num_1, self.num_2, self.num_3];
        result = list(map(lambda x: x * 2, lists));
        return result;

    #setter
    #we can do only put one setter at time 
    @calculator.setter
    def calculator(self, num_1):
        self.num_1 = num_1

    #method 
    def num_num(self):
        print(f'{self.num_1}, {self.num_2}, {self.num_3}');

#self = object
object1 = number(1, 2, 3);
object1.num_num();
print(object1.calculator);

#not update
object1.num_num();

#value is given to the calculator
#Method ho ni ta
object1.calculator = 4;

#updated
object1.num_num();

#getter 
print(object1.calculator);

#updated
object1.calculator = 8;

#getter
print(object1.calculator);

#give updated value
object1.num_num();

#getter and setter in the python
#getter property takes four argument 
#get_fun, set_fun, del_fun, doc_string

#creating class 
class age():
    def __init__(self, age = 4) -> None:
        self.age = age;

    #getter function 
    def get_age(self):
        print('i am inside getter function ');
        return self.age;

    #setter function - set new value
    def set_age(self, a):
        print
        ('i am inside setter function');
        self.age = a;

    #delete function
    def del_age(self):
        print('i am inside delete function');
        # del self.age;
    
    a = property(get_age, set_age, del_age);

#create instance 
instance1 = age();

#default value
print(instance1.age);

#set new value
instance1.set_age(10);

#first print age = 10
print(instance1.age);

#inside getter 
instance1.get_age();

#get updated value
print(instance1.get_age());

#del function
instance1.del_age();

#deleted value
# print(instance1.del_age());

#geting value ❌
# print(instance1.get_age());

#aready deleted property show error
# print(instance1.age);
print('\n');
class getter_setter():
    def __init__(self, name = 'jevis') -> None:
        self._name = name;

    def getter(self):
        print('i am inside getter method');
        return self._name;

    def setter(self, a):
        print('i am inside setter method');
        self._name = a;

    def delete(self):
        print('i am inside delete method');
        del self._name;

    a = property(getter, setter, delete);

obj = getter_setter();
obj.a = 'samprad';

#delete method do nt gets called 
print(obj.a);

#another method
class another_get_Set():
    def __init__(self) -> None:
        self._name = 'shiva';

    @property
    def getter(self):
        print('getter method is called');
        return self._name;

    @getter.setter
    def setter(self, n_name):
        if (n_name < 18):
            raise ValueError('your age is below eligibility criteria');
        
        print('setter method is called');
        self._name = n_name;

obj = another_get_Set();
obj.setter = 19

print(obj.setter);

#print(setter method should be called and it will call the getter method where it will return the set value and update the value);