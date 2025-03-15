
class snake:
    name = "anaconda"

    #method to change name 
    def modifyName(self, new_name):
        self.name = new_name

snake1 = snake()
print(snake1.name)
snake1.modifyName('cobra')
print(snake1.name)