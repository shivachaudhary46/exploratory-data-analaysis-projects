""" there are 7 operators in the python 
1. + eg: 2+3 = 5    addition
2. - eg: 4-5 = -1   subtraction
3. * eg: 8*9 = 73   multiplication
4. / eg: 7/7 = 1    divison
5. // eg: 3/2  = 1  actually 1.5 hunu parne but it is " floor divison "
6. ** eg: 3**2 = 9  power = 3*3
7. % eg: 5%2 = 3    module or remainder """

# print("this is the operators app")

a = 200
b = 100
# print("the value of", a, "+", b, "is: ", a+b);
# print("the value of", a, "-", b, "is: ", a-b);
# print("the value of", a, "*", b, "is: ", a*b);
# print("the value of", a, "/", b, "is: ", a/b);
# print("the value of", a, "**", b, "is: ", a**b);
# print("the value of", a, "//", b, "is: ", a//b);
# print("the value of", a, "%", b, "is: ", a%b);


""" type casting in python """
'''' so we can convert the one data into another data from the function like int(), float(), str(), ord(), oct(), hex(), tuple(), set(), list(), dict()'''

"""" there are two types of typecasting in the python hai ta 
1. explict type casting in the python
2. implicit type casting in the python


above example in the explicit type casting in the python where we use function like int(), float(), str(), set(), ord(), hex(), list(), tuple(), dict()"""


intToString = "12";
# print(intToString, type(intToString));

int = 12;
convertIntString = str(int);
# print(convertIntString, type(convertIntString));

a = "apple"
b = "mango"
# print(int(a) + int(b)); # we cannot convert string into int because they are different data types in python 

c = 2.3
# print(c, type(c));
# float = int(c);
# print(float, type(float)); #we cannot convert the float into int object 

##### implicit type casting 
""" implicit casting means the type csting which by the python itself for the better understanding the implicit type casting is done on the basis of int, float, and complex """

d = 3;
e = 4.5;
# print(d, type(d));
# print(e, type(e));
# print(d + e, type(d + e));

f = float(d);
# print(f, type(f));  '''' we cannnot change the float to int but int can be change to float like 3 is changed to 3.0'''

g = "5.9"
h = "6.9"
i = float(g)
j = float(h);
# print(i + j);


listOfFruit = "mango", "banana", "apple";
convert = list(listOfFruit);
# print(convert);

ListOfBOOks = 1, "its okay to not be okay", "summer love", "firfirey", 3
convertToList = list(ListOfBOOks);
# print(convertToList);

tupleOfGames = "mobile legend", "pubg", "gta vict", "ps5"
convertToTuple = tuple(tupleOfGames);
# print(convertToTuple);

tupleOfCups = "wine glass", "whiskey glass", "vodka glass", "coffee glass", "tea glass";
convertToCups = tuple(tupleOfCups);
# print(convertToCups);



# Creating an empty Dictionary 
# Dict = {} 
# print("Empty Dictionary: ") 
# print(Dict) 
  
# Creating a Dictionary 
# with dict() method 
# Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'}) 
# print("\nDictionary with the use of dict(): ") 
# print(Dict) 
  
# Creating a Dictionary 
# with each item as a Pair 
# Dict = dict([(1, 'Geeks'), (2, 'For')]) 
# print("\nDictionary with each item as a pair: ") 
# print(Dict) 

#empty dicitionary
emptyDicit = {};
# print(emptyDicit);

#dicitionary using dict
usingDict = dict({1: "shiva", 2: "chaudhary", 3: "18"});
# print(usingDict); 

# using with each item as pair
usingDictPair = dict([(1, "shiva"), (2, "chaudhary")]);
# print(usingDictPair);

#using with dict as dicitionary
dictFunction = dict({ 
    "iphone": "14 pro max",
    "launch on": 2023,
    "users": 20202020202
})
print("\nusing the dict function to print the mapped diagram key pair:\n ");
# print(dictFunction);

#using dict as #key pair
dictAsKeyPair = dict([('name','shiva'), ('email','yuukiaasuna100@gmail.com'), ('num', 9766869576)]);
# print(dictAsKeyPair);

#nested dicit using dict function
nestedDictFunction = dict({
        'name':'shiva',
        'religion':'hindu',
        'class': 12,
        'friends':{
            'name': 'jevis',
            'class': 12,
            'religion': 'hindu',
            'friends': {
                'name':'samprad',
                'class': 12,
                'religion': 'buddhisim',
                'friends':{
                    'name':'anjelika',
                    'class': 12,
                    'religion':'christanity'
                }
    }
}})
# print(nestedDictFunction);
 

 # Creating an empty Dictionary 
