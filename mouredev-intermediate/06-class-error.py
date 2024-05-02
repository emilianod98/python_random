### ERROR TYPES ###

# SyntaxError
# print "¡Hola Mundo!" ### SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print ("¡Hola Mundo!")

# NameError
# print(name) ### NameError: name 'name' is not defined
name = "Jhon"
print(name)

# IndexError
my_list =["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
# print(my_list[5]) ### IndexError: list index out of range
print(my_list[4])
# print(my_list[-6]) ### IndexError: list index out of range
print(my_list[-5])

# ModuleNotFoundError
# import maths ### ModuleNotFoundError: No module named 'maths'
import math

# ImportError
# from math import PI ### ImportError: cannot import name 'PI' from 'math' (unknown location). Did you mean: 'pi'?
from math import pi

# TypeError
# suma = "2" + 3
# print(suma) ### TypeError: can only concatenate str (not "int") to str

# AttributeError
# print(math.PI) ### AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
print(math.pi)

# KeyError
my_dict = {"name": "Jhon", "age": 25}
# print(my_dict["last_name"]) ### KeyError: 'last_name'
print(my_dict["name"])  

# ValueError
value = "DIEZ"
# print(int(value)) ### ValueError: invalid literal for int() with base 10: 'DIEZ'
value_correct = "10"
print(int(value_correct))

# ZeroDivisionError
# print(5 / 0) ### ZeroDivisionError: division by zero
print(5 / 2)