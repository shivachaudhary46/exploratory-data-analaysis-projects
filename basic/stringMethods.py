upper ="abcDefGHI"

""" string convert to lower """
print(upper.lower()); 
print(upper.upper());

lower = " this is the FIRST tiMe Writing COdeeeeeeeeeeee ";
''' lower function converts them into all lower '''
print(lower.lower());

''' upper function converts them into all letter upper'''
print(lower.upper());

''' split function works on the spaces and makes list of them '''
print(lower.split()); 

splitString = "kite", "site", "bright", "might";  ''' tuple object has no split '''
# print(splitString.split());

''' rsplit removes the characters on the string and makes list'''
print(lower.rsplit("e"));

''' rstrip function removes the character on trailing means end of the string'''
print(lower)
print(lower.rstrip("e"));

''' capitalize function capital the first letter of the sentences or word note: it will not capital like title '''
capital = "hello world";
print(capital.capitalize());

'''strip removes the beginning and ending white spaces  '''
stripString = "                  shiva chaudhary          ";
print(stripString);
print(stripString.strip());  #❤️❤️begining and ending spaces removed

''' title function makes the each word first letter capital '''
titleString = "introduction to the new world";
print(titleString.title());
print(lower.title());
print(capital.title());
print(stripString.title());

''' so we cannot make the title in the list'''
#print(splitString.title()); 

''' replace function is used to replace old word with the new word'''
replaceString = "this letter is going to be replace"
print(replaceString.replace("replace", "manufactured"));
print(titleString.replace("world", "city"));
print(stripString.replace("          ", "my name is"));
print(stripString.replace(" ", "my name"));

'''count function is used to count the letter in the word and returns the number of the word'''
countString = "aabracadabra"; """6 count ❤️❤️✅"""
print(countString.count("a"));
print(replaceString.count("a"));
print(replaceString.count("the")); ''' so if there is not any then it will returns the 0'''
print(replaceString.count("this"));

''' endswith function which match the words on the ends of the sentences and returns the true or false'''
endswithString = "checking the word";
print(endswithString.endswith("word"));
print(endswithString.endswith("checking"));
print(countString.endswith("a"));
print(countString.endswith("abracadabra"));

print("startswith function returns the bool value: ")
'''startswith() function checks whether the sentence first word or letter is in the sentence and return bool value'''
print(endswithString.startswith("checking"));
print(endswithString.startswith("the"));
print(replaceString.startswith("this"));

'''find() function check the letter is present in sentence or in string and returns index where it is and if not found the returns -1 and always returns the first index of the word '''
findString =  "mikey mike has mike and spike the mike with his mike";
print(findString.find("m"));
print(findString.find("mike"));
print(findString.find("has"));
print(findString.find("s"));
print(findString.find("z"));

''' index() function is same as find() but when it does find the letter it returns error'''
indexString = "pikey peak has spike the wheel with its finger";
print(indexString.index("peak"));
print(indexString.index("s"));
print(indexString.index("wheel"));
#print(indexString.index("z"));  ''' it gives us the error because it z is not in the string'''

''' center() function makes the sentences to the center'''
centerString = "Introduction of the python!!!";
print(centerString.center(50));
print(centerString.center(75));
print(centerString.center(100));
print(centerString.center(1));
print(centerString.center(50, "-"));

'''isalnum() is the function which checks the A-Z,a-z,0-9 return bool value note: it also counts spaces'''
isAlphaNum = "printing is quite hedonistic 23 A";
print(isAlphaNum.isalnum());
print(centerString.isalnum());
print(indexString.isalnum());  

isAlphaSecond = "WElComeTotheworld";
print(isAlphaSecond.isalnum());

isAlphaThird = "commonbabyletsdance!";
print(isAlphaThird.isalnum());

print("isalpha".center(25, "-"));
'''isalpha is same as the isalnum() but it checks only A_Z, a-z'''
print("mynameisshivachaudhari".isalpha());
print("my office works start at 6".isalpha());
print("myofficeworksisatsixoclock".isalpha());
print("my office works is at six o clock".isalpha());

