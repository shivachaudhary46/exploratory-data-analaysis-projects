integer_data_type = [23, 32, 3, 0, 4, 6, 1, 5, 89];
print(integer_data_type, type(integer_data_type), type(integer_data_type[0]));

integer_data_type_1 = [2, 4, 5, 6, 7, 8, 9];
print(integer_data_type_1, type(integer_data_type_1[3]));

string_list = ["shiva", "jevis", "samprad", "ujwol", "anjelika", "krisha"];
print(string_list);
print(string_list[0], type(string_list[1]));
print(len(string_list));

"""list is the collection of the datatypes it can be string, int, list, tuple as well inside the list"""
collection = [1, "jevis", 21, [1, 2, 3], (2, "shiva"), {"name":"jevis", "reading":"bsc csit"}];
print(collection);

'''indexing in list follows syntax ==>   print(name(start: end: jump_index))'''
"""indexing in the datatypes"""
integer = [2, 4, 5, 6, 7, 8, 9];
print(integer[:]);  #👉python will give the default number in the [0:0]
print(integer[0:2]) #😎2, 4
"""negative indexing in the python"""
print(integer[0:-2]); # len(integer) = 7 = 7-2= 5  output###👉 2,4 ,5,6, 7
print(integer[-5:-3]) # 2:4,    #### 5, 6;
print(integer[-7: -3]); #0:4 #### 2, 4, 5, 6
print(integer[0:7:3]); #2, 6, 9

string_data_type = ["jevis", "shiva", "ujwol", "samprad", "anjelika", "krisha", "jenish", "dhiraj", "bishal"];
print(string_data_type[0:9]);  ### all
print(string_data_type[-3: -1]); ## 6:8  ##jenish, dhiraj
print(string_data_type[::-1]); ### reversed
print(string_data_type[::2]); ###jump index with the 2; ##start:end:junpindex """jevis, ujwol, anjelika, jenish, bishal"""
print(string_data_type[-8:-1:3]); #1:8:3  => shiva, anjelika, dhiraj;

colors = ["violets", "indigo", "blue", "green", "orange", "yellow", "red", "skyblue", "brown", "black", "purple"];

if "yellow" in colors:
    print("yellow color is in colors");
else:
    print("yellow color is not in colors");

if "white" in colors:
    print("white color is inside");
else:
    print("white color is not inside");

if "shishir" in string_data_type:
    print("shishir is our friend");
else:
    print("shishir is not our friend");

if "jevis" in string_data_type:
    print("jevis is our friend");
else:
    print("jevis is not our friend");

print(string_data_type[-7:-1:2]);  #2:8:2   #ujwol, anjelika, jenish
print(string_data_type[-2:-1]); #7:8 #dhiraj


'''list comprehension in the list diagram'''
animals = ["tiger", "elephant", "leopard", "cat", "dog", "cow", "snake", "horse", "rhinoceorosous", "giraffe"];
print(animals);
animalsWIth_e = [ani_e for ani_e in animals if "e" in ani_e];
print(animalsWIth_e);

animalsWith_o = [ani_o for ani_o in animals if "o" in ani_o];
print(animalsWith_o);

'''let me write list comprehension syntax 
variable_names = [expression(eg:i*i) for iterating_name(eg:i) in iterable(eg:list, dicitionary, set, tuple, array, string) if condition ]'''
animalsLetter_5 = [anima_5 for anima_5 in animals if len(anima_5) > 5];
print(animalsLetter_5);


numbers = [1, 4, 5, 67, 23, 67, 23, 54, 23, 54, 23,76];
numbers_20 = [number for number in numbers if number > 20]; #😎(❁´◡`❁)printing number greater than 20
print(numbers_20); 

list = [];
print("the list is empty");
print(list);

"""entering the list with the numbers"""
list = [1, 2, 3, 4, 5, 6, 7];
print("the new list is ", list);

"""making new list with string """;  """we can update the list with old variable to the new variable😔😔😔"""
list = ["tv", "cup board", "clock", "table", "wishkey", "wine", "statue"];
print(list);
print(list[0]); #✅tv
print(list[:4]); #✅tv, cup board, clock, table
print(list[-5:-2]); #✅2:5, clock, table, whiskey

