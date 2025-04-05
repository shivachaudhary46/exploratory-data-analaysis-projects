#calculate the factorial number of the given number
#calculate the trailing zeros of the number

#returns the number * factorial function (number -1); = 7*6*5*4*3*2*1
def factorial(num):
    if num <= 1:
        return 1;
    else:
        return num * factorial(num-1);

def trailing_zeros(num):
    #return -1 if num is negative number 
    if num <= 0:
        return -1;

    #floor divide the 5 until it is equals to 5
    #update the 5 in count
    count = 0;
    while num >= 5:
        num //= 5;
        count = count + num;
    
    #return the count 
    return count;

fact = int(input('enter the number to calculate the factorial :'));
result = factorial(fact);
print(f'the factorial number of the {fact} = {result}');

result1 = trailing_zeros(fact);
print(f'the trailing zeros of the {fact} = {result1}');





 
