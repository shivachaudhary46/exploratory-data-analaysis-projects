"""type of inheritance """
#single inheritance
#multiple inheritance
#multilevel inheritance
#heirchial inheritance
#hybrid inheritance

#single inheritance
class parent():
    def parent(self):
        print('parent class');

class child(parent):
    def child_method(self):
        print('child class');

objects1 = parent();

#parent object has not attribute 'child'
# objects1.child();
objects1.parent();

object_child = child();
object_child.child_method();
object_child.parent();
#multiple inheritance 
class mother():
    mothername = '';
    def mother(self):
        print(f'mother : {self.mothername}');

class father():
    fathername = '';
    def father(self):
        print(f'father : {self.fathername}');


class children(mother, father):
    def parents(self):
        #mistake, mother = class, father = class 
        print(f'mother: {self.mothername}');
        print(f'father: {self.fathername}');

obj = children();
obj.fathername = 'arjun';
obj.mothername = 'sarita';
obj.parents();

#multiple inheritance
#when two class is given to one class
#like father mother and son relation ship

class Mother:
    mothername = ""
 
    def mother(self):
        print(self.mothername)
 
 
class Father:
    fathername = ""
 
    def father(self):
        print(self.fathername)
 
 
class Son(Mother, Father):
    def parents(self):
        print("Father name is :", self.fathername)
        print("Mother :", self.mothername)
s1 = Son()
s1.fathername = "Mommy"
s1.mothername = "Daddy"
s1.parents()

#class parents 
class brother():
    brothername = 'sanjeev';
    def brother(self):
        print(f'brother: {self.brothername}');

class mother():
    mothername = 'sarita';
    def mother(self):
        print(f'mother: {self.mothername}');

class bhauju():
    bhaujuname = 'nishma';
    def bhauju(self):
        print(f'bhauju: {self.bhaujuname}');

class me(brother, mother, bhauju):
    def me(self):
        print(f'brother: {self.brothername}');
        print(f'mother: {self.mothername}');
        print(f'bhauju: {self.bhaujuname}');

print('\n');
obj = me();
obj.brothername = 'jevis';
obj.mothername = 'anjelika';
obj.bhaujuname = 'samprad';
obj.me();

#multilevel inheritance 
#when one class is inherit to another and that class is again inherit to the another class
#like grandfather grandchildren relationship

class grandfather():
    def __init__(self, grandfathername) -> None:
        self.grandfathername = grandfathername;

class father(grandfather):
    def __init__(self, grandfathername, fathername) -> None:
        self.grandfathername = grandfathername;
        self.fathername = fathername;
        grandfather.__init__(self, grandfathername);

class son(father):
    def __init__(self, grandfathername, fathername, sonname) -> None:
        self.grandfathername = grandfathername;
        self.fathername = fathername;
        self.sonname = sonname;
        father.__init__(self, grandfathername, fathername);

    def giveInfo(self):
        print(f'grandfather name: {self.grandfathername}');
        print(f'father name: {self.fathername}');
        print(f'son name: {self.sonname}');


obj = son('narayan', 'arjun', 'shiva');

obj.giveInfo();

#multi level inheritance
#grandfather and son relationship
class grandmother():
    def __init__(self, grandmothername) -> None:
        self.grandmothername = grandmothername;

class mother(grandmother):
    def __init__(self, grandmothername, mothername) -> None:
        self.mothername = mothername;
        grandmother.__init__(self, grandmothername);

class son(mother):
    def __init__(self, grandmothername, mothername, sonname) -> None:
        self.sonname = sonname;

        #this syntax must be written for the multilevel inheritance 
        mother.__init__(self, grandmothername, mothername);

    def information(self):
        print(f'grandmother name: {self.grandmothername}');
        print(f'mother name: {self.mothername}');
        print(f'son name: {self.sonname}');

obj = son('jibchi chaudhary', 'sarita chaudhary', 'shiva chaudhary');
obj.information();

#another method of multiple inheritance
#multiple inheritance 
class mother():
    def __init__(self, mothername ) -> None:
        self.mothername = mothername;

class father():
    def __init__(self, fathername ) -> None:
        self.fathername = fathername;

class son(mother, father):
    def __init__(self, mothername, fathername, sonname) -> None:
        self.sonname = sonname;
        mother.__init__(self, mothername);
        father.__init__(self, fathername);

    def informat(self):
        print(f'mother name: {self.mothername}');
        print(f'father name: {self.fathername}');
        print(f'son name: {self.sonname}');

obj = son('sarita', 'arjun', 'shiva');
obj.informat();

#heirchial inheritance
#relationship of the brother and son marriage life and more like parent and each children relation
class parent():
    def forparent(self):
        print(f'from parent class ');

