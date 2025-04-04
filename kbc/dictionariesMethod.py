# for i in range(0, 12):
#     print('the number is {} and '.format(i+1));
#     if i == 4:
#         print('breaking');
#         break;
# else:
#     print('you are in the end of the loop');
# print('out of the loop');

'''while and for loop consist = else'''
'''break hanyo bhane exit '''
'''not printing the else'''

for j in range(5):
    for i in range(6):
        if (j == 4):
            print('breaking');
            break;
        else:
            print('not breaking');
    else:
        print('exit of the i loop');
else: 
    print('exit of the j loop');


for k in range(0, 6):
    for l in range(7):
        if(l == 1):
            print('breaking');
            break;
        else:
            print(l);
    else:
        print('exit of l loop');
else:
    print('exit of k loop');


# for i in range(0, 5):
#     for j in range(0, 6):
#         if(i == 1):
#             print('breaking');
#             break;
#         else:
#             print(i);
#     else:
#         print('exit of the loop j');
# else:
#     print('exit of i loop');

#dictionaries 
dictionary = {'name':'shiva', 'roll no':234, 'college':'madan bhandari memorial college'};
print(dictionary);
dictionary.update({'age': 23});
dictionary.update({'roll no': 345});
dictionary.update({'previous college':'nist, lainchaur'});
print(dictionary);

dict1 = dict([('country0', 'nepal'), ('country1', 'india'), ('country2', 'china'), ('contry3', 'australia'), ('country4', 'usa')]);
print(dict1);
dict1.update(dict([('country0', 'pokhara'), ('country1', 'kathmandu')]));
print(dict1);

# dict1.clear();
# dictionary.clear();
# print(dictionary);
print(dict1);

dict2 = dict([('animals1', 'cow'), ('animals2', 'bat'), ('animals3','snake'), ('animals4', 'buffalo')]);
# del dict2;#not deifned ❌
print(dict2); 
dict2.pop('animals4');
print(dict2);

dict3 = dict([('animals1', 'cow'), ('animals2', 'bat'), ('animals3','snake'), ('animals4', 'buffalo')]);
dict3.pop('animals4');
dict3.pop('animals1');
dict3.popitem();
dict3.pop('animals2');
print(dict3);

dict4 = dict([('ani1', 1), ('ani2', 2), ('ani3', 3),('ani4', 4)]);
# del dict4;
print(dict4);
del dict4['ani1'];
del dict4['ani2'];
print(dict4);   #del delete ani1 & ani2

# a = input('enter the number: ');

#value error 
# try:
#     for i in range(1, 11):
#         print(f'the multiplication of {a} x {i} = {int(a)*i}');
# except Exception as e:
#     print('value error!!!, entered value is not integer. ');

#index error 
# num = int(input('enter the number: '));
# try:
#     a = [1, 2, 3, 4, 5, 6, 7, 8];
#     print(a[num]);

# except IndexError:
    # print('index error!!! or invalid index');

#invalid syntax
# amount = input('enter the number greater than 3000: ');#str
# try:
#     if(int(amount) >= 2999):
#         print('amount is greater than 2999');

# except ValueError:
#     print('value error!!!');
# except SyntaxError:
#     print('syntax error!!!');
# except IndentationError:
#     print('indentation error!!!');
# except TypeError:
#     print('type error!!!!');

#zero division error 
# marks = 1000;
# try:
#     a = marks / 0;
#     print(a);
# except ZeroDivisionError:
#     print('zero division error !! please do not divide by the zero ');

#indentation error 
# amount1 = int(input('enter the number secret number: '));
# secret = [0, 23, 45, 67, 89];
# try:
#     def check():
#         for i in secret:
#             if (amount1 == i):
#                 return True;
#             else:
#                 return False;
#     result = check()
#     if result :
#         print('correct guess');
#     else:
        
#         print('wrong guess');
# except SyntaxError:
#     print('indentation error');

# a = 'shiva';
# b = 2
# try:
#     print(a+b);
# except TypeError:
#     print('error: \'str\' and \'int\' different types cannot be added ');

try:
    a = 'NAME';
    print(int(a));
except ValueError:
    print('number is not an integer!!!!');

#list error 
list1 = [1, 1, 2, 4];

try:
    for i in range(7):
        print('the element of list: {}'.format(list1[i]));
except IndexError:
    print('list out of range index');

def calculate(a):
    if a >= 7:
        #throw error a = 6
        b = a/(a-6);

        #throws error a = 10
        print('the value of a/a-1 is ', b);

try:
    # calculate(6);
    if __name__ == '__main__':
        calculate(10);



except ZeroDivisionError:
    print('zero divison error occured and handeled.');
except NameError:
    print('name error occured and handeled');

def add(a, b):
    sum = ((a+b)/(a-b));
    print('((a+b)/(a-b))',sum);
try:
    # add(3.0, 2.0);
    if __name__ == '__main__':
        add(45, 46);
        add(2.0, 3.0);
        add(3.0, 3.0);

except ZeroDivisionError:
    print('zero division error occured and handeled');

# f = 12;
# def zeroDivision(f):
#     b = f/0
#     print('the f/0 is', b);

# try:
#     zeroDivision(12);

# except ZeroDivisionError:
#     print('number cannot be divide by 0 in python ');

# else:
#     print(f);

# finally:
#     print('this will always executed');




# # Program to depict Raising Exception 
  
# try:  
#     raise NameError("Hi there")  # Raise Error 
# except NameError: 
#     print ("An exception") 
#     raise  # To determine whether the exception was raised or not 


