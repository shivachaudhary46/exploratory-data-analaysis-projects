'''if else statement '''

'''asking input frm the user'''
# inputFromUser =  int(input("give me the number: "));
# print(inputFromUser);


# if(inputFromUser<=10):
#     print("the number is between the 0-10");
# else:
#     print("the number is bigger than 10")


# takingInput = int(input("please enter the number: "));

# if(takingInput<0):
#     print("it is negative number");   
# elif(takingInput>=10 and takingInput<=100):
#     if(takingInput<50 and takingInput>=10):
#         print("the number is between 10-50");
#     elif(takingInput<=100 and takingInput>=50):
#         print("the number is between 50-100");
# elif(takingInput>100 and takingInput<200):
#     if(takingInput<=150):
#         print("the number is between 100 to 150");
#     elif(takingInput>=150 and takingInput<=200):
#         print("the number is between 150-200");
# elif(takingInput>200):
#     if(takingInput>200 and takingInput<=500):
#         print("the number is between 200 to 500");
#     elif(takingInput>500 and takingInput <=1000):
#         print("the number is between 500-1000");
#     else:
#         print("the number is greater than 1000");
# else:
    # print("please enter the number only dont enter A_Z, a-z");

# spritString = "  shiva chaudhary ";
# print("give answer in true or false: ");
# inputFromUser = input("so thier is any sprit(beginning and ending spaces) in the string which i have written over it guess it? and won prize money: ");
# inputToCapital = inputFromUser.capitalize()

# if(inputToCapital):
#     print("you have guessed it right;");
#     print("2000,000,000 has sent to your account");
# else:
#     print("you lose try next time");

# from datetime import datetime

# currentTime = datetime.now();
# print(currentTime);

# currentTimeIn = currentTime.strftime("%H:%M:%S");
# print(currentTimeIn, type(currentTimeIn));

# # currentHours = currentTime.strftime("%h:%m:%s");  
# ''' this does not works hour minute and seconds must be in the capital letters we ca also write day month and year d m y'''

# currentYears = currentTime.strftime("%d/%m/%Y %H:%M:%S");
# print(currentYears);  

# if(currentTimeIn <= "12:60:60"):
#     print("good morning sir!!");
# elif(currentTimeIn <= "18:60:60"):
#     print("good afternoon sir!!");
# elif(currentTimeIn <= "21:60:60"):
#     print("good evening sir!!");
# else:
#     print("good night sir!!");


''' if user gives the input and tell the iser the good morning sir'''

# from datetime import datetime

# currentDate = datetime.now();
# print(currentDate, type(currentDate));  #class is datetime.datetime

# dateConvertToString = currentDate.strftime("%H:%M:%S");
# print(dateConvertToString, type(dateConvertToString));

# #taking the input from the user
# inputFromUser = input("give the current date in \"Hour:minute:seconds\": ");

# if(inputFromUser):
#     if(inputFromUser <= "12:60:60"):
#         print("good morning sir!!!");
#     elif(inputFromUser <= "18:60:60"):
#         print("good afternoon sir!!!");
#     elif(inputFromUser <= "21:60:60"):
#         print("good evening sir!!!");
#     else:
#         print("good night sir!!!");


# import time;
# print(time);
# t = time.strptime("%d/%m/%y %H:%M:%S");❌
# print(t);

from datetime import datetime;
now = datetime.now();
print(now);
hour = int(now.strftime("%H"));
# print(hour);
name = input('enter the name: ');

if(hour >= 0 and hour <= 12 ):
    print("good morning!!", name);
elif(hour > 12 and hour <= 17):
    print("good afternoon!!", name);
elif(hour > 17 and hour <= 24):
    print("good night sir!!", name);
