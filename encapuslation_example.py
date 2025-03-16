#implement the example of the encapsulation 

class Account:
    def __init__(self, owner, amount, salary):
        self.owner = owner  #public access properties
        self._amount = amount   #protected access properties 
        self.__salary = salary  #private access properties 

    def display(self):
        print(f"name : {self.owner} | amount : {self.owner} | salary : {self.__salary}")

acc1 = Account('shiva', 800, 100000)
print(acc1.owner)
#this will give error beecausee it is private propertiees