### Python Arrays ###

# Arrays
'''
Arrays are used to store multiple values in one single variable:
'''

cars = ["Ford", "Volvo", "BMW"]
print(cars)

# What is an Array?
'''
An array is a special variable, which can hold more than one value at a time.
If you have a list of items (a list of car names, for example), storing the cars in single variables could look like this:

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

However, what if you want to loop through the cars and find a specific one? And what if you had not 3 cars, but 300?
The solution is an array!
An array can hold many values under a single name, and you can access the values by referring to an index number.
'''

# Access the Elements of an Array
x = cars[0] # Get the value of the first array item:
print(x)

print(cars)
cars[0] = "Toyota" # cars[0] = "Toyota"
print(cars)

# The Length of an Array
x = len(cars)
print(x)

# Looping Array Elements
for x in cars:
    print(x)

# Adding Array Elements
cars.append("Honda")
print(cars)

# Removing Array Elements
cars.pop(1)
print(cars)

cars.remove("Volvo")
print(cars)



### Array Methods ###
'''
Method	    Description
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
'''