### NumPy Trigonometric Functions ### 
import numpy as np

# Trigonometric Functions
'''
NumPy provides the ufuncs sin(), cos() and tan() that take values in radians and produce the corresponding sin, cos and tan values.
'''

x = np.sin(np.pi/2)
print(x) # x = np.sin(np.pi/2).

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sin(arr)
print(x) # Find sine values for all of the values in arr.



# Convert Degrees Into Radians
'''
By default all of the trigonometric functions take radians as parameters but we can convert radians to degrees and vice versa as well in NumPy.
Note: radians values are pi/180 * degree_values.
'''

arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)
print(x) # Convert all of the values in following array arr to radians.



# Radians to Degrees

arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
x = np.rad2deg(arr)
print(x) # Convert all of the values in following array arr to degrees.



# Finding Angles
'''
Finding angles from values of sine, cos, tan. E.g. sin, cos and tan inverse (arcsin, arccos, arctan).
NumPy provides ufuncs arcsin(), arccos() and arctan() that produce radian values for corresponding sin, cos and tan values given.
'''

x = np.arcsin(1.0)
print(x) # Find the angle of 1.0.



# Angles of Each Value in Arrays

arr = np.array([1, -1, 0.1])
x = np.arcsin(arr)
print(x) # Find the angle for all of the sine values in the array.



# Hypotenues
'''
Finding hypotenues using pythagoras theorem in NumPy.
NumPy provides the hypot() function that takes the base and perpendicular values and produces hypotenues based on pythagoras theorem.
'''

base = 3
perp = 4
x = np.hypot(base, perp)
print(x) # Find the hypotenues for 4 base and 3 perpendicular.