### NumPy Products ###
import numpy as np

# Products
'''
To find the product of the elements in an array, use the prod() function.
'''

arr = np.array([1, 2, 3, 4])
x = np.prod(arr)
print(x) # Find the product of the elements of this array.

# Returns: 24 because 1*2*3*4 = 24

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
x = np.prod([arr1, arr2])
print(x) # Find the product of the elements of two arrays

# Returns: 40320 because 1*2*3*4*5*6*7*8 = 40320



# Product Over an Axis
'''
If you specify axis=1, NumPy will return the product of each array.
'''

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
newarr = np.prod([arr1, arr2], axis=1)
print(newarr) # Perform summation in the following array over 1st axis.

# Returns: [24 1680] 



# Cummulative Product
'''
Cummulative product means taking the product partially.
E.g. The partial product of [1, 2, 3, 4] is [1, 1*2, 1*2*3, 1*2*3*4] = [1, 2, 6, 24]
Perfom partial sum with the cumprod() function.
'''

arr = np.array([5, 6, 7, 8])
newarr = np.cumprod(arr)
print(newarr) # Take cummulative product of all elements for following array.

# Returns: [5 30 210 1680]