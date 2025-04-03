#map function
def square(x):
    return x * x

number = [2, 4, 6, 7, 9, 1, 3, 5];
newList = map(square, number);
print(newList, type(newList));#map object, class map

newList = list(map(square, number));
print(newList);

#list lai aarko iterable list banaune 

numbers = [2, 3, 6, 4, 7, 9, 4];
def function(n):
    return n ** 3;

newList1 = [];
for num in numbers:
    newList1.append(function(num));

print(newList1, type(newList1));

number = 1, 4, 6, 7, 8, 9
list_to_tuple = list(map(lambda x: x**3, number));
print(list_to_tuple, type(list_to_tuple));

num = 1, 2, 3, 4, 5, 6, 7
a_tuple = tuple(map(lambda x: x**2, num));
print(a_tuple, type(a_tuple));

num1 = [2, 4, 6, 7, 8, 9];
num2 = [2, 4, 6, 7, 8, 9];
a_set = set(map(lambda x, y: x + y, num1, num2));
print(type(a_set));
print(a_set);

#filter builitin method in the python
def filter_fun(n):
    return n > 4;

a_filter = filter(filter_fun, num1);
print(a_filter, type(a_filter));

number = 1, 2, 3, 5, 6, 7, 8
b_filter = list(filter(filter_fun, number));
print(b_filter);

num1 = [1, 2, 3, 5];
num2 = [1, 2, 3, 5];
filterToList = list(filter((lambda x: 4>x), num1));
print(filterToList);

#map takes many argument than 3 but filter only takes 2 argument 

number = [23, 45, 67, 78, 43, 23, 53, 89, 23]
a_filter = list(filter(lambda x: x< 20, number));
print(a_filter);

number = [23, 45, 67, 78, 43, 23, 53, 89, 23]
a_filter = list(filter(lambda x:  x > 23, number));
print(a_filter);

from functools import reduce;
number = [2, 4, 5, 6, 7]
a_reduce = reduce(lambda x, y: x+y, number);
print(a_reduce);

setTool = {2, 3, 6, 4, 7, 4};
print(setTool);
a_reduce = reduce(lambda x, y: x + y, setTool);
print(a_reduce);

lists = [2, 3, 4, 5, 6, 7, 8];
a_reduce = reduce(lambda x, y : x + y , lists);
print(a_reduce);

#differences between is and == 
a = True;
b = False;
print(a is b);#exact location of memory of object
print(a == b);#equals values

a = 'string';
b = 'string';
print(a is b);
print(a == b);

print('\n');
a = 3
b = '3';
print(a == b);
print(a is b);

a = 3;
b = 3;
print(a == b);
print(a is b);

a = [1, 2, 4];
b = [1, 2, 4];
print(a == b);#check value
print(a is b);#check the object memory value 

print('\n');
a = (1, 2, 4);
b = (1, 2, 4);
print(a == b);
print(a is b);
#tuple are immutable so python place them in same memory

print('\n');
a = {1, 2, 4};
b = {1, 2, 4};
print(a == b);
print(a is b);