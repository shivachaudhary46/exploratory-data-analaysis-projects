def my_generator():
    for i in range(0, 500):
        yield i;

gen = my_generator();
# print(next(gen));
# print(next(gen));
# print(next(gen));
# print(next(gen));

#generator typeObject is not suscriptable 
# for j in gen[:20]:
#     print(j);

# for j in gen:
#     print(j);

#generate the huge data from the api
from newsapi import NewsApiClient;
import pprint;

#initialize the newapi with apikey
newsapi = NewsApiClient(api_key='9b603a86fd3444a4b7326c3f0d6e60fd');

get_headlines = newsapi.get_top_headlines(q='sports',
                                           category='sports',
                                           country='us',
                                           language='en'); 
# pprint.pprint(get_headlines);
def generator_headlines():
    for i, head in enumerate(get_headlines['articles']):
        yield i, head['title'].title();

gen = generator_headlines();

# for j in gen:
#     print(j[0], j[1]);

#why generator is used in the pythoN ?
'''generatoe does not stores the variable like lists in the memory. if we get the hugedata from any source or api we get huge data that cannot be put in the variable. Even if we succeded putting variable computer takes huge time or this so. programmer has generated this generator concpt. generator only iterates whne the function or the lambda function is called .It means that generator or yield cannot be used outside the function'''

#function caching 
#function caching is the way of the memoization of the data in the computer. It means that when the computer or program computes the data it saves the data as the cache so. again if same problem arises it can solve quickly and it does not takes any time. function caching is the effective solution  in the expensive computation and when there is repeated input and repeated problems because it saves the each problem so it will be use for future use

#we can do function caching from the functools in the python 
#functools.lru_cache(maxsize=None) decorator

from functools import lru_cache;
import time;

@lru_cache(maxsize=None)
def function_caching(n):
    time.sleep(10);
    return n * 5;

# function_caching(20);
# print('done for the 20');
# function_caching(25);
# print('done for the 25');
# function_caching(2);
# print('done for the 2');
# function_caching(6);
# print('done for the 6');


# function_caching(20);
# print('done for the 20');
# function_caching(25);
# print('done for the 25');
# function_caching(2);
# print('done for the 2');
# function_caching(6);
# print('done for the 6');

@lru_cache(maxsize=None)
def fibo(n):
    if n < 2:
        return n;
    else:
        return fibo(n-1) + fibo(n-2);

print(fibo(20));

