# stringName = "trikko";
# for character in stringName:
#     print(    character);
#     print(" ", character);  #these line gives more space than the line 5
#     print("\n", character);     
#     print(" \n", character);  #5th line and 6th line are same 

stringClothes = "sweatshirt";
# for looping in stringClothes:
    # print(looping, ",", looping);

    #using the seperator in the looping print
    # print(looping, sep="-");
    # print(looping, end=",");
    # print(looping, end=" ");
    # print(looping.[0], end=" ");  #we cannot iterate the single word in the print
    # print(stringClothes[0:5], looping, end=" ");


'''iterating over the list data type using the for loop'''
# listOfTheClothes = ['hoodie','baggypants','shirts','tshirt'];
# convert = str(listOfTheClothes); '''in another way we can join these items'''
# print(convert, type(convert));  '''string mai xa but it shows the data in the list data type'''
# joinfunctionWithoutSpaces = "".join(listOfTheClothes);    ''''we can do replace list by using ".join() function '''
# joinfunctionWithSpaces = " ".join(listOfTheClothes);
# print(joinfunctionWithSpaces);
# print(joinfunctionWithoutSpaces);

# replacingTheJoinFunction = joinfunctionWithoutSpaces.replace("tshirt", "jacket");
# replacingTheFunctionJoin = joinfunctionWithSpaces.replace("tshirt", "jacket");
# usingSplitFunction = replacingTheFunctionJoin.split();

# for loopingList in listOfTheClothes[0]:
#     print(loopingList);         '''looping on the first item of the list'''

# for loopingSecondList in listOfTheClothes[2]:
#     print(loopingSecondList);

# replaceString = "replace"
# replacingTheList = replaceString.replace("replace", "pants");
# print(replacingTheList);
# for looping in listOfTheClothes:
#     print(looping);
#     if(looping == "tshirt"):
#         print("replaceing the tshirt item");
#         for loopingAnother in usingSplitFunction:
#             print(loopingAnother);

# for makingRange in range(9):
#     print(makingRange); '''so if we write 9 then it will come from to 8 from 0 to 8'''

# for makingRange1 in range(1, 10):
#     print(makingRange1);

# for makingRange2 in range(1, 20000):
#     print(makingRange2);        '''so we cant write the same name in the for loop'''


'''while loop in the python is so much handy '''
# count = 0;

# while (count<10):
#     print(count);
#     count = count + 1;

# print("hooray for ya you have completed the while loop");


# countSecond = 1;

# while (countSecond <= 5):
#     print(countSecond);
#     countSecond = countSecond + 1;
# else:
#     print("we can do this also in the while loop");

# countThird = int(input("enter the number: "));

# while(countThird <= 89):
#     print(countThird);
#     countThird = countThird + 1;
# else:
#     print("enter the number less than 89 to get most of the iteration in while loop");

"""python while reversed loop from higher number to lower number"""

# reverseCount = int(input("enter the number: "));

# while (reverseCount>0):
#     print(reverseCount);
#     reverseCount = reverseCount - 1;
# else:
#     print("so we have exited the loop");


# count = 10;

# while (count >0):
#     print(count);
#     count = count - 1;
# else:
#     print("we have exited the loop");

'''for loop use in the dicitionary'''
# print("\ndicitionary iteration: \n");

# """creating dicitionary item"""
# dForDict = {};
# dForDict['name'] = "shiva";
# dForDict['caste'] = "chaudhary";
# dForDict['job'] = 'student';
# dForDict[1] = 'yuukiaasuna100@gmail.com'
# dForDict[2] = 4

# print(dForDict);

# '''how to iterate the dict by using for loop?? '''
# for looping in dForDict:
#     print(looping, type(looping));  #actually looping ko key ko type print hunxa
#     print(dForDict[looping], type(dForDict[looping]));  #key ko value ko type print hunxa

# '''how to check the value of the dicitionary in the console'''
# print(dForDict['caste']);
# print(dForDict['name']);
# print(dForDict['job']);

'''making new dicitionary items like'''

# dictionary = dict([('mobile1','iphone'), ('mobile2', 'samsung'), ('mobile3', 'redmi'), ('mobile4', 'one plus')]);

