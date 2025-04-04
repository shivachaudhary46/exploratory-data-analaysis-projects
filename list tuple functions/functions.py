a = 34
b = 45
c = 33

arthiMean = (a + c)/2 *b ;
# print(arthiMean);

d = 45
e = 90
f = 32
arthiMeanSecond = (d + f)/ 2 *e;
# print(arthiMeanSecond);

'''we can make this more simpler by using '''

def arthimeticMean(a, b, c):
    arthimetic = a + c / 2 * b;         '''a, b, c are the arguments for this functions and only valid for this functions'''
    print(arthimetic);

first = 45
second = 50
third = 55;

# arthimeticMean(first, second, third);       '''first , second , third is parameters and giving value to a, b, c'''

'''geometric mean of the a b c number a'''
def geometricMean(a, b, c):
    geometric = a * b * c / (a + b + c);
    print(geometric);

i = 24
ii = 26
iii = 28
# geometricMean(i, ii, iii);

'''making the average of the number '''
def average(a, b, c, d, e, f):
    # 
    counter = 0; 
    while True:
        counter = counter + 1;
        if(counter > 6):
            print("breaking");
            break; 

    # 
    averageFormula = a + b + c + d + e+ f / counter;
    # print(averageFormula);

def counting_arg(*args):

    ''' so if we want to give as many as parameters in the argument when giving the value then we use "*"  '''
    ##returning the length of the args 
    return(len(args));


a = 1
b = 1
c = 1
d = 1
e = 1
f = 1
g = 1
h = 1
i = 1
j = 1

number = counting_arg(a, b, c, d, e, f, g, h, i, j);
# print("the number of the args is", number);


def counting_method_2(*args):
    lenCounting = len(args);
    print(lenCounting);

# counting_method_2();

# def counting_method_3(a, b, c, d, e, f, g, h, i, j):
#     lenCounting = len(a, b, c, d, e, f, g, h, i, j); '''len takes only one args'''
#     print(lenCounting);     """ File "C:\Users\user\OneDrive\Documents\python basics\functions.py", line 83, in <module>
#                                     counting_method_3(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
#                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#                                 File "C:\Users\user\OneDrive\Documents\python basics\functions.py", line 80, in counting_method_3
#                                     lenCounting = len(a, b, c, d, e, f, g, h, i, j);
#                                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#                                         TypeError: len() takes exactly one argument (10 given)"""
#     pass;

# counting_method_3(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

'''let me write the code for the counting the actual argument given in the functions'''
def countingAverage_1(*args):
    counting = len(args);
    # args = args + 1;   '''1 xa ni ta so tuple sanga int jodna mildena ni ta'''
    print(args, type(args));  '''args class is tuple '''
    adding = sum(args);  '''sum function convert tuple of int to class int'''
    print(counting, type(counting));    '''counting class is int'''
    averageFormula = adding / counting;     '''int/int'''
    print("the average formula of the given value is", args, "=", averageFormula);  '''19.5714'''
a = 2
b = 5
c = 20
countingAverage_1(23, 43, 12, 32, a, b, c);


'''lets try map function'''
# def mul(i):
#     return i * i;

# x = map(mul, (3, 5, 7, 11, 13));  '''map ko first argument should be the functions, second can be tuple'''
# count = list(x);
# print(count);
# # print(x);

# counter = 0
# for counting in count:
#     print(counting);
#     counter = counter + 1
#     # print(counter);


#     string = count[counter];

# convert = "".join(string);
# print(convert);



a_tuple = 23, 43, 12, 32, 2, 5, 20;
# print(a_tuple, type(a_tuple));  '''class = tuple'''


# for number in a_tuple:
#     print(number, type(number));
    
result = sum(a_tuple) / 7; 
# print(result);


def b_tuple(a, b, c, d, e):
    result = ""; '''class = string'''
    sum = a, b, c, d, e;  '''sum ko type is tuple'''
    print(sum, type(sum));
    for numberLoop in sum:
        print(numberLoop, type(numberLoop));  '''numberLoop is int'''
        result += str(numberLoop);
        return(result)
    
