#dunder method ??
#d for double and under for underscore method

from typing import Any


class Employee():
    def __init__(self, emp_name, emp_id) -> None:
        self._emp_name = emp_name;
        self._emp_id = emp_id;

    def __len__(self):
        i = 0;
        for c in self._emp_name:
            i += 1;
        return i;

    def __str__(self) -> str:
        return f'from string dunder method {self._emp_name} -> __str__'
    
    def __call__(self):
        return (f'im from call method');

    def __repr__(self) -> str:
        return f'from repr dunder method {self._emp_name} -> which returns string which can be rewrite by the users '

if __name__ == '__main__':
    objectEmp = Employee('jevis', '202');
    print(len(objectEmp));
    print(str(objectEmp));
    print(objectEmp());
    print(repr(objectEmp));

class square():
    def __init__(self, x, y) -> None:
        self.x = x;
        self.y = y;

    def area(self):
        return self.x * self.y;

rectangle = square(3, 5);
print(rectangle.area());

class circle(square):
    def __init__(self, r) -> None:
        self.r = r;

        #we can update the inherit constructor
        super().__init__(r, r);

    def circleFor(self):
        return 3.14 * super().area();

areaOfCircle = circle(5);

#❌
print(areaOfCircle.circleFor());

#employee for the method overriding 
class manager():
    def __init__(self, man_id, man_name) -> None:
        self._man_id = man_id;
        self._man_name = man_name;

    def infoMan(self):
        return (f'name is {self._man_name} and his id {self._man_id}')

class employee(manager):
    def __init__(self, emp_id, emp_name) -> None:
        self._emp_id = emp_id;
        self._emp_name = emp_name;

        #updated man_id to emp_id, man_name to emp_name
        super().__init__(emp_id, emp_name);

    def info(self):
        return super().infoMan();

obj = employee(102, 'jevis');
print(obj.info());

#method overriding 
class ceo():
    def __init__(self, ceo_name, ceo_id) -> None:
        self.__ceo_name = ceo_name;
        self.__ceo_id = ceo_id;

    def infoFor(self):
        return f'name is {self.__ceo_name} and id is {self.__ceo_id}';

class HrManager(ceo):
    def __init__(self, man_name, man_id) -> None:
        super().__init__(man_name, man_id);

    def infoFor(self):
        return super().infoFor();
        
Employer = HrManager('shiva', 201);
print(Employer.infoFor());

#rename the files through using class

#import os
import os;
path = 'C:/Users/user/OneDrive/Documents/python basics/cutter1'

class clearTheCutter():
    def __init__(self, userfile, which) -> None:
        self._userfile = userfile;
        self._which = which;

    #check whether the user file name has .PNG OR NOT returns with add '.png'  if not
    def check_if_add(self):
        #add decorator with func as argument
        def decorator(func):
            #takes the *args as self._user
            def decorated(*args, **kwds):
                result = func(*args, **kwds);
                print(result);
            return decorated;

        @decorator
        def check_png(a):
            if not a.endswith(self._which):
                return a[0:-4] + self._which;
            else:
                return a;
        
        #giving self._userfile to check
        check_png(self._userfile);

    # @classmethod
    # #files is the cutter each file names another method 
    # def check(name, file):
    #     if not file.endswith('.png'):
    #         n = file + '.png';
    #         return name(n);

class rename(clearTheCutter):
    def __init__(self, userfile, which) -> None:
        self.path = 'C:/Users/user/OneDrive/Documents/python basics/cutter1';
        super().__init__(userfile, which);

    @property
    def get(self):
        #show the changed name in the format of list
        lists = list(map(lambda x: x, os.listdir(self.path)));
        return lists;
    
    @get.setter
    def setFor(self, which):
        self._which = which;
        try:
            i = 0;  
            for file in os.listdir(self.path):
                self._old = os.path.join(self.path, file);
                self._new = 'new' + str(i) + self._which
                self._new = os.path.join(self.path, self._new);

                #renaming with os.rename
                os.rename(self._old, self._new);
                i += 1; 
        except Exception as e:
            print(e);           

    def check_if_add(self):
        return super().check_if_add();      
    
# which = input('which type file you want to cutt: ');
# for files in os.listdir(path):
#     file1 = clearTheCutter(files, which);

# file2 = rename('shiva', '.png');
# file2.setFor = '.png';

#operator oveloading 
class vector():
    def __init__(self, i, j, k) -> None:
        self.i = i;
        self.j = j;
        self.k = k;

    def __str__(self):
        return f'{self.i}i + {self.j}j + {self.k}k';

    def __add__(self, x):
        # return f'{self.i + x.i}i + {self.j + x.j}j + {self.k + x.k}k'
        return vector(self.i + x.i, self.j + x.j, self.k + x.k);

    #example of the operator overloading
    def __sub__(self, x):
        #pow = x^y
        return pow(self.i, x.i);

    def __mul__(self, c):
        return vector(self.i * (c.i + c.j + c.k), self.j * (c.i + c.j + c.k), self.k * (c.i + c.j + c.k) );

num1 = vector(2, 3, 4);
print(str(num1))

num2 = vector(4, 3, 2)
print(str(num2));


print(num1 + num2);

#means that operator overloading in the python means that we can change the operator and its type in the class
# binary operator overloaded 
print(type(num1 + num2));

#calling the function
print(num1 - num2);
print(num2-num1);
print(num1 * num2);

#class method
print(vector.__mul__(num1, num2));

#instance method
print(num1.__mul__(num2));

class overloading():
    def __init__(self, a, b) -> None:
        self.a = a;
        self.b = b;

    def __add__(self, other):
        return complex(self.a + other.a, self.b + other.b);

num1 = overloading(1, 2);
num2 = overloading(2, 3);

print(num1 + num2);
print(type(num1 + num2));

class greater():
    def __init__(self, a) -> None:
        self.a = a;
    
    def __gt__(self, other):
        if (self.a>other.a):
            return True;
        else:
            return False;

obj = greater(3);
obj1 = greater(5);
if obj > obj1 :
    print(f'obj is greater than obj1 ')
else:
    print(f'obj1 is greater than obj')

import os;
print(os.getcwd());



