### NumPy Array Slicing ###

# Slicing arrays
'''
Slicing in python means taking elements from one given index to another given index.
We pass slice instead of index like this: [start:end].
We can also define the step, like this: [start:end:step].
If we don't pass start its considered 0
If we don't pass end its considered length of array in that dimension
If we don't pass step its considered 1
'''

# Example:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

# Note: The result includes the start index, but excludes the end index.

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:]) # Slice elements from index 4 to the end of the array.

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4]) # Slice elements from the beginning to index 4 (not included).



# Negative Slicing.
'''
Use the minus operator to refer to an index from the end.
'''

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1]) # arr = np.array([1, 2, 3, 4, 5, 6, 7])



# STEP.
'''
Use the step value to determine the step of the slicing
'''

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2]) # Return every other element from index 1 to index 5.

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::2]) # Return every other element from the entire array.



# Slicing 2-D Arrays.
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4]) # From the second element, slice elements from index 1 to index 4 (not included).

# Note: Remember that second element has index 1.

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2]) # From both elements, return index 2.

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4]) # From both elements, slice index 1 to index 4 (not included), this will return a 2-D array.