result = b_tuple( 2, 3, 4, 5, 6);  '''class is tuple but each is int'''
int_result = int(result);
print(int_result);


rent = "coffee shop", "car rent", "realestate";
for loop in rent:
    print(loop);

a_tuple = 3, 4, 5, 6, 7;  '''class = tuple'''
result = '';  ''' class = string'''

for number in a_tuple:
    #number = tuple but each number loop lauda kheri it is in int 
    result += str(number); #string function use 
result = int(result); #int function
print(result) # 👉️ 34567


'''converting the tuple to string and list'''
rent = "coffeeshop", "carrent", "wineshop", "buiseness";
# print(rent, type(rent));
string = " ".join(rent);
# print(string, type(string));
replace = string.replace("coffeeshop", "buiseness");
spliting = string.split();
# print(spliting, type(spliting));


numbers = 1, 2, 3, 4, 5, 6, 7;
# print(numbers, type(numbers));
string = "".join(str(numbers));          '''it only concatanate the string '''
# print(string, type(string));        '''class = string'''
# integers = int(string);     '''can't convert class tuple of string to the int'''
# print(integers, type(integers));

'''hence we can make tuple class full of the integers to the strings of their own and finally to the int by using for loop but if we use join function we can only convert to the string'''

def is_greater(a, b):
    if(a>b):
        print("a is greater than b");
    else:
        print("b is greater than a or equal to a");

c = 9
d = 9
# is_greater(c, d);

'''syntax 1 to make the function in the python'''

def adding(num1: int, num2: int) -> int:
    add = num1 + num2;
    return(add);

# num1, num2 = 15, 5;
result = adding(5, 25);
# print(result);

'''synatx for example 1 
def function_name(parameters1: data_type , *parameters2: data_type) -> return_type:
    body statement 44
    return() OR print();

function_name(arguments1, arguments2); function calling     
'''

'''calculate whwther the number is prime or not'''
# n = 3
# if n in [2, 3]:
#     print("true");
# else:
#     print("false");

def is_prime(n):
    if n in [2, 3]:
        return True;
    elif (n == 1) or (n % 2 == 0):
        return False;

    r = 3
    while r*r <= n:
        if n%r == 0:    
            return False;
        r += 2;
    return True;

# n = int(input("enter the number to check whether the is prime number or not: "))
# if (is_prime(n)):
#     print(f"{n} is prime number");
# else:
#     print(f"{n} is not prime number")

'''use of the docstring .The first string after the function is called the Document string or Docstring in short. This is used to describe the functionality of the function.'''

'''syntax : print(function_name.__doc__)'''

def oddEvenCalc(n):
    '''calculating odd or even'''
    if (n % 2 == 0):
        return True;
    else:
        return False;

# n = int(input("enter the number to check odd or even: "));
# if oddEvenCalc(n):
#     print(f"{n} is even");
# else:
#     print(f"{n} is odd");

# Python code to illustrate the cube of a number
# using lambda function
# def cube(x): 
#     return x*x*x;


# cube_v2 = lambda x : x*x*x

# print(cube(7))
# print(cube_v2(7))


def cube_x(num):
    return num*num*num;
num = 2;
# print(cube_x(num));

'''making lambda function. so lambda function is anomoyous function which is only written in one single line'''
making_cube = lambda x : x * x * x;
x = 3
# print(making_cube(x));

# making the nested function inside the function
def outside_function():
    def inside_function(n):
        if(n % 2 == 0):
            print("it is even number");
        else:
            print("it is odd number");
    num = int(input("enter the number: "));
    inside_function(num);

# outside_function();
 
defination = lambda num: print(f"the number is {num}") ;
print(defination(67));

"""there are four types of the arguments in the function
1. default argument
2. keyword argument
3. variable len gth argument
4. required argument 
"""


