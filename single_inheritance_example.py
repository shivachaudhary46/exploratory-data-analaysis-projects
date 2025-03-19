#create a bank account with deposit method and withdrawal method 
#from single inheritance
class bank_account:
    def __init__(self, owner, amount):
        
        self.owner = owner
        self.amount = amount

    def deposit(self, dep_amount):
        
        self.amount = self.amount + dep_amount
        print(f"{self.amount} added to account")

    def withdrawal(self, withdraw_amount):
        
        if self.amount >= withdraw_amount:
            self.amount = self.amount - withdraw_amount
        else:
            print(f"insufficient balance {self.amount}")
        print(f"remaining amount {self.amount}")


class Person(bank_account):
    def __init__(self, owner, amount, salary, age):
        super().__init__(owner, amount)
        self.salary = salary
        self.age = age

    def display(self):
        print(f"name : {self.owner} \nage : {self.age} \nsalary : {self.salary} \nsavings : {self.amount}")


person1 = Person('shiva', 8000, 500000, 19)
print(person1.owner)
print(person1.salary)
print(person1.age)
print(person1.amount)

person1.deposit(9000)
person1.display()

person1.deposit(500000)
person1.display()

person1.withdrawal(400000)
person1.display()