### Python Variables ###

# Creating Variables
x = 5
y = "John"
print(x)
print(y)

# Rewriting the variable
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(y)
print(z)

# Get the type
x = 5
y = "John"
print(type(x))
print(type(y))

# Single or Double Quotes?
x = "John"
# is the same as
x = 'John'

# Case-Sensitive
a = 4
'''
A = "Sally"
''' #A will not overwrite a



### Variable Names ###

'''
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
''' # Legal Variable names:

'''
2myvar = "John"
my-var = "John"
my var = "John"
''' # Illegal Variable names:

myVariableName = "John" #camelCase
MyVariableName = "John" #PascalCase
my_variable_name = "John" #snake_case

# Python Variables - Assign Multiple Values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


### Python - Output Variables ###

# Output Variables
x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

'''
x = 5
y = "John"
print(x + y)
''' #TypeError

x = 5
y = "John"
print(x, y)



### Python - Global Variables ###

x = "awesome"
def myfunc():
    print("Python is " + x)
myfunc()

x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()

print("Python is " + x)

# The global Keyword
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)

x = "awesome"
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)