#6. Write a Python program to get the number of occurrences of a specified element in an array.
from array import *
num = array('i', [0, 2, 4, 2, 6, 8, 2,2])
print("Original array: "+str(num))
print("Number of occurrences of the number 3 in the said array: "+str(num.count(2)))
