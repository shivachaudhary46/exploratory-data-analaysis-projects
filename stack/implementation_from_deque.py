#implmentationn using collections.deque

from collections import deque 

stack = deque()

#append function to push 
stack.append(1)
stack.append(7)
stack.append(4)
stack.append(3)

print('Initial Stack: ', stack)

#after popping()

stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack) 


