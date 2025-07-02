#Constructors
#In Python, a constructor is a special method used to initialize the newly created object of a class. The constructor method in Python is called __init__().
'''Syntax

class ClassName:
 def __init__(self, parameters):
  #initialization code'''


class Person:
    def __init__(self, name, age):
        print("Hii")
        self.name = name
        self.age = age

    def greet(self):  # ← Now correctly indented inside the class
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object
p = Person("Alice", 30)
p.greet()
