"""Question – Parameterized Methods, Constructors & Destructors
 Create a class BankAccount that:
 1. Uses a parameterized constructor to initialize account_number and balance
2. Implements methods deposit(amount) and withdraw(amount)
3. Uses a destructor to display a message when the object is deleted
4. Handle invalid withdrawal using proper checks		"""

#Uses a parameterized constructor to initialize account_number and balance
class BankAccount:
    def __init__(self,acc_number,balance):
        self.acc_number=acc_number
        self.balance=balance
obj1=BankAccount("Ac123477",5000)
print(obj1.acc_number,obj1.balance)

#Implements methods deposit(amount) and withdraw(amount)
class BankAccount:
    def __init__(self,acc_number,balance):
        self.acc_number=acc_number
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        return self.balance
    def withdraw(self,amount):
        self.balance=self.balance-amount
        return self.balance

obj1=BankAccount("Ac123477",5000)
print(obj1.balance)
print(obj1.acc_number)
print(obj1.deposit(900))
print(obj1.withdraw(500))

# Uses a destructor to display a message when the object is deleted
class BankAccount:
    def __init__(self,acc_number,balance):
        self.acc_number=acc_number
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        return self.balance
    def withdraw(self,amount):
        self.balance=self.balance-amount
        return self.balance
    def __del__(self):
        print("Object deleted")

obj1=BankAccount("Ac123477",5000)
print(obj1.balance)
print(obj1.acc_number)
print(obj1.deposit(900))
print(obj1.withdraw(500))

# 4. Handle invalid withdrawal using proper checks
class BankAccount:
    def __init__(self,acc_number,balance):
        self.acc_number=acc_number
        self.balance=balance
    def deposit(self,amount):
        if amount >0:
            self.balace+=amount
            print("Amount deposited",amount)
        else:
            print("Invalid deposit amount")
        return self.balance

    def withdraw(self,amount):
        if amount<=0:
            print("Invalid withdraw amount")
        elif amount >self.balance:
            print("Insufficient balance")
        else:
            self.balance=self.balance-amount
        return self.balance
    def __del__(self):
        print("Object deleted")

obj1=BankAccount("Ac123477",5000)
print(obj1.balance)
print(obj1.acc_number)
print(obj1.deposit(900))
print(obj1.withdraw(500))