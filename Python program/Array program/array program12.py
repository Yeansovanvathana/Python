#12. Write a Python program to remove the first occurrence of a specified element from an array.
from array import *
num = array('i', [1, 2, 3, 4, 3, 1, 9, 3])
print("Original array: "+str(num))
print("Remove the first occurrence of 3 from the said array:")
num.remove(3)
print("New array: "+str(num))