# '''making loops in the dicitionary'''
# for i in dictionary:
#     print(i, dictionary[i]);
#     print("% s % s" % (i, dictionary[i])); '''so we can do this method also in for loop printing the statement'''


'''let me write syntax for it  print(" %S=string %d=int %f=float" % (loopname, dict[loopname]))'''

"""break and continue loop in the python"""
# for i in range(1, 10, 2): 
#     print(i);   '''third argument in for loop means that it will skip for that numbers which is given'''

# print("looping the range: ")
# for even in range(1, 24, 4):
#     print(even);
#     if(even % 2 == 0):
#         break;
#     if(even % 3 == 0):
#         break;

''' make the multiplication table from 10 to 20'''
# for one in range(1, 15):
    # if(one == 10):
    #     print("we only need multiplication table upto the one"); ''''break statement is used so it will ignore this line '''
    #     break;

'''trying the continue statement'''
    # if(one == 10):
    #     print("using continue statement");  '''if hamle continue ko paxaadi this line exectur garyo bhane pahila continue hunxa and it  will try to ignore this line so continue ko mathi hunuparxa'''
    #     continue;  '''continue statement only skips the condition match iteration'''

    # print("1 x", one, "=", 1 * one);    '''multiplication of the one '''
    
# for two in range(0, 15):
#     if(two == 10):
#         break; '''so we want to print only upto 10'''  '''so this break = means get out from this loop'''
#     print("2 x" , two + 1, "=", 2*(two + 1));
''' 0   1
    1   2
    2   3
    3   4
    4   5   
    5   6
    6   7
    7   8
    8   9
    9   10  10 will be appear in the screen
    10 == 10 so it will break from here'''

# for three in range(0, 15):
#     if(three == 10):
#         print("we are breaking on the 10");
#         break;      '''if we put if else in the down 
#                         0 - 1
#                         1 - 2
#                         2 - 3
#                         3 - 4
#                         4 - 5
#                         5 - 6
#                         6 - 7
#                         7 - 8
#                         8 - 9
#                         9 - 10
#                         10 - 11  line 183 ma 10 print hunxa and balla if else ma break hunxa ni ta but if we put if else in the up '''
#     print("3 x", three + 1, "=", 3*(three + 1));

# for twelve in range(0, 15):
#     if(twelve == 10):
#         print("we are continuing or skiping the 10th iteration it means we have done + 1 so it is skipping on the 11nth");
#         continue;
#     print("12 x", twelve + 1, "=", 12 * (twelve+1));

# for thirteenth in range(1, 13):
#     if(thirteenth == 10):
#         print("breaking");
#         break;
#     print("13 x", thirteenth, "=", 13*thirteenth);

# for fourteen in range(1, 20):
#     print("14 x", fourteen, "=", 14*fourteen);
#     '''in here 10 will be print then after break'''
#     if(fourteen == 10):
#         print("breaking");
#         break;

'''how to do the do while loop'''
# inputInt = int(input("enter the number: "));
# while True:
#     print(inputInt);
#     inputInt = inputInt + 1;
#     if (inputInt >= 20):
#         break;

''' do{s
        body statment   
    }while()
'''

# from datetime import datetime

# stringTime = datetime.now();
# #converting into string 
# convertTime = stringTime.strftime("%H:%M:%S");

# converting the datetime.datetime to string 
# print(convertTime);

# for number in range(0, 100):
#     stringTime = datetime.now();
#     #converting into string 
#     convertTime = stringTime.strftime("%H:%M:%S");

#     # converting the datetime.datetime to string 
#     print(convertTime);  """seriously it runs 200000 2 lakhs times ""



#making the guess game 
guessWord = "games";
counter = 0

while True:
    """so you have to put counter and break logic at first then you have to ask the user your input if she/he has guessed correctly you won but if you have guessed the question incorrectly you loose"""
    counter = counter + 1;
    if(counter>3):
        print("breaking");
        break;
    askingInput = input("""you have the 3 chances of the guess. Guess the word:  """);
    convertInput = askingInput.lower();
    # print(guessWord);
    # print(convertInput);
    if(convertInput == guessWord):
        print("you have won the guessing game!!!");
        break;
    else:
        print("sorry better luck next time!!!");

