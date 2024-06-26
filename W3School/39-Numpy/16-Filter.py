### NumPy Filter Array ###
import numpy as np

# Filtering Arrays.
'''
Getting some elements out of an existing array and creating a new array out of them is called filtering.
In NumPy, you filter an array using a boolean index list.
A boolean index list is a list of booleans corresponding to indexes in the array.
If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array.
'''

arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr) # Create an array from the elements on index 0 and 2.

'''
The example above will return [41, 43], why?
Because the new array contains only the values where the filter array had the value True, in this case, index 0 and 2.
'''



# Creating the Filter Array
'''
In the example above we hard-coded the True and False values, but the common use is to create a filter array based on conditions.
'''

arr = np.array([41, 42, 43, 44])
# Create an empty list
filter_arr = []
# go through each element in arr
for element in arr:
    # if the element is higher than 42, set the value to True, otherwise False:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr = arr[filter_arr]
print(filter_arr)
print(newarr) # Create a filter array that will return only values higher than 42.

arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print(filter_arr)
print(newarr) # Create a filter array that will return only even elements from the original array.