"""ascessing multi dimensional list """
multi_list = [["jevis", "shrestha"], "anjelika", ["samprad", "adhikari"], "shiva"];
print(multi_list[0][1], type(multi_list[0][1]));  #👉first [0] position -> llst👉["jevis", "shrestha"] [1]-> shrestha, class = "string"
print(multi_list[1][0]); #✅[1] = anjelika, [0] = a
print(multi_list[2][1]); #✅adihkari, class = string
print(multi_list[3][4]); #3 = shiva, 4 = a
# print(multi_list[3][4][1]); #❌
# print(multi_list[3][1,2]);  #❌

#using len function to count the lenght of the list
calc_length = [1, 2, 3, 4, 5, 6, 7, 8];
print(len(calc_length));


"""taking input as the list"""
# input_taking_list = input("enter the list, (space separated): ");
# print(input_taking_list, type(input_taking_list));
# convert_list = input_taking_list.split();
# print(convert_list);

"""taking the integer element fromthe user """; # ❌❌❌❌❌❌❌❌❌❌❌
# n = int(input("how many number you want to enter: "));
# list_created = list(map(int, input("enter integers (space separated): \n").strip().split()))[:n];
# print(list_created);

# input size of the list
# n = int(input("Enter the size of list : "));  #this method mistake '❌❌❌❌❌❌❌❌❌
# # store integers in a list using map,
# # split and strip functions
# lst = list(map(int, input("Enter the integer\
# elements:").strip().split()))[:n]
 
# # printing the list
# print('The list is:', lst);

#adding list element with the append method
"""empty list"""
list = [];
print("the list is empty: ");
print(list);

'''adding by the append method'''
'''append is function which is used to add the element to the list'''
list.append(2);
list.append(45);
list.append(56);

print("after addding the element by append method: ", list);

"""adding the element by using for loop"""
for element in range(0, 6):
    list.append(element);
print("after adding the element by using for loop: ", list);

"""adding the tuple in the list"""
a_tuple = (1, 2, 4);
# list.append(2, 3, 4);  #❌❌❌❌(append takes only one argument)
list.append(a_tuple);
print("after adding the tuple in the list: ", list);



"""adding the list in the list"""
list_2 = ["hooray", "finish"];
list.append(list_2);
print("list after adding the list in the list: ", list);

"""summary✅✅✅✅✅"""
list = [];
print(list);
list.append(1);
list.append(2);
list.append(3);
print(list);
for i in range(4, 7):
    list.append(i);
print(list);
tuple_add_list = (7, 8, 9);
list.append(tuple_add_list);
print(list);
list_add_list = [10, 11, 12];
list.append(list_add_list);
print(list);

"""using insert element in the list✅✅"""
"""insert() function replace the value or insert the value at the specific position"""
"""insert() syntax: list.insert(position, value you want to insert)"""

"""using insert function"""
print("using insert function: ");
list_insert_function = [67, 78, 89, 90, 23]; ###positions [0, 1, 2, 3, 4]
print(list_insert_function);
list_insert_function.insert(0, 78); 
list_insert_function.insert(1, "34");
list_insert_function.insert(2, "shiva");
list_insert_function.insert(3, "jevis");
list_insert_function.insert(4, 23);
list_insert_function.insert(5, 45); #☝️positions [0=78, 1=34, 2=shiva, 3=jevis, 4=23, 5=45, 6=67, 7=78, 8=89, 9=90, 10=23]
print(list_insert_function);
list_insert_function.insert(8, 66); #☝️positions [0=78, 1=34, 2=shiva, 3=jevis, 4=23, 5=45, 6=67, 7=78, 8=66, 9=89, 10=90, 11=23]
print(list_insert_function);

'''using extend function in the list'''
print("extend function takes one argument and add at the end of the list: ");
list_using_extend = [23, 43, 58, 49]; #position = 0, 1, 2, 3
print(list_using_extend);
# empty_list = [];
# print(empty_list);

