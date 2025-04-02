#koun banega cororepati

import random;
#making the list of the questions
# ques = dict([(0, 'what is the deepest lake in the world ?? '), (1, 'what is the full form of the cgi ??'), (2, 'what is the deepest gorge in the world ??'),(3,'what is the highest waterfalls in the world ??')]);
ques = ['','what is the deepest lake in the world ?? ', 'what is the full form of the cgi ??', 'what is the deepest gorge in the world ??', 'what is the highest waterfalls in the world ??'];
ans1 = ['','lake baikal', 'issyk kul', 'great slave lake', 'rara lake'];
ans2 = ['','computer generated imagery','computer generated intilligences','computer graphics images', 'computer grated imagery' ];
ans3 = ['','the kali gandaki george', 'george of cyprus','George of Laodicea', 'Georgius Florentius,'];
ans4 = ['','angel falls', 'david falls', 'nigeria falls', 'Kunchikal Waterfalls'];
answer = ['',ans1, ans2, ans3, ans4];

print("welcome to koun banega cororepati!!(kbc)".center(50, '-'));
name = input("enter your name to play: ");

def gender():
    asking = input('are you male or female: ');
    if asking == 'male':
        return "Mr";
    else:
        return 'Mrs';

sex = gender();

def country():
    asking = input('which country are you from: ');
    if asking == 'nepal':
        return 'Rs ';
    elif asking == 'india':
        return '₹ ';
    elif asking == 'china':
        return '¥ ';
    elif asking == 'japan':
        return '¥ ';
    elif asking == 'germany':
        return '€ ';
    elif asking == 'france':
        return '€ ';
    elif asking == 'austria':
        return '€ ';
    else:
        return '$ ';

currency = country();
print('you can play upto 15 question in this kbc game:')

print(f"""prizes for each ✅ answer:
      1. ✅- {currency}15000
      2. ✅- {currency}30000
      3. ✅- {currency}60000
      4. ✅- {currency}120000
      5. ✅- {currency}240000
      6. ✅- {currency}480000
      7. ✅- {currency}960000
      8. ✅- {currency}1920000
      9. ✅- {currency}3840000
      10. ✅- {currency}7680000
      11. ✅- {currency}15360000
      12. ✅- {currency}30720000
      13. ✅- {currency}61440000
      14. ✅- {currency}122880000
      15. ✅- {currency}245760000""");

def kbc(n):
    for i in (0, 16):
        if n == i:
    
            number = 0;
            count = 16;
            while count >= number:
                result = kbc(number);
                number += 1;

def money_prize():
    money = 7500;
    return money;

won = money_prize();

# if result:
#     won *= 2;
#     prize = 'correct answer!! you have won {}{} prize money {}.{}';
#     print(prize.format(currency, won, sex, name));
# else:
#     prize = 'wrong answer!! you have won {}{} prize money {}.{}';
#     print(prize.format(currency, won, sex, name));