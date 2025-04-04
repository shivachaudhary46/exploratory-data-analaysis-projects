tuple3 = (1, 2, 3);
print(tuple3);

for i in tuple3:
    print(i);

tuple_str = ("string", "is", "tuple");
print(tuple_str);

for j in tuple_str:
    print(j);

a_tuple = (1, "mom", "dad", "me", 1);
print(a_tuple);

for k in a_tuple:
    print(k);

#tuple immutable
tuple3 = (1,);
print(tuple3, type(tuple3));

#positive indexing
tuple_pos = ("my name is shiva chaudhary",);
print(tuple_pos[0][1:], type(tuple_pos[0][1:]));
tuple2 = tuple_pos[6:12];#()=❌
print(tuple2);

animals = ("cat", "bat","rat", "mouse", "horse", "dolphin", "mermaid", 'whale', 'snake', 'snail', 'tiger', 'bear','crocodile');
print(animals[10:13]);
print(animals[5:8]);
print(animals[9:13]);

print(animals[-2:-1]);
print(animals[-8:-2]);
print(animals[-10:-1]);
print(animals[-13:-7]);

print(animals[-12:]);
print(animals[:]);
print(animals[:-12]);

print(animals[::-1]);
print(animals[::2]);
print(animals[::3]);
print(animals[::-3]);
print(animals[-10:-2:2]);

if "cat" in animals:
    print("cat is present");
else:
    print("cat is absent");

if "horse" in animals:
    print("horse is present");
else:
    print("horse is absent");

tuple2 = ("jevis", "shiva", "samprad", "anje", "ujwol", "krisha");
convert_list = list(tuple2);
convert_list[0] = "dhiraj"; #update
convert_list.pop();         #remove last item
convert_list.pop(3);        #remove index;
convert_list.append("bishal");
tuple1 = tuple(convert_list);
print(tuple1);

#indirect method to replace the tuple
countries = ("england", "america", "australia", "france", "japan", "italy", "spain");
print(countries);
temp = list(countries);
print(temp);
temp.append("korea");
temp.append("russia");
print(temp);
temp.pop(3);
print(temp);
temp[2] = "switzerland";
print(temp);
countries = tuple(temp);
print(countries);

a = ("a", "b", "c", "d", "e", "f", "g");
b = ("a", "b");
print(a+b);

counter = ("a","b","b","a","e","f","a");
count1 = counter.count("a");
print(count1);
counter.count("c");#tuple attribute
print(counter);

counter2 = ('1','2','1','1','2','1','2');
count2 = counter2.count(1);
print(count2);
count3 = counter2.count('1');
print(count3);

index1 = counter2.index('2');
print(index1);

index2 = counter.index('a', 2, 5); #index(element, start, end);
print(index2);


#order
tuples = (1, 'shiva', 'jevis', 'samprad', 'anjelika', 'krisha', 'dhiraj', 'boolean', False, True, 12);
for tuple1 in tuples:
    print(tuple1);

print(tuples[0:15]);
print(tuples[3:len(tuples)]);
print(tuples[-5:-2]);
print(tuples[-3]);
print(tuples[-3:len(tuples)]);
print(tuples[:-8]);

tuple_list = list(tuples);
print(tuple_list);
tuple_list.append('ujwol');
tuple_list.append(123);
tuple_list.pop(0);
extend_list = ['junu', 'bishal', 'dhiraj'];
tuple_list.extend(extend_list);
tuple_list.insert(2, 'shovit');
print(tuple_list);
tuple_list.remove('boolean');
tuple_list.reverse();
list_to_tup = tuple(tuple_list);
print(list_to_tup);