### NumPy Getting Started ###

# Installation of NumPy
'''
pip install numpy
'''

# Import NumPy
import numpy

arr = numpy.array([1, 2, 3, 4, 5])
print(arr) # Now NumPy is imported and ready to use.


import numpy as np # NumPy is usually imported under the np alias.

arr = np.array([1, 2, 3, 4, 5])
print(arr) # Now the NumPy package can be referred to as np instead of numpy.

# Checking NumPy Version
import numpy as np
print(np.__version__) # This will print the version of NumPy installed.