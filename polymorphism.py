#Polymorphism means “many forms”.
#It allows the same interface or method name to behave differently depending on the object or data type.

#Method Overriding (Runtime Polymorphism)
#A child class provides a specific implementation of a method that is already defined in its parent class.
class Payment:
    def process_payment(self,payment):
         print(f"Processing payment through {payment}")

class CreditCardPayment(Payment):
    def process_payment(self,payment):
        print(f"the payment mode is through{payment}(creditcard)")   

class UPIPayment(Payment):
    def process_payment(self,payment):
        print(f"the payment mode is through{payment}(UPI)")         
 
payments = [CreditCardPayment(),UPIPayment()]
for p in payments:
    p.process_payment("Online")