# Dict = {}
# print("Empty Dictionary: ") 
# print(Dict) 

# Adding elements one at a time 
# Dict[0] = 'Geeks'
# Dict[2] = 'For'
# Dict[3] = 1
# print("\nDictionary after adding 3 elements: ") 
# print(Dict) 

# Adding set of values 
# to a single Key 
# Dict['Value_set'] = 2, 3, 4
# print("\nDictionary after adding 3 elements: ") 
# print(Dict) 

# # Updating existing Key's Value 
# Dict[2] = 'Welcome'
# print("\nUpdated key value: ") 
# print(Dict) 

# # Adding Nested Key value to Dictionary 
# Dict[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}}
# print("\nAdding a Nested Key: ") 
# print(Dict) 



#creating the empty dicitionary as god
god = {};
# print(god);

#adding element by one at a time 
god[0] = "buddha"
god[1] = "saraswoti";
god[2] = "laughing buddha"
god[3] = "shiva";
god[4] = "Bishnu"
# print(god);

#adding different element at a time 
god["kami-sama"] = "japanese", 2, 3, "ryuu"
# print(god);

#adding more one element at a time 
god[12] = "krishna"
god[11] = "ganesh";
# print(god);

#updating the element of key 
god[1] = "kali bhagwati"
# print(god);

#adding nested structure on the god dicitionary
god['nested structure'] = { 0:"buddha", 1: "saraswoti", 2: "laughing buddha", 3:"shiva"}
# print(god);

dicitionary = dict({ "name": "anjelika", "age": 34, "likes":"pizza"});
# print(dicitionary);

dictOfCellphones = dict([(0,"samsung"), (1, "iphone"), (2, "huwai"), (3, "redmi 25"),( 4, "one plus")]);
# print(dictOfCellphones);



""" adding dicitionary one at a time"""
cellPhone = {}
cellPhone["samsung"] = 2022;
cellPhone["iphone"] = 2022;
cellPhone["redmi"] = 2021;
cellPhone["one plus"] = 2020;

#checking the list 
print(cellPhone);


# adding one set of the list in the dictioary
cellPhone["brand"] = "iphone", "samsung", "huwai", "one plus";
cellPhone["establish"] = 2022, 2023, 2034, 2034;
print(cellPhone);

#updating the cellphone dictionary
cellPhone["one plus"] = 2021;

#nested adding on the dictionary
cellPhone["iphone"] = {
    "name":"iphone",
    "class":"ring tone",
    "user": 202020
}
print(cellPhone);

#7 Operators 
#   +
#   -
#   *
#   /
#   **  
#   //
#   %

a = 2;
b = 4;

print(b+a);
print(b-a);
print(b*a);
print(b/a, type(b/a));
print(b**a);
print(23//4);
print(45%a);

print("number form code, ");
print(12+12);
print(12-12);
print(12*12);
print(12/12);
print(12**2);
print(25//4);
print(25%4);

integer = 23;
print(integer, type(integer));
string = str(integer);
print(string, type(string));
print(str(integer), type(str(integer)));
# print(int(string), type(int(string)));#❌

string = "this";
print(string, type(string));

float1 = 2.4
# print(int(float1), type(int(float1)));#❌

integer1 = float(integer);
print(integer1, type(integer1));

float2 = 2.4;
print(str(float2), type(str(float2)));

string = "2.4";
print(float(string), type(float(string)));

list1 = 1, "name", "shiva", "chaudhary", ["jevis", "shrestha"];
print(list(list1));

lst2 = 1, 1, "jevis", "samprad", (1, 2, 3);
print(list(lst2));

dict1 = dict({'name':'shiva', 'num':'1', 'roll no':'23'});
print(dict1);

dict2 = dict([(1,'jevis'),(2, 'samprad'),(3,'shiva'),(4,'anje')]);
print(dict2);

dict3 = dict([('god1','saraswoti'),('god2', 'buddha'),('god3','shiva'),('god4','ganesh')]);
print(dict3, type(dict3));

dict = {};
dict[1] = 'physics';
dict[2] = 'maths';
dict[3] = 'cheme';
dict[4] = 'english';
dict[5] = 'nepali';
print(dict);

dict[5] = 'art';
print(dict);

dict['books'] = 'rich dad', 'robert kiyosaki';
print(dict);

dict['neseted'] = {1:'phys', 2:'cheme', 3:'math'}
print(dict);



















