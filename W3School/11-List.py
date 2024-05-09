### Python Lists ###

# Create a List
thislist = ["apple", "banana", "cherry"]
print(thislist)

# List Items
'''
- List items are ordered, changeable, and allow duplicate values.
- List items are indexed, the first item has index [0], the second item has index [1] etc.
'''

# Ordered
'''
- When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
- If you add new items to a list, the new items will be placed at the end of the list.
'''

# Changeable
'''
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
'''

# Allow Duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# List Items - Data Types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]

list3 = [True, False, False]


list4 = ["abc", 34, True, 40, "male"]

# type()
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# The list() Constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# Access Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Negative Indexing
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# Range of Negative Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

### Python - Change List Items ###
# Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"

print(thislist)

# Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]

print(thislist)

# Change the second and third value by replacing it with one value
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]

print(thislist)

# Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")

print(thislist)

# Append Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")

print(thislist)

# Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)

print(thislist)

# Add Any Iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

### Python - Remove List Items ###
# Remove Specified Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")

print(thislist)

# Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)

print(thislist)

# Remove the last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()

print(thislist)

# Remove the first item
thislist = ["apple", "banana", "cherry"]
del thislist[0]

print(thislist)

# Clear the List
thislist = ["apple", "banana", "cherry"]
thislist.clear()

print(thislist)

### Python - Loop Lists ###
'''
# Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
    # Loop Through the Index Numbers

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

# Using a While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    '''

# Looping Using List Comprehension
'''
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
'''

### Python - List Comprehension ###
'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)
'''
# List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# The Syntax
# newlist = [expression for item in iterable if condition == True]

# The expression is the current item in the iteration, but it is also    the outcome, which you can manipulate before it ends up like a list item in the new list:

# newlist = [x if x != "banana" else "orange" for x in fruits]

# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:



### Python - Sort Lists ###

# Sort List Alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort the Numbers List Alphanumerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort Descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# Customize Sort Function
def myfunc(n):
    return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# Case Insensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Case Sensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Reverse Order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)



### Python - Copy Lists ###

# Copy a List
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2

# Another Way to Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

# Another Way to Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)



### Python - List Methods ###
'''
Method	        Description
append()	    Adds an element at the end of the list
clear()	        Removes all the elements from the list
copy()	        Returns a copy of the list
count()	        Returns the number of elements with the specified value
extend()	    Add the elements of a list (or any iterable), to the end of the current list
index()	        Returns the index of the first element with the specified value
insert()	    Adds an element at the specified position
pop()	        Removes the element at the specified position
remove()	    Removes the item with the specified value
reverse()	    Reverses the order of the list
sort()	        Sorts the list
'''