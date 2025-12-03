class Employee:   #class definition
    #constructor to intialize attributes
    def __init__(self,name,emp_id,department):
        self.name = name               #Attributes
        self.emp_id = emp_id           #Attributes
        self.department = department     #Attributes

    #method to display employee details
    def display_info(self):
        print(f"Name: {self.name}, ID:{self.emp_id}, Department: {self.department}")

    def update_department(self,new_department):
        self.department = new_department
        print(f"{self.name}'s department updated to {self.department}")  

   #creating objects(Instances of employee class)
emp1 = Employee("Alice",101,"HR") 
emp2 = Employee("Bob",102, "engineering")       

   #Accessing attributes and methods
emp1.display_info()      # calls method
emp2.display_info()

   #updating department for emp2
emp1.update_department("IT department")
emp2.update_department("Product Development")  

    #checking instance relationship
print(isinstance(emp1, Employee))
print(isinstance(emp2,Employee))