'''so let me give the example of the default argument'''

def default_argument(a=2, b=3, c=4, d=5):
    average = a + b + c + d / 4;
    print("the average number is", average);

default_argument();  '''example of the default argument'''

def calc_average(a=3, b=3, c=3, d=1):
    average = a + b + c + d / 4;
    print(a);
    print(b);
    print(c);
    print(d);
    print("the average number ", average);

calc_average(d=23, a=2, c=4, b=5);  """we can update it as well"""

def multiplying(num1: int, num2: int) -> int:
    mul = num2 - num1;
    return mul;

result = multiplying(num1=1, num2=1);
print(result);




'''example of key word argument'''
def lot_of_names(fname, mname, lname):
    print(f"the name is {fname} {mname} {lname}")


lot_of_names("chaudhary", "arjun", "prasad");
lot_of_names("sarita", "", "chaudhary");
lot_of_names("bahadur", "jevis", "shrestha");
lot_of_names("samprad", "adhikari", "kumar");
lot_of_names("rimal", "anjelika", ""); '''❤️❤️❤️if we write the order of the aguments and give value to parameters is called required arguments'''

'''in key word argument it will follow the order of the argument u pass. let's take the above example we have to put the firstname but we have kept the chaudhary which is last name so python is not human it does not know that chaudhary is last name'''
lot_of_names(fname="arjun", lname="chaudhary", mname="prasad"); """👈 actually this is the example of key word argument"""



'''example of the variable length argument'''
def average_number_calculate(*args):
    sum = 0;
    for each_number in args:
        # print(each_number, type(each_number));
        # print(numbers[3]);
        sum = sum + each_number;
    print(sum / len(args)); """👉😭 each_number shows only the first value given in the tuple eg:: 0 so we can't get the average numbers of the tuple but problem was because because of the return .if we are returning the value we should have used paranthesis hope it is my hypothesis. In future you would get confuse so i would tell u now. In first we are returning the value using return so it was giving the problem"""

average_number_calculate(0, 3, 4, 6, 7, 52, 43 ,5);
# print(calculate);

numbers = 1, 2, 3, 4, 4, 4;
# print(numbers, type(numbers));
# print(numbers[0]);  #👉 1 
# for number in numbers:
    # print(number);

def a_tuple(*args):
    for number in args:
        print(number);

# a_tuple(1,2,4); #😎

'''example of the required argument'''
def names_friends(fname, mname, lname):
    print(f"the name is {fname} {mname} {lname}");

names_friends("arjun", "prasad", "chaudhary");

'''function of the dict = key value pairs'''
'''note: inside paranthesis ()👈 use ** double star'''
def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"]); '''☝️name is the defination name or variable name of the dict
                                                                        fname, mname, lname are the (keys) and values are given from the function call '''

name(mname = "Buchanan", lname = "Barnes", fname = "James");

dict = dict();
dict["country1"] = "nepal";
dict["country2"] = "japan";
dict["country3"] = "australia";
print(dict);

def dictionary(**country):
    print("Country names are: ", country["fname"], country["mname"], country["lname"], type(country["fname"]));

dictionary(fname= "austrilia", mname="nepal", lname="america");  """👉this is the method to make the dicitionary but its output is showing in the string. """

def function(n):
    return n * n;

result = function(5);
print(result);

cube = lambda x : x ** 3;
square = lambda x: x ** 2;
average_num = lambda x, y, z: (x + y + z)/3
print(cube(2));
print(cube(4));

#we can pass function in the argument of the function 
def result(fx, value):
    print(fx(value) + 5);

result(function, 3);


def function_pass(cube_fx, square_fx, average_fx, c_value, s_value, x, y, z):
    return cube_fx(c_value) + square_fx(s_value) + average_fx(x, y, z);

result = function_pass(cube, square, average_num, 2, 5, 14, 78, 43);
print('the add of the cube function, square function, average function ', result);