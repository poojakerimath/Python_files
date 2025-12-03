#Abstraction is one of the four main pillars of Object-Oriented Programming (OOP) 
#It means hiding the implementation details and showing only the essential features of an object to the user.
#ABC stands for Abstract Base Class.
#@abstractmethod marks methods that must be implemented in child classes.
#You cannot instantiate an abstract class directly.
'''
from abc import ABC,abstractmethod

#Abstract class
class Shape(ABC):
     @abstractmethod
     def area(self):
          pass
     
     
     @abstractmethod
     def perimeter(self):
        pass
#concrete class implementing the abstract class
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 *(self.length + self.width)
    
rect = Rectangle(10,5)
print("Area:",rect.area())
print("perimeter:",rect.perimeter())
'''

from abc import ABC ,abstractmethod

#abstract class
class Payment(ABC):
    @abstractmethod
    def process_payment(self,payment):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"processing credit card payment of {amount}")

class UPIPayment(Payment):
    def process_payment(self,amount):
        print(f"The payment successfully paid through {amount}")    

class PayPalPayment(Payment):
    def process_payment(self,amount):
        print(f"The payment successfully paid through {amount}")    
    

payment1 = CreditCardPayment()
payment1.process_payment(100)

payment2 = UPIPayment()
payment2.process_payment(200)

payment3 = PayPalPayment()
payment3.process_payment(2300)





