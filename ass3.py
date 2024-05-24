

# Example 1: Saving and Loading a NumPy Array in `.npy` Format

# Saving an Array

import numpy as np

# Create a NumPy array
array = np.array([1, 2, 3, 4, 5])

# Save the array to a file
np.save('array.npy', array)


#Loading the Array

# Load the array from the file
loaded_array = np.load('array.npy')

print(loaded_array)


# Example 2: Saving and Loading Multiple Arrays in `.npz` Format

# Saving Multiple Arrays

import numpy as np

# Create multiple NumPy arrays
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

# Save the arrays to a file
np.savez('arrays.npz', array1=array1, array2=array2)


# Loading Multiple Arrays

# Load the arrays from the file
loaded = np.load('arrays.npz')

array1_loaded = loaded['array1']
array2_loaded = loaded['array2']

print(array1_loaded)
print(array2_loaded)


# Example 3: Saving and Loading Data in Text Format

# Saving an Array to a Text File

import numpy as np

# Create a NumPy array
array = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]])

# Save the array to a text file
np.savetxt('array.txt', array)


# Loading the Array from a Text File

# Load the array from the text file
loaded_array = np.loadtxt('array.txt')

print(loaded_array)

