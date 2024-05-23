### Python Inheritance ### Herencía

'''
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.
'''

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname()

# Create a Child Class
'''
To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
'''

class Student(Person):
    pass # Create a class named Student, which will inherit the properties and methods from the Person class:

x = Student("Mike", "Olsen")
x.printname()

# Add the __init__() Function
'''
So far we have created a child class that inherits the properties and methods from its parent.
We want to add the __init__() function to the child class (instead of the pass keyword).
Note: The __init__() function is called automatically every time the class is being used to create a new object.
'''

class Student(Person):
    def __init__(self, fname, lname):
        # add properties etc
        pass

'''
When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
'''

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

'''
Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function.
'''

# Use the super() Function
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

# Add Properties
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
x = Student("Mike", "Olsen", 2019)

# Add Methods
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

