#5. Write a Python program to get the current memory address and the length in elements of the buffer used to hold an array?s contents and also find the size of the memory buffer in bytes.
from array import *
num_array= array('i', [1, 3, 5, 7, 9])
print("Original array: "+str(num_array))
print("Current memory address and the length in elements of the buffer: "+str(num_array.buffer_info()))
print("The size of the memory buffer in bytes: "+str(num_array.buffer_info()[1] * num_array.itemsize))
