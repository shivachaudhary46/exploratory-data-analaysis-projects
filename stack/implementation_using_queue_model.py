#Implementation by fifo queue

from queue import LifoQueue

#initializing the lifo queue
stack = LifoQueue(maxsize=3)

print(stack.qsize())

#to insert element into the stack we use put function 
stack.put('a')
stack.put('b')
stack.put('c')

print('full : ', stack.full())
print('size :' , stack.qsize())

#to pop element we use get function
print(stack.get())
print(stack.get())
print(stack.get())

print('is empty : ', stack.empty())