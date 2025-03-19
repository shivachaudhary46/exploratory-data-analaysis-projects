#python program to implement 
#stack using List 

stack = []

# append() function to push
# element in the stack 
stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')

print('initial stack : ', stack)

#taking out the pushed element 
#Filo order 
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('after poping out all element : ')
print(stack)