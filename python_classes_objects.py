
# class snake:
#     name = "anaconda"

#     #method to change name 
#     def modifyName(self, new_name):
#         self.name = new_name

# snake1 = snake()
# print(snake1.name)
# snake1.modifyName('cobra')
# print(snake1.name)

class snake:
    
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def modifyName(self, newName):
        self.name = newName

snake1 = snake('anaconda', 56)
snake2 = snake('python', 89)

print(snake1.name)
print(snake1.id)

print(snake2.name)
print(snake2.id)