#extend function using in the list 
list_3 = [90, "jevis", "shrestha"]; ###extend function takes only one argument so we are making them variable😊
list_using_extend.extend(list_3);       #position = 4, 5, 6✅✅✅✅
print("extend function after using list_3, ", list_using_extend);
list_4 = ["shiva", "chaudhary"];
list_using_extend.extend(list_4);       ##position = 7, 8✅✅✅✅✅
print("extend function after adding the list_4, ",list_using_extend);
list_5 = ["samprad" ,"adhikari"]
list_using_extend.extend(list_5);       ##position = 9, 10✅✅✅✅✅
print("extend function after adding the list_5, ", list_using_extend);

"""extend function does not change position ✅✅✅"""
"""asccesing the list aitem and extending in the extend_list"""
ascessing = list_using_extend[5:9]; ###😎(●'◡'●)posi = 5=jevis, 6=shrestha, 7=shiva, 8=chaudhary
list_using_extend.extend(ascessing); ###👇position = 11 = jevis, 12 = shrestha, 13 = shiva, 14 = chaudhary
print("after asscessing the 5, 6, 7, 8 adding in the extend_function, ", list_using_extend);

'''using the reverse function''';
reverse_function = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
print("\ndefault", reverse_function);
reverse_function.reverse();
print("after using reverse function, ", reverse_function);

list_using_extend.reverse();
print("extend_list function reversing function, ", list_using_extend);

list_reverse  = [1, 2, 3, 5];
reverse_list = list_reverse.reverse();
print(reverse_list); #none because reverse function does not return the value 

"""another method using the reverse👇👇"""
print(list_using_extend[::-1]);  ##start:end:jumpover if 1 bhaye bhane j xa tei dekhauxa but -1 bhaye bhane ulto hunxa

print("reversed function, "); """The reversed() function returns a reverse iterator, which can be converted to a list using the list() function.👈"""

list_reversed = [1, 2, 3, 4, 5, 6, 7];
# reversing_list = list(reversed(list_reversed));❌❌

# print(reversing_list, type(reversing_list));  """output = <list_reverseiterator object at 0x000001DA77606D70> / class = list_reverseiterator"""

# convert_list = "".join(str(reversing_list));
# print(convert_list, type(convert_list)); """class = string  ❌❌❌❌❌❌"""

# convert_list_2 = convert_list.split();
# print(convert_list_2);    """['<list_reverseiterator', 'object', 'at', '0x000001E4ECD77070>']❌❌❌❌❌"""

words = "Hello my name is Bob"
reverse_word = ' '.join(reversed(words.split(' ')))
print(reverse_word);

words2 = words.split(' ');
print(words2);      #same

words3 = words.split();
print(words3);      #same

if (words2 == words3):
    print(True);
else:
    print(False);

reverse = ''.join(reversed(words));
print(reverse);

reverse0 = ' '.join(reversed(words));
print(reverse0);

reverse1 = ''.join(reversed(words.split()));
print(reverse1);

reverse2 = ' '.join(reversed(words.split()));
print(reverse2);

myname = "shiva is my name";
reversing0 = ' '.join(reversed(myname));
print(reversing0);

reversing1 = ' '.join(reversed(myname.split(' ')));
print(reversing1);

numbers5 = [1, 56, 78, 34, 53];
revnumber = ' '.join(reversed(str(numbers5).split()));
print(revnumber, type(revnumber));

# revnumber1 = ' '.join(reversed(numbers5.split())); #❌
# print(revnumber1);

# revnumber2 = ' '.join(reversed(numbers5).split());  #❌ list iterator has no attribute 'split'
# print(revnumber2);

#remove removes list by the value
numbers_5 = [1, 2, 3, 4, 5];
print("initial list, ", numbers_5);

#removing
numbers_5.remove(4);
numbers_5.remove(5);
print(numbers_5);

#removing as list
# numbers_3 = [1, 2, 3];  # list.remove(list❌)
# numbers_5.remove(numbers_3);

# for loop
for i in range(1, 3):
    numbers_5.remove(i);

print(numbers_5);