print("islower".center(25, "-"));
'''islower() is function which checks the whole letter is lowercase or not'''
print("shiva chaudhari".islower());
print("AssnCklCCLKSds".islower());
print("my name is shiva chaudhary".islower());

print("istitle".center(25, "-"));
'''istitle() function checks the each letter is capital or not returns bool value'''
print("My Mom Is Awesome".istitle());
print("My MoM Is AwesoMe".istitle());
print("shiva chaudhary".istitle());
print("INTRODUCTION".istitle());

print("isupper".center(25, "-"));
'''isupper() is function which checks the each letter is uppercase or not '''
print("MY NAME IS".isupper());  '''true'''
print("k xa tmro HAAL khabar".isupper());  '''false'''
print("My Name".isupper()); '''false'''
print("Introduction To The World".isupper());  '''false'''

'''isprintable is the function which checks the letter which is printable or not'''
print("isprintable".center(25, "-"));
print("what are you doing next week ??\n".isprintable());  '''false'''
print("can you > < do my homework".isprintable());  '''true'''
print("what \"are you\" doing next week??".isprintable()); '''true'''
print("can some one fish in this @rea??".isprintable());  '''true'''
 
'''swapcase() is function which swaps the case when lower to upper and viceversa'''
print("swapcase".center(25, "-"));
print("THIS is The first Time".swapcase());
print("let's go to the coffee date?? ".swapcase());
print("HELLO SEXY LADY LET'S GO TO THE DATE".swapcase());
print("kdjaBSSJS".swapcase()); '''note: it will swap the whole each single letter lower to upper and viceversa'''

print("isspace".center(25, "-"));
'''isspace() function checks whether the whole sentence has spaces or not and returns the bool value'''
print("is the world is dying?? ".isspace()); '''false'''
print("helpmeout".isspace());  '''false'''
print("couldyou-give_me-coffe".isspace()); '''false'''
print("           ".isspace()); '''true'''
print("                           ".isspace()); '''true'''

#upper()
string = "higHerCApitAL";
print(string.upper());

#lower()
str_low = 'lOWEr CapItAl';
print(str_low.lower());

#strip()
str_strip = "   removes the spaces of start and ending   ";
print(str_strip.strip());

#rstrip()
str_strip1 = "removes the ending word";
print(str_strip1.rstrip("d"));

#split()
split_str = "changing into the list"
print(split_str.split());

#count()
counting = "count the word in the sentences";
print(counting.count('o'));

#replace()
replace_str = "replacing the string";
print(replace_str.replace("the", "with"));

#center()
center_str = "making to the center";
print(center_str.center(25, '.'));

#title()
string1 = 'it capitalie the every word like title';
print(string1.title());

#capitalize()
string2 = 'capitalize the front word letter';
print(string2.capitalize());

#startswith()
start_word = 'return bool value and check for first word';
print(start_word.startswith('return'));

#endswith()
end_word = 'return bool value and check for last word';
print(end_word.endswith('word'));

#find()
find = 'find the word and return index number';
print(find.find('t'));

#index()
index_str = 'find the word and return index number kei xaina bhane error show garxa';
print(index_str.index('g'));

#isalnum()
is_alnum = 'check the word is a-z, A-Z, 0-9 return bool';
print(is_alnum.isalnum());

#isalpha()
is_alpha = 'check the word is is aphabet or not';
print(is_alpha.isalpha());

#isspace()
is_space = "             ";
print(is_space.isspace());

#isupper
is_upper = "HIGHER";
print(is_upper.isupper());

#iupper
is_lower = "Lower";
print(is_lower.islower());

#isprintable()
is_printable = "check the sentences is printable or not\n";
print(is_printable.isprintable());

#swapcase 
swap_case = 'CONVERT respectable case to another and viceversa';
print(swap_case.swapcase())