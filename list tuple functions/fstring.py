countries = "these are neighbouring countries {1}, {2}, {2}, {2}";
country1 = 'france';
country2 = 'italy';
country3 = 'malta'
country4 = 'sweden';
country5 = 'australia';
country6 = 'hungary';
country7 = 'urugay';
country8 = 'bolovia';
country9 = 'china';
country10 = 'romanaia';
country11 = 'greek';
country12 = 'spain';
country13 = 'india';
country14 = 'america';
country15 = 'uk';
country16 = 'nepal';
print(countries.format(country1, country2, country3, country4, country5, country6, country7));

string = 'hey , i am {1} and my country is {0}'
name = 'shiva';
print(string.format(name, country16));

price = 67.09999;
string1 = f'it is {price:.2f}';
print(string1);

float = 78.01234555555;
string2 = f'it is {float:.6f}';
print(string2);

string3 = 'we make fstring by the {gmail}'
print(string3.format(gmail = 'yuukiaasuna100@gmail.com'));

string4 = 'we make fstring by the {class1}';
print(string4.format(class1 = 1));

class_1 = 12;
print(f'i am in currently in {class_1}');

print(f'{2*8}');
string2 = f'{3*5}';
print(string2, type(string2)); 

string5=34.90009343
class_2 = f'this is the{string5:.4f}';
print(class_2);

'''fstring'''
a = 'my name is {} and i am living in the {}';
name = 'shiva';
country = 'nepal';
print(a.format(name, country));

price = 23.6777
seller = f'i want to buy for {price:.2f}';
print(seller);

price = 45.77887
seller = f'i want to buy carrot for {price:.2f}';
print(seller);

price = 45.89999;
buyer = f'i want to eat pizza ate {price:.5f}';
print(buyer);

killer = 'this is the first time i have {2} {1} in my {0}';
kill = 'kill';
people = '2 people';
life = 'whole life';
print(killer.format(kill, people, life));

'''what is doc_string'''
def numbers():
    '''this is doc string which means the text which is written after the defination of the function '''
    number = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh'];
    for num in number:
        result = f'the {num} number'
        print(result);

numbers();

print(numbers.__doc__);


'''what is doc string??'''
def countries():
    country = ['nepal', 'india', 'china', 'bangladesh', 'myanmar', 'russia', 'ukraine', 'mongolia'];
    '''this is comment'''
    for count in country:
        result = f'i am living in {count}';
        print(result);

countries();
print(countries.__doc__);#❌none

#doc string
#doc string
#it is string used to document a Python module, class, function or method

'''recursion in the python''' 
def recursion(num):
    if num == 1 or num == 0:
        return 1;
    else:
        return num * recursion(num-1);

result = recursion(7);
print('the recursion of the 7', result);

result = recursion(10);
print('the recursion of the 10', result);

def recursion1(n):
    if n == 1 or n == 0:
        return 1;
    else:
        return n * recursion1(n-1);

result1 = recursion1(12);
print('the recursion of the 12', result1);

#fibonacci series 
def fibonacci(n):        
    if (n == 1 ):
        return 1;
    elif (n == 0):
        return 0;
    else:
        return fibonacci(n-1) + fibonacci(n-2);
        # print(i);

def fibonacci_calc():
    def numbers():
        series = ['first', 'second', 'third', 'forth', 'fifth', 'sixth', 'seventh', 'eight', 'ninth', 'tenth', 'eleventh', 'twelevth'];
        for i in range(12):
            return series[i];

    number = numbers();

    n = int(input("how many fibonacci series you want to print: "));
        #checking 
    if n <= 0:
        print("please enter the positive number");
        n = int(input('how many fibonacci series you want to print: '));
    else: 
        for i in range(n):
            result2 = fibonacci(i);
            print(f"the {number} fibonacci series of : {result2}");

# fibonacci_calc();

'''fibonacci series using recursion'''
def fibonacci_series(n):
    if (n == 0):
        return 0;
    elif (n == 1):
        return 1;
    else:
        return fibonacci(n-1)+fibonacci(n-2);

# user = int(input("enter how many fibonacci series you want to print: "));
# #checking 
# if user <= 0:
#     print("enter the positive integer.");
#     #update
#     user = int(input("enter how many fibonacci series you want to print: "));
# else:
#     for i in range(user):
#         print(fibonacci_series(i));
    
#fibonacci series using formula
num1, num2 = 0, 1;
count = 0;

#input 
# user1 = int(input('enter how many fibonacci series you want to print: '));
# user1 -= 2;
# #checking 
# if user1 <= 0:
#     #update
#     user1 = int(input('enter the positive number: '));
#     user1 -= 2;
#     print(num1);
#     print(num2);
#     while count < user1:
#             nth = num1 + num2;
#             num1 = num2;
#             num2 = nth;
#             print(nth);
#             count += 1;
    
# else:
    
    # print(num1);
    # print(num2);
    # while count < user1:
    #         nth = num1 + num2;
    #         num1 = num2;
    #         num2 = nth;
    #         print(nth);
    #         count += 1;

#fibonacci series using formula in python 
# counter = 0; 
# n1, n2 = 0, 1;

