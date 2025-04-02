string = "hello My name is shiva chaudhary";
a = "malfunction"
b = "shiva"

# print(a + b);
c = """this guy is fabulous
this woman is wealthy 
I like her
because she is so gorgeous""" 
# print(c);

# print(string[0]);
# print(string[5]);
# print(string[6]);
# print(string[7]);

# for character in c:
    # print(character);

# for orentation in string:
    # print(orentation);

# for character in b :
    # print(character);

# for person in c:
    # print(person
    # 
    # 
fruits = "mango";
fruits2 = "banana";
books = "rich by robert kiyosaki";
pencil = "apsara";

# print(fruits[0]); #m
# print(fruits[4]); #o
# # print(fruits[5]); #error string index out of range
# print(fruits2[2]) # t 
# print(books[8]); # r
# print(pencil[0]); # ==a
# print(pencil[1]); # p
# print(pencil[2]); #s
# print(pencil[5]); #a
# print("\nwe are doing loops in the pencil: \n");


# for looping in pencil:
    # print(looping);

# print("\nwe are doing loops in fruits: \n");

# for loopingFruits in fruits:
#     print("\n", loopingFruits);

# print("\n we are doing loops in the fruits2")

# for loopingFruits2 in fruits2:
#     print("\n", loopingFruits2);

# print("\n we are doing loops in ban of the fruits2= \"banana\" ");

# for loopingFruits2 in fruits2[0], fruits2[1], fruits2[2]:
#     print(loopingFruits2);

# print("\n we are doing loops in the dicitionary: \n")

# creating dictionary 
dictionary = dict({0: "jevis", 1: "shiva", 2: "samprad", 3: "anje", 4:"ujwol"});

# for loopingDict in dictionary:
#     print(loopingDict);

""" hence if we do loop in dicitionary it will only give you the key not the value because dicitionary is the key value pair"""

""" creating list """
list4 = [1, 2, 3, "jevis", "samprad", "anjelika", ["krisha", "samprad"]];

# print("\ncreating loop in the list4: \n");
# for loopingList in list4:
#     print(loopingList);

""" creating tuple """
tuple = (1, 2, 3, ("jevis", "shrestha",), "samprad", "anjelika");

#loopinf tuple 
# print("\n creating loop in tuple so we can check whether it works: \n");
# for loopingTuple in tuple[0], tuple[1], tuple[2]:
    # print(loopingTuple);

""" so we can do loop in the tuple"""

"""so we can write multi line code in string with the use of (triple double quote or single quote """ """ & ''' ''') """

""" slicing in the python """
name = "harry";
nameLen = len(name);
# print(nameLen);
# print(name[len(name)-4:len(name)-2]); # ar   print(name[len(name)-4: len(name)-2]);
# print(name[-4:-2]); #these are same 

fruits = "pineapple";
# print(fruits[0:8]); # pineappl
# print(fruits[-2:-8]); # 7:1  #it does not takkes hai ta
# print(fruits[-8:-2]);   #1:7

books = "rich dad poor dad";
# print(books[0:len(books)-4]);  #17-3 = 14 

drinks = "could you pass me a coffee??"
# print(drinks[0:len(drinks)-9]); #  0: 19 
# print(len(drinks));

drinks2 = "vodka is my favourite";
# print(drinks2[0:12], "drinks");

animals = "gorilla likes banana";
# print(animals[0:7]);

drinks3 = "wine glass is my favourite";
# print(drinks3[0:4]);
# print(drinks3[5:10]);
# print(drinks3[11:13]);
# print(drinks3[:]);


characters = "A B C D E F"
# print("\nlooping the characters in the python\n ");

# for loopingChar in characters:
#     print("\n\n",loopingChar);


# print("\n printing the only character of" + "3 and -1 of fruits3\n: ");
# print(drinks3[3:-1]);


""" we can do reversing in the pyhton string """
""" so how do we do the string reversing in the python"""

noteBook = "science and mathematics";
# print(noteBook[::-1]);
# print(noteBook[0:3:-1]); # it does not return any of the index 
# print(noteBook[-1::]); #it returns the value of the -1 which is s 


# print(noteBook[::-1]);
glasses = "wine", "whiskey", "coffee", "brandy";
"""print(len(glasses)); #length is 4
print(glasses[0:4]);
print(glasses[0:3])
print(glasses[0:2]);
print(glasses[0:1]);
print(glasses[-2:-4]); ## hence it shows nothing 
print(glasses[-3: -1]);  '''4-3 = 1 == whiskey and 4-1 = 3 == coffee''';
print(glasses[-4:-3]); ''' 4-4 = 0 == wine and 4-3 = 1 == wine because >> last term " n-1 " tesaile output comes wine only'''
print(glasses[::-1]); ''' output = ('brandy','coffee','whiskey','wine')'''
"""

