#if else short hand
a = 2;
b = 3;
print('a') if a > b else print('b');
print(a) if a<b else print(b);

a = 3330;
b = 3330;
# print('a') if a>b else print('b')if a == b else print('=');
a = 330
b = 3330
print("A") if a > b else print("=") if a == b else print("B");

value = True;
value1 = False;
print('true') if value1 else print('==') if value == value1 else print('false');

def function(string):
    print(string) if string else print(string);

# value = input('enter the word true or false: ');

if value == 'true':
    string = True;
else:
    string = False;

function(string);

c = 23
d = 23
print(f'c: {c} +  d: {d} = \'{c+d}\'is smaller than 23') if c+d < 23 else print(f'c: {c} and d: {d} is equal') if c == d else print(f'c: {c} + d: {d} = \'{c+d}\' is greater than 23');

# condition = input('enter the true or false: ');
# result = True if condition else False;
# print(result);

a = 2;
b = 3;
# print(a) if a < b else print('===') if a == b else print(b);


#enumerate in python

#normal
lists = ['jevis', 'shiva', 'anje', 'samprad', 'salina', 'kushum', 'ujwol', 'bishal'];

index = 0
for list in lists:
    print(list);
    if index == 3:
        print('i want to get out samprad');
        
    index += 1;

for index, list in enumerate(lists):
    print(index, list);
    if index == 1:
        print('shiva is bad boy');

animals = ['jevis', 'samprad', 'anje', 'kushum', 'salina', 'ujwol', 'dhiraj'];

for animal in enumerate(animals):
    print('\n', animal);#tuple

for ani, num in enumerate(animals):
    print(ani, num);

games = [89, 23, 54, 67, 1, 34, 0, 23, 12];

for i, game in enumerate(games):
    print(i, game);
    if i == 0:
        print('shiva has get this marks');
    
print('\n');
for i, game in enumerate(games, start=3):
    print(i, game);


for i, animal in enumerate(animals, start=1):
    print(i, animals);

friends = ['jevis', 'samprad', 'anjelika', 'ujwol', 'kushum', 'salina', 'dhiraj'];

print(enumerate(friends),type(enumerate(friends)));

l1 = ["eat", "sleep", "repeat"]
s1 = "geek"
 
# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1);

print(next(obj1), next(obj2));
 
print ("Return type:", type(obj1))
# print (list(enumerate(l1)));
 
# changing start index to 2 from 0
# print (list(enumerate(s1, 2)))#new version #❌


for i, friend in enumerate(friends):
    print(i, friend);

print('\n');
for i, friend in enumerate(friends, start=100):
    print(i, friend);

print('\n');
for friend in enumerate(friends):
    print(friend);

print('\n');
fruits = ['apple', 'orange', 'pomergranate', 'pineaple', 'papaya', 'banana'];
print(next(enumerate(fruits)));
print(next(enumerate(fruits)));
print(next(enumerate(fruits)));

object1 = enumerate(fruits);
print('the enumrate of ', object1);
for i in range(6):
    print('next element:', next(object1));

print('\n');
print(next(obj1), next(obj2));

cups = ['coffee', 'tea', 'whiskey', 'wine', 'rum', 'brandy', 'vodka'];
object2 = enumerate(cups);
print('next element: ', next(object2));
print('next element: ', next(object2));


#random series
#lower case
def random_string(n):
    import string;
    import random;
    lowercase = ''.join(random.choice(string.ascii_lowercase)for i in range(n));
    print(f'the random lowercase string is \'{lowercase}\' ')

random_string(8);
random_string(4);

#upper case
import random;
import string;
uppercase = ''.join(random.choice(string.ascii_uppercase) for i in range(3));
print(f'the random upper case string: {uppercase}');

letters = ''.join(random.choice(string.ascii_letters) for i in range(8));
print(f'the random letters of upper and lower: {letters}');

specific_letters = ''.join(random.choice('wejkanfdjisaewjn') for i in range(8));
print('specific letters: ', specific_letters);

#choice will repeat so we use sample to not repeat
# sample(string, 8);

without_repeat = ''.join(random.sample(string.ascii_lowercase, 26));
print('string without repeation of the word ', without_repeat);

without_repeat_1 = ''.join(random.sample(string.ascii_uppercase, 9));
print('string uppecase without repeation: ', without_repeat_1);


#string.ascii_letters = A-Z, a-z
#string.ascii_punctuation = @#$%^&**
#string.ascii_digits = 0-9
ranodom_generated = string.ascii_letters + string.punctuation + string.digits;
generate_password = ''.join(random.sample(ranodom_generated, 9));
print('generated password', generate_password);

printable_password = string.printable + string.ascii_letters + string.digits;
password = ''.join(random.sample(printable_password, 7));
print('the password has been created : ', password);

