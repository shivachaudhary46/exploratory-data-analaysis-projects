dictionaries = {'name':'shiva', 'class':12, 'roll no':456};
print(dictionaries);

print(dictionaries['name']);
print(dictionaries.get('class'));
print(dictionaries.get('clothes'));#none❌

print(dictionaries['roll no']);

for i in dictionaries:
    print('\n',dictionaries[i]);
    print(dictionaries.items());
    print(dictionaries.keys());
    print(dictionaries.values());

print('\n', dictionaries.keys());
print(dictionaries.values());

dict1 = dict([('name', 'jevis'), ('class', 'bsc csit'), ('roll no', 234)]);
print(dict1);
print(dict1.keys());
print(dict1.values());
print(dict1.items());

for key, values in dict1.items():
    print(f'the {key} and {values} of dictionaries (key, values) pair of jevis');

for pikey, peak in dictionaries.items():
    print(f'the dictionaries key = {pikey} and values = {peak} is written.\n\n\n\n\n')

# def fibonacci(n):
#     if n == 0:
#         ans1 = ['lake baikal', 'issyk kul', 'great slave lake', 'rara lake'];
#         print("what is deepest lake in world: ");
#         for i in range(0, 4):
#             print(i, ans1[i]);
#         ques = input("enter the correct answer: ");
#         if ques == ans1[0]:
#             return True;
#         else:
#             return False

#     elif n == 1:
#         print("what is fullform of the cgi: ");
#         ans2 = ['computer generated imagery','computer generated intilligences','computer graphics images', 'computer grated imagery' ];
#         for i in range(0, 4):
#             print(i, ans2[i]);
#         ques = input("enter the correct answer: ");
#         if ques == ans2[0]:
#             return True;
#         else:
#             return False;

#     else:
#         return 'you won the game';

# number = int(input('how many questions you want to be asked: '));
# for i in range(0, number):
#     result = fibonacci(i);
#     if(result == True):
#         print('correct answer');
#     else:
#         print('wrong answer');
#         break;✅✅✅✅✅✅


def fibonacci(n):
    for i in range(0, 12):
        if n == i :
            #question
            ques = ['what is the deepest lake in the world ?? ', 'what is the full form of the cgi ??', 'what is the deepest gorge in the world ??', 'what is the highest waterfalls in the world ??', 'who was the first King of the united Nepal ?? ', 'who was the first president of Nepal ?? ', 'Who founded Pashupati temple in the Kathmandu ?? ', 'Who Led The Peasant Uprising In Nepal In 1951 That Ended The Rana Regime ?? ', 'Who Built The Swayambhunath Stupa In Kathmandu ?? ', 'Who Established The Modern Education System In Nepal ?? ', 'Who Was The First Person To Climb Mount Everest ?? ', 'What Was The Religion Of The Malla Kings Who Ruled The Kathmandu Valley From The 12th To The 18th Century ?? '];
            #answer
            ans = [['','rara lake', 'issyk kul', 'great slave lake', 'lake baikal', 'd'], ['','computer graphics images','computer generated intilligences','computer generated imagery', 'computer grated imagery', 'c'], ['','george of cyprus', 'the kali gandaki george','George of Laodicea', 'Georgius Florentius', 'b'], ['','nigeria falls', 'david falls', 'angel falls', 'Kunchikal Waterfalls', 'c'], ['','birendra bir bikram shah', 'jung bahadur rana', 'mahendra bir bikram shah', 'prithivi narayan shah', 'd'], ['', 'surya bahadur thapa', 'bidhya devi bhandari', 'Dr. Prakash Chandra Lohani', 'ram baran yadav', 'd'], ['', 'jayasithi malla', 'yaksha malla', ' Siddhi Narsingh Malla', 'pratap malla', 'a'], ['', 'bir shumsher', 'Jang Bahadur Rana', 'sukraraj sasthri', 'mohan shumsher', 'c'], ['','mahendra bir bikram shah','Jaya Prakash Malla', 'pratap malla', 'siddhi narsingh malla', 'b'], ['','dev shumsher rana', 'bhimsen thapa', 'chandra shumsher rana', 'jung bahadur rana', 'd'], ['', 'Tenzing Norgay',' Edmund Hillary','Reinhold Messner','Junko Tabei', 'b'], ['', 'hinduism', 'buddhism', 'jainism', 'islamism', 'a']];

            print(f'{i+1}. {ques[i]}');
            print(f'a. {ans[i][1]}              b. {ans[i][2]}');
            print(f'c. {ans[i][3]}              d. {ans[i][4]}');
            ques = input("\nenter the correct answer:(a-d):  ");
            low = ans[i][5]
            answer = low.lower();
            if ques == answer:
                return True;
            elif ques == 'end':
                return 0;
            else:
                return False;


print("welcome to koun banega cororepati!!(kbc)".center(50, '-'));
print('enter \'end\' to end the game: ');
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

print('you can play upto 12 question in this kbc game:')
print(f"""prizes for each ✅ answer:
      1. ✅- {currency}15,000
      2. ✅- {currency}30,000
      3. ✅- {currency}60,000
      4. ✅- {currency}1,20,000
      5. ✅- {currency}2,40,000
      6. ✅- {currency}4,80,000
      7. ✅- {currency}9,60,000
      8. ✅- {currency}19,20,000
      9. ✅- {currency}38,40,000
      10. ✅- {currency}76,80,000
      11. ✅- {currency}1,53,60,000
      12. ✅- {currency}3,07,20,000: """);


number = 12
money = 7500;
for i in range(0, number):
    result = fibonacci(i);
    if(result == True):
        money *= 2;
        print(f'correct answer!! you have won {currency}{money} {sex}. {name}\n');
    elif(result == 0):
        print(f'game over!!! you have won {currency}{money} {sex}. {name}\n');
        break;
    else:
        print(f'wrong answer!! you have won {currency}{money} {sex}. {name}\n');
        break;

