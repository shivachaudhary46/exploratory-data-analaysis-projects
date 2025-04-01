''' match else statement is like an if else statement and much easier than the if else 
in here we can denote the default_by underscope and we dont have to use the break statement in the python like c, c++ '''

# x = int(input("enter the value: "));

# match x:
#     case 0:
#         print("the number is Zero");
#     case _ if x % 2 == 0:
#         print("the number is divisible by 2 and has == 0 ");
#     case _ if x!= 90:
#         print(x, "is not equals to(==) 90");
#     case _ if x!= 80:
#         print(x, "is not equals to(==) 80");
#     case _:
#         print("your number is", x);


# stringFavouriteSports = input("enter your favvourite sports: ");

# """making the amtch else statement for favourite sports"""
# match stringFavouriteSports:
#     case "basketball":
#         print("your favourite sports is basketball");
#     case _ if stringFavouriteSports == "volleyball":
#         print("your favourite sports is volleyball.");
#     case _ if stringFavouriteSports == "football":
#         print("your favourite sports is football");
#     case _ if stringFavouriteSports == "badminton":
#         print("your sports is badminton");
#     case _ :
#         print("your favourite sports is", stringFavouriteSports);
from datetime import datetime
currentTime = datetime.now();
currentTimeInString = currentTime.strftime("%H:%M:%S");
print(currentTimeInString);

"""creating match statement using python"""
favouriteSites = input("could you tell me your faourite sites you have been using: ");

match favouriteSites:
    case "hanime.tv":
        print("your fav sites is", favouriteSites);
    case _ if favouriteSites == "aniwatch.com":
        print("your fav anime is ",favouriteSites);
    case _ if(favouriteSites == "myflixer"):
        print("your fav sites is", favouriteSites);
    case _ :
        print("your fav sites is", favouriteSites);

games = input('enter your favoutite game: ');
match games:
    case 'football':
        print('your favourite game is football');
    case 'volleyball':
        print('your favourite game is volleyball');
    case 'basketball':
        print('your favourite game is basketball');
    case _:
        print('your favourite game is', games);