password1 = ''.join(random.choice(printable_password) for i in range(5));
print('printabe password ', password1);

#random 1 uppercase, 1 lowercase, 1 digits, 1 punctuations
def random_one_cases():
    import string;
    import random;
    generates = string.ascii_letters + string.digits + string.punctuation;
    #one ascii_letters 
    password = random.choice(string.ascii_lowercase);

    #one ascii_upperacase
    password += random.choice(string.ascii_uppercase);

    #One digits 
    password += random.choice(string.digits);

    #one punctuation
    password += random.choice(string.punctuation);
    print(password);
    for i in range(7):
        password += random.choice(generates);
    
    listsForPass = [];
    for i in password:
        listsForPass.append(i);
    # print(listsForPass);

    #shuffle list 
    random.SystemRandom().shuffle(listsForPass);
    stringForPass = ''.join(listsForPass);
    print('the password has been create by theh block chaun company', stringForPass);

random_one_cases();

# strings = 'abcdefg';
# lists = [];
# for i in strings:
#     lists.append(i);
# print(lists);

#virtual environment
# import pandas as pd;
# print(pd.__version__);

import random;
lists1 = ['a', 'b', 'c', 'd', 'e', 3, 4, 5];
random.SystemRandom().shuffle(lists1);
print(lists1);

lists2 = [23, 'h'];
lists1.append(lists2);
print(lists1);

lists1.extend(lists2);
print(lists1);

lists1.append('j');
print(lists1);

lists1.remove([23,'h']); #not index
print(lists1);#return error if not list.remove(x) x = null

lists1.insert(0, 'shiva');
lists1.insert(1, 'jevis');
print(lists1);

index1 = lists1.index(23);
print(index1);#return index 

animals = ['bat', 'snake', 'tiger', 'lion', 'elephant', 'cow', 'rat', 'tiger', 'lion', 'elephant'];
print(animals.count('tiger'));
print(animals.count('elephant'));

print(animals.index('tiger', 5, len(animals)));#7
animals.pop();
print(animals);
# print(animals.pop('bat'));#x = index
print(animals.pop(1)); #returns the index = value
print(animals); #update ni 😊 like delete

animals.reverse();
random.SystemRandom().shuffle(animals);
animals.reverse();
print(animals);
# print(animals.reverse());#none
# animals.clear();
# print(animals);

birds = animals.copy();
animals.append('crocodile');
birds.append('hippotamus');
print(birds);

print(animals);

stack = [2, 4, 7];
print(stack.pop(2));#x=index
print(stack);
print(stack);

#pop left only can use in collections deque
from collections import deque;
lists = deque(['shiva', 'jevis', 'anjelika', 'samprad']);
lists.append('krisha'); #arrives
lists.append(''); #arrives
lists.popleft(); #lefts
lists.popleft(); #lefts
print(lists);

squares = [];

for i in range(11):
    squares.append(i ** 2);

print(squares);

# square = list(map(lambda x : x **2, range(10)));
# print(square);

lists = [x ** 2 for x in range(11)];
print(lists);

lists1 = [[x, y] for x in (1, 3, 7) for y in (4, 3, 7) if x != y];
print(lists1);

import math;

a = math.sqrt(18);
print(a);

# import math as m;
# b = m.sqrt(9);
# print(b);
# print(type(b));
print(dir(math));
a = math.factorial(7);
print('the factorial of 7 is {}'.format(a))

b = math.perm(12);#return factorial if k paramaeters is not provide
print('the perm of the {}'.format(b));
c = math.perm(12, 4);
print(c);


from math import sqrt, degrees, pow, radians, tau;
print('print tau from math', tau);

from math import *;
print(__loader__);
print(cosh(60));



from math import sqrt, pi;
c = sqrt(12) * pi;
print(c);

import math as m;
print(m.floor(m.pi));

# from functions import is_prime;
# n = int(input('enter the number to check whether number is prime or not: '));
# if (is_prime(n)):
#     print(f'{n} is prime number');
# else:
#     print(f'{n} is composite number');


from dictionariesMethod import fib2 as fib;
fib(23);

# import importlib;
# importlib.reload('dictionariesMethod');#❌

#-------------------------------standard module
import sys;
# print(sys.ps1);#has no attribute ps1❌
# print(sys.ps2);
sys.ps1 = 'c>'; #these are available if the interpreter is in interactive mode

#how to interactive the interpreter?? ans: 
sys.path.append('/ufs/guido/lib/python');

print(sys.path); #listof the string determining the search path for the module
sys.ps1 = print('yuck');#yuck
print(sys.ps1);#none

import builtins;
print(dir(__build_class__));
print(dir(builtins));



