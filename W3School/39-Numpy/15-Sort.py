### NumPy Sorting Arrays ###
import numpy as np

# Sorting Arrays
'''
Sorting means putting elements in an ordered sequence.
Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending.
The NumPy ndarray object has a function called sort(), that will sort a specified array.
'''

arr = np.array([3, 2, 0, 1])
print(np.sort(arr)) # Sort the array.

'''
Note: This method returns a copy of the array, leaving the original array unchanged.
'''

# You can also sort arrays of strings, or any other data type.
arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr)) # Sort the array alphabetically.

arr = np.array([True, False, True])
print(np.sort(arr)) # Sort a boolean array.



# Sorting a 2-D Array
'''
If you use the sort() method on a 2-D array, both arrays will be sorted
'''

arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr)) # Sort a 2-D array.