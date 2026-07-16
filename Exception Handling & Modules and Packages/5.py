#raise (in java throw)
class bank:

    def __init__(self,balance):
        self.balance=balance
    def withdraw(self,amount):
        if amount < 0:
            raise Exception('amount canot be in negative')
        if self.balance < amount:
           raise Exception("u don't have that much of amount")
        self.balance=self.balance-amount

obj=bank(10000)
try:
    obj.withdraw(5000)
except Exception as e:
    print(e)
else:
    print(obj.balance)