class son1(parent):
    def forson1(self):
        print(f'from children one : elder');

class son2(parent):
    def forson2(self):
        print(f'from children two : younger');

objForSon1 = son1();
objForSon1.forson1();
objForSon1.forparent();

#❌
# objForSon1.forson2();

objForSon2 = son2();
objForSon2.forson2();
objForSon2.forparent();


#hybrid inheritance 
#inheritance consisting of multiple inheritance is called inheritance
class school():
    def sch_info(self):
        print(f'manasalu public secondary school');

#single inheritance
class student1(school):
    def student1(self):
        print(f'shiva chaudhary');

#heirchial inheritance
class student2(school):
    def student2(self):
        print('jevis shrestha');

#multiple inheritance 
class student3(student1, school):
    def student3(self):
        print('samprad adhikari');

objForSchool = school();
objForSchool.sch_info();

objforStudent1 = student1();
objforStudent1.sch_info();

objforStudent2 = student2();
objforStudent2.sch_info();

objforStudent3 = student3();
objforStudent3.student1();
objforStudent3.sch_info();
objforStudent3.student3();

#acess modifiers 
#there is not strict hard and fast rule for asceesing the code
#python user use as convemtion
#type
#public default modifier
#private modifier
#protected modifier

#Public modifier
class public():
    def __init__(self, name, age) -> None:
        self.name = name;
        self.age = age;
        
instance = public('shiva', 18);
instance.a = 'hello';
print(instance.a);
print(instance.name);
print(instance.age);

#pirvate modifier 
#Name mangling method -> means changing the name
class private():
    def __init__(self, name, surname) -> None:
        self.__name = name
        self.__surname = surname

    def function(self):
        print(f'my name is {self.__name} {self.__surname}')

instance1 = private('jevis', 'shrestha');

#❌
# print(instance.name);
# instance.function();

print('\n');
print(instance1._private__name)
instance1.function();

# print(instance1.__dir__())

#protected ascess modifier
class protected():
    def __init__(self, car1, car2, car3, car4) -> None:
        self._car1 = car1;
        self._car2 = car2;
        self._car3 = car3;
        self._car4 = car4;

    def fun_fun(self):
        print(f'i have four cars {self._car1}, {self._car2}, {self._car3}, {self._car4}');

class sub_protect(protected):
    pass;

objForProtected = protected('audi', 'bugati cheron', 'lamborgini', 'ferari');
print(objForProtected._car1);
objForProtected.fun_fun();

objForSubProtect = sub_protect('audi', 'bugati cheron', 'lamborgini', 'ferari');
objForSubProtect.fun_fun();
print(objForSubProtect._car3);

#library
#from method assign book and add number of book accordint to it
#show user book and number
#show number of book == len of books

class library():
    def __init__(self) -> None:
        self.num_of_book = 0;
        self.book = [];

        while True:
            self.newBook = input('enter book name or enter exit to end: ');
            self.book.append(self.newBook);
            self.num_of_book += 1;

            if self.newBook == 'exit':
                self.book.pop();
                self.num_of_book -= 1;
                break;
    
    def showresult(self):
        print('\n');
        print(f'{self.num_of_book} has been added in LIBRARY');
        
        for index, book in enumerate(self.book, 1):
            print(f'{index} {book}');

    #equals to or not
    def equalsto(self):
        if self.num_of_book == len(self.book):
            print(f'equal');
        else:
            print('not equal');

instance = library();

instance.showresult();
instance.equalsto();

#static method in python
#it is easier because we dont have to write the self  
#can call by class name or instance defined name
class Math():
    def __init__(self, num1, num2) -> None:
        self.num1 = num1;
        self.num2 = num2;

    #this n is given to the method while caling
    def function(self, n):
        self.num1 = self.num1 + n;
        self.num2 = self.num2 + n;

    @staticmethod
    def add(a, b):
        return a + b;

    @staticmethod
    def mul(a, b):
        return a * b;

    @staticmethod
    def subtract(a, b, c):
        return a - b - c;

print('for math')
instance1 = Math(3, 5);
print(instance1.num1, instance1.num2);

print('for math class: ')
instance1 = Math(4, 6);
print(instance1.num1, instance1.num2);

#updated
print('updated math with function: ')
instance1.function(3);
print(instance1.num1, instance1.num2);

print('add');
print(Math.add(2, 3));
print(instance1.add(4, 5));

print('mul');
print(Math.mul(2, 3));
print(instance1.mul(4, 5));

print('subtract');
print(Math.subtract(5, 5, 3));
print(instance1.subtract(4, 3, 2));

