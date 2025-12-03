#Inheritance in Python allows one class (child/subclass) to reuse and extend the functionality of another class (parent/superclass).
#It’s a core concept of OOP that promotes code reuse and hierarchical relationships.

#Single inheritance
#parent class
class Animal():
    def speaks(self):
        print("animal makes a sound")

#child class inheriting the parent class
class Dog(Animal):
        def speaks(self):
          print("dog barks")
#create objects
a = Animal()
d = Dog()
a.speaks() #animal makes a sound
d.speaks() #dog barks




#using super() to call parents
class Animal():
     def speaks(self):
          print("Animals makes a sound")
    
class Dog(Animal):
    def speaks(self): 
         super().speaks  #call a parent method
         print("Dog barks")

d = Dog()
a = Animal()
d.speaks()
a.speaks()

     
#multiple inheritance
class Human():
         def human(self):
           print("humans will teach")
class Python(Human):
     def teach(self):
          print("python learner")
class Learner(Human,Python): #multiple inheritance
     def pythonteach(self):
          print("they are teaching a python")         
learn = Learner()
learn.human()
learn.teach()
learn.pythonteach()


#multilevel- inheritance
class Grandparent():
     def grandparent(self):
          print("I am the grandparent")

class Parent(Grandparent):
     def parent(self):
          print("I am the Parent")   

class Child(Parent):
     def child(self):
          print("I am the child")     
c =  Child()
c.grandparent()
c.parent()
c.child()


#hierchical inheritance
# Parent class
class Human:
    def human(self):
        print("They are humans")

# Child class 1
class Teacher(Human):
    def teach(self):
        print("They are teaching")

# Child class 2
class Student(Human):
    def learn(self):
        print("They are learning")

# Create objects
t = Teacher()
s = Student()

# Access methods
t.human()    # From Human
t.teach()    # From Teacher
s.human()    # From Human
