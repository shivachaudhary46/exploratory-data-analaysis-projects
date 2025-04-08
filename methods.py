import re;

pattern = r'[A-Z]+yclones';

text = '''Weather fronts mark the boundary between two masses of air of different temperature, humidity, and densities, and are associated with the most prominent meteorological phenomena. Strong cold fronts typically feature narrow bands of thunderstorms and severe weather, and may on occasion be preceded by squall lines or dry lines. Such fronts form west of the circulation center and generally move from west to east; warm fronts form east of the cyclone center and are usually preceded by stratiform precipitation and fog. Warm fronts move poleward ahead of the cyclone path. Occluded fronts form late in the cyclone life cycle near the center of the cyclone and often wrap around the storm center.

Tropical Byclones describes the process of development of tropical Dyclones. Tropical cyclones form due to latent heat driven by significant thunderstorm activity, and are warm core.[10][11] Cyclones can transition between extratropical, subtropical, and tropical phases.[12] Mesocyclones form as warm core cyclones over land, and can lead to tornado formation.[13] Waterspouts can also form from mesocyclones, but more often develop from environments of high instability and low vertical wind shear.[14] In the Atlantic and the northeastern Pacific oceans, a tropical cyclone is generally referred to as a hurricane (from the name of the ancient Pyclones American deity of wind, Huracan), in the Indian and south Pacific oceans it is called a cyclone, and in the northwestern Pacific it is called a typhoon.[15] The growth of instability in the vortices is not universal. For example, the size, intensity, moist-convection, surface evaporation, the value of potential temperature at each potential height can affect the nonlinear evolution of a vortex'''

#re.search() returns the first MatchObject of start and end index 
match = re.search(pattern, text);
# print(match.span());

#finds all occurence and returns in the list
match = re.findall(pattern, text);
# print(match);

#find all occurence in the iter object
matches = re.finditer(pattern, text);
# for match in matches:
#     print(text[match.span()[0]:match.span()[1]]);
    # print(match.span()[0], match.span()[1]);
    # print(text[match.span()[0]]);

#
find = r'[a-z]+at';
search = 'the cat has the biggest hat in the town';

#sub means replace in the regression expression 
#syntax = re.sub(pattern, 'replace word', 'string where need to be replaced')
# match = re.sub(find, 'dog', search);
# print(match);   

find = r'\\';
search = 'the cat has longest \\ tail in the history';

regex = re.findall(find, search);
print(regex);

find = r'\n';
search = '\n this syntax match the new lines';
regex = re.findall(find, search);
print(regex);

pattern = r'\w+\d+\@\w+\.\w+';
expression = 'yuukiaasuna100@gmail.com';
match = re.search(pattern, expression);
if match:
    email = match.group();
    print(email);

#\w+\d+\s+ more than 1 words, digits, space 
pattern = r'\w+\d+\@\w+\.\w+';
expression = 'yuukiaasuna100@gmail.com';
match = re.search(pattern, expression);
if match:
    email = match.group();
    print(email);

# * multiple times
pattern = r'zo*';
expression = 'zoo, zo, z, abc, hello gonna kill you zoooo';
regex = re.findall(pattern, expression);
print(regex);

#
pattern = r'z+';
expression = 'zoo, zo, z, abc, hello gonna kill you zoooo, zinx zzzzzz';
regex = re.findall(pattern, expression);
print(regex);

#? do or dont
pattern = r'a?ve?';
expression = 'have, has, never, save, lame,';
regex = re.findall(pattern, expression);
print(regex);

#matches every single character except new lines
pattern = r'.';
expression = 'have, has';
regex = re.findall(pattern, expression);
print(regex);

#escaped sequence chars
pattern = r'\(\)';
expression = '(/has the /), ()';
regex = re.findall(pattern, expression);
print(regex);

pattern = r'z|wood';
expression = 'zood, zoo, zo, wood, wo, zinx';
regex = re.findall(pattern, expression);
print(regex);

pattern = r'(z|w)ood?';
expression = 'zood, zoo, zo, wood, wo, zinx';
regex = re.findall(pattern, expression);
print(regex);

pattern = r'\w+o{2}\w+';
expression = 'food, hood';
regex = re.findall(pattern, expression);
print(regex);

pattern = r'o{2,}';
expression = 'zood, zoo, zo, wooooooooooooooooooooooood, wo, zinx';
regex = re.findall(pattern, expression);
print(regex);

#o+ 
pattern = r'o{1,}';
expression = 'zood, zoo, zo, wooooooooooooooood, wo, zinx';
regex = re.findall(pattern, expression);
print(regex);

#matches the o but print all the chars which do not match as ''
pattern = r'o{0,}';
expression = 'zood, zoo, zo, woo, woooo';
regex = re.findall(pattern, expression);
print(regex);

pattern = r'[abc]';
expression = 'plain';
regex = re.findall(pattern, expression);
print(regex);

pattern = r'[^abc]';
expression = 'plain';
regex = re.findall(pattern, expression);
print(regex);

#match except m-z
pattern = r'[^m-z]';
expression = 'make, mopq, mop, mors code, abc trek ';
regex = re.findall(pattern, expression);
print(regex);

pattern = r'\A';
expression = 'podcasts, ANJE, anje';
regex = re.findall(pattern, expression);
print(regex);

#matches the boundary
pattern = r'er\b';
expression = 'neverever has er';
regex = re.findall(pattern, expression);
print(regex);

#matches non word boundary
pattern = r'ea*r\B';
expression = 'I have never woke earlyat night';
regex = re.findall(pattern, expression);
print(regex); 

pattern = r'ea*r*';
expression = 'i have one e, ear , eaaaa, earrrr';
regex = re.findall(pattern, expression);
print(regex);

pattern = r'\D';
expression = 'I have ';
regex = re.findall(pattern, expression);
print(regex); 

pattern = r'\ding';
expression = '345, ing, 345ing';
regex = re.findall(pattern, expression);
print(regex); 

#Matches any non-white space character.
pattern = r'\S';
expression = 'white     , space';
regex = re.findall(pattern, expression);
print(regex); 

pattern = r'\s';
expression = 'white space';
regex = re.findall(pattern, expression);
print(regex); 

#pattern we cannot use regex in the lists  
# pattern = r'nepal';
# expression = ['nepal', 'india', 'china'];
# match = re.search(pattern, expression);
# print(match.group());