#using pop()
#removes the last element 
#if index given removes that
#pop removes by index
poplist = [2, 3, 4, 64, 45];
print("poplist", poplist);

poplist.pop();
print(poplist);

print(poplist.pop(0)); #return 2
print(poplist);

poplist.pop(2);
print(poplist);

# poplist.pop(2); #out of range❌
# print(poplist);

#list comprehension
odd_square = [x ** 2 for x in range(1, 11) if x %2 == 1];
print(odd_square);

even_square = [x**2 for x in range(1, 11) if x %2 == 0];
print(even_square);

#using function
def odd_calc():
    odd = [];
    for i in range(1, 11):
        if i % 2 == 1:
            odd.append(i ** 2);
    print(odd);

#function call
odd_calc();


def even_calc():
    even = [];
    for i in range(1, 11):
        if i%2==0:
            even.append(i**2);
    return even

result = even_calc();
print(result);

#prime number calculator 
def is_prime(n):
    if n == 1 or n % 2 == 0:
        return False;
    elif n == 2 or n == 3:
        return True;

    r = 3
    while r*r <= n:
        if(n%r == 0):
            return False;
        r += 2;
    return True;

# n = int(input("enter the number: "));
# if is_prime(n):
#     print(f"{n} is prime number");
# else:
#     print(f"{n} is composite number");

#sort method 
#in the asceding order
numbers2 = [23, 42, 34, 1, 89, 2, 2, 3, 1, 78, 90, 56, 89, 78, 56];
# numbers2.sort();
# print(numbers2);
numbers2.sort(reverse=True);#desceding order
print(numbers2);

numbers3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1];
# numbers3.sort();  #asceding order
print(numbers3); #same
numbers3.sort(reverse=True);    #same #desceding order
print(numbers3);

string = ["b", "d", "g", "z", "k", "y", "m", "a", "A", "B", "n", "H", "i", "Z"]; #1st capital and then small letter
string.sort();
print(string);

animals = ["bat", "elephant", "snake", "hippotamus", "horse", "cow", "dog", "deer", "dolphin", "deermom", 'deeerdad'];
print(animals.sort()); #none
# animals.sort();
animals.sort();
print(animals);
animals.sort(reverse=True); #z-a
print(animals);

#count() -> return value
count_num = [1, 1, 1, 1, 1, 1, 1];
print(count_num.count(1));

count_1 = [1, 1, 2, 2, 3, 3];
count_1.sort(reverse=True);
# count_1.count(1);
print(count_1);
print(count_1.count(2));
print(count_1.count(3));
print(count_1.count(4));    #return 0 if not

#reverse() -> don't return value
reverse3 = ["jevis", "shiva", "samprad", "ujwol", "anje", "shovit", "rajul"];
reverse3.reverse();
print(reverse3);

reverse4 = [23, 32, 54, 76, 87];
reverse4.reverse();
print(reverse4);

#index function -> returns value
text = ["a", "d", "e", "z"];
print(text.index("a"));
print(text.index("z"));
# text.index(0);  #❌show error
print(text);

#copy function
l = [67, 0, 23, 56, 78];
print(l);
m = l;  #refernce 
m[0] = 2;
print(l);   #value replace bcoz reference
print(m);   #reference 

a = [2, 78, 3, 67];
b = a.copy();
b[0] = 34;
print(a);   #does not replace
print(b);   #replace

#concatanate list
a = [3, 8, 9];
b = [4, 3, 9];
c = a + b;
print(a);
print(b);
print(c);

#insert();
insert = ["jevis", "shiva", "samprad"];
print(insert);
insert.insert(0, "ujwol");
print(insert);
insert.insert(3, "anjelika")
print(insert);

#append();
append = [1, 4, 6, 7];
print(append);
append.append(5);
print(append);
append.append(7);
print(append);
append_1 = [3, 4];
append.append(append_1);    #[1, 4, 6, 7, 5, 7, [3, 4]]
print(append);

#extend()
extend = [2, 3, 5, 6];
print(extend);
extend1 = [2, 3];
extend.extend(extend1); #[2, 3, 5, 6, 2, 3]
print(extend);
