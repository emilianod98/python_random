### Rounding Decimals ### 
import numpy as np

# Ro1unding Decimals
'''
There are primarily five ways of rounding off decimals in NumPy:

•   truncation
•   fix
•   rounding
•   floor
•   ceil

'''



# Truncation
'''
Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.
'''

arr = np.trunc([-3.1666, 3.6667])
print(arr) # Truncate elements of following array

arr = np.fix([-3.1666, 3.6667])
print(arr) # Same example, using fix()



# Rounding
'''
The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.
E.g. round off to 1 decimal point, 3.16666 is 3.2
'''

arr = np.around(3.1666, 2)
print(arr) # Round off 3.1666 to 2 decimal places.



# Floor
'''
The floor() function rounds off decimal to nearest lower integer.
E.g. floor of 3.166 is 3.
'''

arr = np.floor([-3.1666, 3.6667])
print(arr) # Floor the elements of following array.



# Ceil
'''
The ceil() function rounds off decimal to nearest upper integer.
E.g. ceil of 3.166 is 4.
'''

arr = np.ceil([-3.1666, 3.6667])
print(arr) # Ceil the elements of following array.