# numbers = [67, 1, 5, 10, 4, 5]

# print("before apending numbers -> ", numbers);
# numbers.append(56)
# print("after apending numbers -> ", numbers);

# num2 = [67, 1, 5, 10, 4, 8]
# numbers.extend(num2);
# print(numbers);

# numbers.insert(0, 100)
# print(number y) for x in [1, 2, 3] for y in [3, 1, 4] if x!=y]
# print(list1)

# matrix = [
#     [1, 2, 3, 4], 
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]

# [[row[i] for row in matrix ] for i in range(4)]s)

# #it shoows the error in the remove functionn 
# # if removing function does not found 
# num2.remove(4)
# print(num2)

# num2.pop(4)
# print(num2)

# num2.clear()
# print(num2)

# numbers.sort()
# print(numbers)

# numbers.reverse()
# print(numbers)

# basket = {'apple', 'orange', 'pear', 'banana', 'apple'}
# print(basket)

# print('orange' in basket)

# a = set('abracadabra')
# b = set('alacazam')

# print(a)
# print(b)

# print(a-b)
# print(a|b)
# print(a&b)
# print(a^b)

# tel = {'jack' : 101, 'sape' : 102}
# tel['jack'] = 103
# print(tel)

# del tel['sape']

# print(tel)

# tel['stack'] = 78
# tel['queue'] = 80
# print(tel)
# sorted(tel)

# print(tel['stack'])
# print('queue' in tel)

knights = {'friend1':'shiva', 'friend2': 'shiva2'}
for k, v in knights.items():
    print(k,'->', v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions =  ['name', 'zodiac sign', 'favourite colour']
answers = ['lancelot', 'Libra', 'blue']
for q, a in zip(questions, answers):
    print('what is your {0} ? it is {1}'.format(q, a))

