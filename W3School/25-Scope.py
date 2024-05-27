### Python Scope ###

'''
A variable is only available from inside the region it is created. This is called scope.
'''

# Local Scope
def myfunc():
    x = 300
    print(x)

myfunc()    # A variable created inside a function is available inside that function.

# Function Inside Function

'''
As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:
'''

def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc() 


# Global Scope
x = 300
def myfunc():
    print(x)
myfunc()
print(x) # A variable created outside of a function is global and can be used by anyone.


# Naming Variables
'''
If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):
'''

x = 300
def myfunc():
    x = 200
    print(x)
myfunc()
print(x)


# Global Keyword
def myfunc():
    global x
    x = 300
myfunc()
print(x) # If you use the global keyword, the variable belongs to the global scope.

'''
Also, use the global keyword if you want to make a change to a global variable inside a function.
'''

x = 300
def myfunc():
    global x
    x = 200
myfunc()
print(x)


# Nonlocal Keyword
'''
The nonlocal keyword is used to work with variables inside nested functions.
The nonlocal keyword makes the variable belong to the outer function.
'''

def myfunc1():
    x = "Jane"
    def myfunc2():
        nonlocal x
        x = "hello"
    myfunc2()
    return x

print(myfunc1())