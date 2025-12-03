#Encapsulation in Python is an object-oriented programming (OOP) principle that refers to bundling data (attributes) and methods (functions) that operate on that data into a single unit, 
# typically a class, and restricting direct access to some of the object's components. 

# three attributes you are having
#1.public attributes : accessible from anywhere
#2.protect attributes : prefixed with single underscore should not accessed directly outside the class
#3.private attributes: prefixed with __double underscore it is harder to access directly
class bank_accounts():
    def __init__(self,account_number,balance):
        self.account_number = account_number  #public
        self._balance = balance  #protect
        self.__pin = "1234"    #private

    def deposit(self,amount):
        if amount>0:
            self._balance+=amount
            print(f"deposited: {amount}")
        else:
            print("Invalid amount")

    def withdraw(self,amount,pin):
        if pin ==self.__pin:
            if 0<amount<=self._balance:
                self._balance -= amount
                print(f'withdrawn: {amount}')
            else:
                print(f"Insufficient balance or invalid balance")
        else:
            print("Incorrect pin")      

    def check_balance(self,pin):
        if pin == self._pin:
            print(f"current balance: {self._balance}")
        else:
            print("Incorrect PIN")              
            
                 