# user2 = int(input('how many fibonacci series you want to print: '));
# user2 -= 2;
# if (user2 <= 0):
#     user2 = int(input('enter the positive number: '));

# else:
#     print(n1);
#     print(n2);
#     while counter < user2:
#         sum = n1 + n2;
#         print(sum);
#         n1 = n2;
#         n2 = sum;
#         counter += 1;

##fibonaci series +
def fibo(n):
    if n == 1:
        return 1;
    elif n == 0:
        return 0;
    else:
        return fibo(n-1) + fibo(n-2);

# user = int(input("enter how many series you want to print: "));
# if (user <= 0):
#     user = int(input('enter the positive number'));

# for i in range(user):
#     print(fibo(i));

#what is recursion in the python
def recursion(n):
    if n == 1 or n == 0:
        return 1;
    else:
        return n * recursion(n-1);

# take_input = int(input('enter the number for the recursion: '));
# result = recursion(take_input);
# print(f"the reucrsion of the {take_input} is: ", result);


ans1 = ['','lake baikal', 'lake rara', 'fewa lake', 'begnas lake'];
ans2 = ['', 'karnali river', 'saptakoshi river', 'koshi river', 'panchpokhari river'];

question = ['','what is the deepest lake in the nepal? ', 'what is the longest river in the nepal? ', 'what is your dad name? ', 'what is your mom name'];

# try for kbc
def question1(string):
    print('\n', string);

def answer(ans):
    print(ans);

for i in range(1, 2):
    question1(question[i]);
    for i in range(1, 5):
        answer(ans1[i]);
    
'''set in the pyhton'''
'''set cant contain dict, list'''
'''does not maintain order'''
set2 = {};
print(set2, type(set2));

set1 = {1, 2, 3, 4, 5};
print(set1);

values = {True, "false", False, 12, 'mehendi', 12, 13, 'mehendi', 89, 90};
print(values)

for i in values:
    print(i);


empty_set = set();
print(empty_set, type(empty_set));

print(set1);
print(set1);
print(set1);

value = {1, 'a', 'z', 'y', 'b', 'f', 'm', 2, 10, 'k', 'k', 'a', 'b', True, False, True, False};

print(value);
print(value);

ans1 = {'','lake baikal', 'lake rara', 'tilicho lake', 'begnas lake'};
print(ans1);

ans2 = {'','karnali river', 'saptakoshi river', 'koshi rivier', 'mailiung river'};
print(ans2);

# for i in range(1, 2):
#     print(i);

countries1 = {'tokyo', 'india', 'mumbai', 'kathmandu', 'pokhara', 'yokohama', 'texas', 'sydney'};
countries2 = {'nepal', 'malyasia', 'phillipines', 'punjab', 'vishakapatnam'};
print(countries1.isdisjoint(countries2));

country1 = {'nepal',};
country2 = {'india',};
country = country1.isdisjoint(country2);
print(country);

print(country1, type(country1));

animal1 = {'bat','cat','cow'};
animal2 = {'bat', 'cow', 'snake'};
print(animal1.union(animal2));#❌not update
print(animal1);
print(animal1.update(animal2));

books = {'physics', 'maths', 'nepali', 'chemestry',};
books1 = {'english', 'account'};
books.update(books1);
print(books);

wine = {'a', 'b', 'c', 'a', 'b', 'c'};
numbers = {1, 2, 3, 4, };
print(wine.intersection(numbers));

wine2 = {'a', 'b', 'c'};
print(wine.intersection(wine2));

cups = {'wine', 'whiskey', 'beer', 'juice', 'orange'};
cups1 = {'apple juice', 'water', 'coffee', 'whiskey'};
print(cups.intersection(cups1));

# cups.intersection_update(cups1);
print(cups);#updated = whiskey

# cups.update(cups1);
print(cups);

print(wine.union(cups));

print(cups.issuperset(cups1));
print(wine2.issuperset(cups));

print('\n');
laptops = {'dell', 'macbook', 'insipiron 1500 series', 'asus gaming'};
laptops1 = {'acer', 'ibm 1500', 'macbook', 'asus gaming'};
print(laptops.issuperset(laptops1));
print(laptops.issubset(laptops1));
print(laptops.issubset(laptops1));

laptops.update(laptops1);
print(laptops);

print(laptops.issuperset(laptops1));

laptops1.add('dell 1500');
print(laptops1);

cups.add('tea cupp');
print(cups);

cups3 = {'tea cupp', 'orange', 'beer', 'wine', 'whiskey'};
cups.discard(cups3);
print(cups)

letter = {'a','b','c','d','e','f'};
# let = {'a', 'b'};
# letter.discard(let);
# print(letter);
letter.discard('a');
letter.discard('b');
letter.remove('d');
print(letter);
letter.discard('z');
print(letter);
letter.remove('e');
letter.remove('f');
letter.remove('c');
print(letter);
print(letter, type(letter));

landmark = {'eifiel tower', 'land of the pisa', 'hanging babylon of the garden', 'imperium'};
print(landmark.pop());
print(landmark);
# del landmark;
# print(landmark);
landmark.clear();
print(landmark);

random = {True, False, 'shiva', 'jevis', 'samprad', 45, 90};
if True in random:
    print('true is present');
else:
    print('true is absent');






