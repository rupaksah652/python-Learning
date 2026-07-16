#custome Exception 
class Myexception(Exception):
    def __init__(self,message):
        print(message)
        
class bank:

    def __init__(self,balance):
        self.balance=balance
    def withdraw(self,amount):
        if amount < 0:
            raise Myexception('amount canot be in negative')
        if self.balance < amount:
           raise Myexception("u don't have that much of amount")
        self.balance=self.balance-amount

obj=bank(10000)
try:
    obj.withdraw(-5000)
except Myexception as e:
    pass
else:
    print(obj.balance)