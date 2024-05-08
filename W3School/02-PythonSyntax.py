### Python Syntax ###
print("Hello, World!")

# Python Indentation
if 5 > 2:
    print("Five is greater than two!")

'''
if 5 > 2: 
print("Five is greater than two!")
''' #SYNTAX ERROR

'''
if 5 > 2:
    print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!")
''' #There is no error, but the code is horrendous.

'''
if 5 > 2:
    print("Five is greater than two!")
        print("Five is greater than two!")
''' # IndentationError: unexpected indent



### Python Variables ###
x = 5
y = "Hello, World!"

print(x)
print(y)