pictures = "one piece";
reversingPictures = reversed(pictures);     '''reversed function used class = reversed '''
print(reversingPictures, type(reversingPictures));       '''it shows we can reversed the word by join and reversed function'''

reversingSecondTime = "".join(reversingPictures);
print(reversingSecondTime)

print("".join(reversingPictures));  ''' basically bhannuparda kheri it shows null'''

clothes = "pants", "shirts", "bras";
joiningClothes = "".join(clothes);
print(joiningClothes);  ''' it works join function works for the clothes = "pants", "shirts", "bras" output == pantsshirtsbras'''

""" how to replace the strings """

string = "shiva chaudhary";
print(string);
""" string are immutable so we cannot update the string directly """;
print("\n s of shiva chaudhary is replaced by k \n ");
replaceString = string.replace("s", "k");  ''' syntax of replace variable.replace("old word", " new word")'''
print(replaceString); 

citizenship = "district administration office";
replaceCitizen = citizenship.replace("district", "passport");
print("\n", replaceCitizen);

youtube = "nepal 8th wonder of world";
replaceNepal = youtube.replace("Nepal", "australia"); """ in python replace is case sensitive """
replaceYoutube = youtube.replace("nepal", "australia");
print(replaceNepal);
print(replaceYoutube);


""" how to update the strings one at time """
""" hence strings are immutable so they are difficult or harder to update the strings"""
""" lets make the string to a list then update it and join using the join function in the python"""

# names = "shiva chaudhary";
# list1 = list(names);
# list1[0] = "k";
# joiningList = "".join(list1);
# print(joiningList);

# Python Program to Update 
# character of a String 
'''
String1 = "Hello, I'm a Geek"
print("Initial String: ") 
print(String1) '''

# Updating a character of the String 
## As python strings are immutable, they don't support item updation directly 
### there are following two ways 
#1 
"""list1 = list(String1);   ''' we cannot change string to the list so we cannot do that'''
list1[2] = 'p'
String2 = ''.join(list1) 
print("\nUpdating character at 2nd Index: ") 
print(String2) 
"""


characters = "hi i am shiva";
updateCharacters = characters[0:2] + " my" + characters[4:];
updateCharacters = characters[0:2] + " my " + characters[3:];
# print(updateCharacters);

updateSecondTime = characters[0:7] + "jevish" ;
updateSecondTime = characters[0:8] + "jevish" ;
# print(updateSecondTime);

a = 'string';
b = 'string';
print(a+b);
c = a+b;
d = 'p e e k a b o'
print(c);
print(c[6:]);
print(c[-2:12]);
print(c[-10:-6]);
print(c[::-1]);
print(d[::-1]);
d_opp = d[::-1];

for i in d_opp:
    print(i);

for i in c:
    print(i);

list3 = [1, 2, 'one', 'five', [1, 2,'one']];
for loop in list3:
    print(loop);

for loop in list3[4]:
    print(loop, type(loop));

for e in d:
    print(e, end="");

h = d.split();
print("\n", h);

a_tuple = ("shiva", "jevis", "samprad");
# for tuple in a_tuple:
#     print(tuple);

a_dict = dict([(1, 'bat'),(2, 'cat'),(3, 'horse'),(4, 'hippotamus')]);
for dict in a_dict: 
    print(dict, a_dict[dict]);

b_dict = {};

b_dict["clothes1"] = "hoodie";
b_dict["clcthes2"] = "pant";
b_dict["clothes3"] = "shirt";
b_dict["clothes4"] = "sweat shirt";
print(b_dict);

b_dict["clothes5"] = "underwear", "tshirt", "scaff";

for dict1 in b_dict:
    print(dict1, b_dict[dict1]);

string1 = "python is shiva";
list1 = string1.split();
item = list1[0][0];
replace = string1.replace("python", item);
print(replace);

string2 = "my name is shiva chaudhary";
join =' '.join(reversed(string2.split()));
print(join);
# print(reverse, type(reverse));

string3 = "my name is arjun chauhdary";
join = reversed(string3.split());#reverse iterator
join1 = reversed(string3);#reverse
print(join1);
print(join);

reverse = ' '.join(join);
reverse1 = ' '.join(join1);
print(reverse);
print(reverse1);

string4 = "shovit kumar shrestha";
convert = string4.split();
convert[0] = "rajul";
join_str = ' '.join(convert);
print(join_str);

string5 = 'jevis shrestha';
convert_str = string5.split();
convert_str[1] = "maharjan";
join_str1 = ' '.join(convert_str);
print(join_str1);

string6 = 'samprad adhikari';
print(len(string6))
ascess = string6[0:6] + 'n' + string6[7:16]; 
print(ascess);


























