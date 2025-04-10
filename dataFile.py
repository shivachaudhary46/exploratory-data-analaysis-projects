# import numpy as np;
# data = [np.random.standard_normal() for i in range(7)];
# print(data);

from jupyterMethods import g, f;
result = f(45);
print(result);

result1 = g(2, 3);
print(result1);

a = [2, 3, 4]
b = a;
c =list(a);

#c is mutable 
print(c);
print(a is b);
print(b is c);
print(a is c);
print(a is not c);

#we can do mutable or val assignment in the list, numpy arrays, dictionaries
a = [2, 3, 5, [3, 4]];
print(a);

a[-1] = (3, 4);
print(a);

#tuble objects are immutable so we cannot change the value using diff methods 
#addignment value is not consider in the tuple
b = (2, 3, 4 , 'string');
b[2] = 'string';
print(b);


