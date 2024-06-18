### NumPy Creating Arrays ###

# Create a NumPy ndarray Object
'''
Create a NumPy ndarray Object
'''

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

# type(): This built-in Python function tells us the type of the object passed to it. Like in above code it shows that arr is numpy.ndarray type.

# To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray:

arr = np.array((1, 2, 3, 4, 5))
print(arr) # Use a tuple to create a NumPy array.



# Dimensions in Arrays

'''
A dimension in arrays is one level of array depth (nested arrays).
'''
# nested array: are arrays that have arrays as their elements.



# 0-D Arrays.
arr = np.array(42)
print(arr) # Create a 0-D array with value 42.



# 1-D Arrays.
arr = np.array([1, 2, 3, 4, 5])
print(arr) # Create a 1-D array containing the values 1,2,3,4,5.



# 2-D Arrays.
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr) # Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6.



# 3-D arrays.
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr) # Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6.



# Check Number of Dimensions?
'''
NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.
'''

# Example
import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)



# Higher Dimensional Arrays.
'''
An array can have any number of dimensions.
When the array is created, you can define the number of dimensions by using the ndmin argument.
'''

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim) # Create an array with 5 dimensions and verify that it has 5 dimensions.

'''
In this array the innermost dimension (5th dim) has 4 elements, the 4th dim has 1 element that is the vector, the 3rd dim has 1 element that is the matrix with the vector, the 2nd dim has 1 element that is 3D array and 1st dim has 1 element that is a 4D array.
'''