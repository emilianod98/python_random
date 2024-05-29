### Python String Formatting ###
'''
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
Before Python 3.6 we had to use the format() method.
'''

# F-Strings
'''
F-string allows you to format selected parts of a string.
To specify a string as an f-string, simply put an f in front of the string literal, like this:
'''

txt = f"The price is 49 dollars"
print(txt) # Create an f-string.


# Placeholders and Modifiers
'''
To format values in an f-string, add placeholders {}, a placeholder can contain variables, operations, functions, and modifiers to format the value.
'''

price = 59
txt = f"The price is {price} dollars"
print(txt) # Add a placeholder for the price variable.

'''
A placeholder can also include a modifier to format the value.
A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
'''

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt) # Display the price with 2 decimals.

txt = f"The price is {95:.2f} dollars"
print(txt) # Display the value 95 with 2 decimals.


# Perform Operations in F-Strings
'''
You can perform Python operations inside the placeholders.
You can do math operations:
'''

txt = f"The price is {20 * 59} dollars"
print(txt) # Perform a math operation in the placeholder, and return the result.

price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt) # Add taxes before displaying the price.

price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"

print(txt) # Return "Expensive" if the price is over 50, otherwise return "Cheap".


# Execute Functions in F-Strings
fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt) # Use the string method upper()to convert a value into upper case letters.

def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt) # Create a function that converts feet into meters.


# More Modifiers
price = 59000
txt = f"The price is {price:,} dollars"
print(txt) # Use a comma as a thousand separator.


'''
Formatting Types
:<		Left aligns the result (within the available space)
:>		Right aligns the result (within the available space)
:^		Center aligns the result (within the available space)
:=		Places the sign to the left most position
:+		Use a plus sign to indicate if the result is positive or negative
:-		Use a minus sign for negative values only
: 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
:,		Use a comma as a thousand separator
:_		Use a underscore as a thousand separator
:b		Binary format
:c		Converts the value into the corresponding Unicode character
:d		Decimal format
:e		Scientific format, with a lower case e
:E		Scientific format, with an upper case E
:f		Fix point number format
:F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
:g		General format
:G		General format (using a upper case E for scientific notations)
:o		Octal format
:x		Hex format, lower case
:X		Hex format, upper case
:n		Number format
:%		Percentage format
'''


# String format()
'''
Before Python 3.6 we used the format() method to format strings.
The format() method can still be used, but f-strings are faster and the preferred way to format strings.
The next examples in this page demonstrates how to format strings with the format() method.
The format() method also uses curly brackets as placeholders {}, but the syntax is slightly different:
'''

price = 49
txt = "The price is {} dollars"
print(txt.format(price)) # Add a placeholder where you want to display the price.

'''
You can add parameters inside the curly brackets to specify how to convert the value:
'''

txt = "The price is {:.2f} dollars" # Format the price to be displayed as a number with two decimals.


# Multiple Values
'''
print(txt.format(price, itemno, count)) # If you want to use more values, just add more values to the format() method:
'''

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))


# Index Numbers
'''
You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:
'''
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

'''
Also, if you want to refer to the same value more than once, use the index number:
'''

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))


# Named Indexes
'''
You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you pass the parameter values txt.format(carname = "Ford"):
'''

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))