# #program raising error and handeling well
# try: 
#     raise NameError('hi my name is shiva chaudhary');
#     print('raising error ');
# except NameError:
#     print('name error raised and handeled');
#     raise;  #check if raise or not

# try:
#     list2 = [1, 2, 3, 4, 5];
#     raise IndexError(list2[4]);
#     print('raising error');

# except IndexError:
#     print('index error list out of range range occured and handeled well');
#     raise;


# def function(n):
#     try:
#         ans = ['','lake baikal', 'rara lake', 'tilicho lake', 'fewa lake'];
#         for i in range(0, 4):
#             if i == n:
#                 print('what is the deepest lake in the world?? ');
#                 # for j in range(1, 5):
#                 #     print(j, ans[j] );
#                 answer = set(ans);
#                 for j in answer:
#                     print(j);
                
#                 ques = input('enter answer: ');
#                 # print(ans[1]);
#                 if ques == ans[1]:
#                     return True;
#                 else:
#                     return False;

#     except Exception as error:
#         print('error occured', error);
#         return False;
#     finally:
#         print('--------------finally----------------------')
#         ans = ['','lake baikal', 'rara lake', 'tilicho lake', 'fewa lake'];
#         answer = set(ans);
#         for i in answer:
#             print(i);

# result = function(0);
# if result:
#     print('\ncorrect answer');
# else:
#     print('\nwrong answer');

# def function(n):
#     list2 = [['lake baikal', 'rara lake', 'begnas lake', 'fewa lake'], ['Mt Everest', 'Mt kanchanjunga', 'Mt k2', 'Mt makalu'], ['kali gandaki river', 'karnali river', 'seti river', 'saptakoshi river']];
#     for i in range(0, 12):
#         if i == n:
#             for k in list2:
#                 set_i = set(k);
#                 # print(set_i);
#                 for j in range(0, 4):
#                     print(set_i)
#                 # for j in set_i:
#                 #     print(j);

# result = function(0);
# print(result);

# take = input('enter the number between 5 and 9: ');

# try:
#     if (take == 'quit'):
#             print('skiping this question');
#     elif(int(take) < 5 or int(take) > 9):
#         raise ValueError('enter the value between 5 and 9');
#     else:
#         print('you have entered the correct number');

# except Exception as error:
#     print('error: ', error);

# except ValueError:
#     print('value error was raised. enter the value between 5 and 9');

# take1 = input('enter the number between 10 and 20: ');

# try:
#     if( take1 == 'skip'):
#         print('skipping this question');
#     elif(int(take1) < 10 or int(take1) > 20):
#         raise ValueError('enter the number between 10 to 20');
#     elif(int(take1) > 10 or int(take1) < 20):
#         print('you have entered the correct number')
#     else:
#         print('enter an integer. ');
        
# except Exception as error:
#     print('error: ', error);

# finally:
#     print('this code is always executed');



##secret code converter
import random;
def function(length):
    import string;
    #taking all the lower case string from import string;
    generate = string.ascii_lowercase;
    string = ''.join(random.choice(generate) for i in range(length));
    print('random string from the import =', length, '=', string)

if __name__ == '__main__':
    reply = input('do want to decode or encode ??: ');
    str = input('what do you want to write: ')

def code(str):
        import random;
        import string;
        generate = ''.join(random.choice(string.ascii_lowercase) for i in range(3));
        generate1 = ''.join(random.choice(string.ascii_lowercase) for i in range(3));
        replaced = str.replace(str[0], '');
        firstLetter = str[0];
        replace = generate + replaced + firstLetter + generate1;
        print(f'language which has been coded \'{replace}\'');
        decode(replace);

def decode(str):
    replaced1 = str.replace(str[0:3], '');
    replaced2 = replaced1.replace(str[-3:len(str)], '');
    replaced = replaced2.replace(replaced2[-1], '')
    final_word = replaced2[-1] + replaced;
    print(f'the decode of the word \'{str}\' is ', final_word);
        
def reversed11(string):
    # print(string,type(string));
    reverse = ''.join(reversed(string));
    print(f'the language has been coded \'{reverse}\' ');

if __name__ == '__main__':
    length = len(str);
    if (length > 3):
            code(str);
    elif(length <= 3):
            reversed11(str);
    else:
        print('please enter anything to write the secret code');
# print(__name__);


# import random;
#how to generate random string of any length 
# length = int(input('enter length of string to generate: '));

#how to convert nonetype to str type
string1 = None;
# print(string1, type(string1));

string2 =  '' if string1 is None else string1;
# print(string2, type(string2));


#function to generate random words
import string;
import random;
generate = ''.join(random.choice(string.ascii_lowercase)for i in range(3));
# print(generate, type(generate));

#function = none type when generating random words 
def random2(n):
    generate1 = string.ascii_letters;
    generate2 = ''.join(random.choice(generate1)for i in range(n));
    # print(generate2, type(generate2));

# string = random2(4);
# print(string, type(string));
def fib2(n):
    a, b = 0, 1;
    list = [];
    while a < n:
        list.append(a);
        a, b = b, a+b;
    print(list);
    print(__name__);#if it run in dictionariesMethod __name__ = __main__, if it run in shorthandpy __name__ = dictionariesMethod.py

if __name__ ==  '__main__':
    fib2(25)

#fibonacci series 
def fib1(n):
    a, b = 0, 1;
    list = [];
    while a < n:
        list.append(a);
        a , b = b, a+b;

    print(list);

# from shorthand import fib1;
# fib1(1000);
# fib1(1000000);

