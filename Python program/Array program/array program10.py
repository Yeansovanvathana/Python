#10. Write a Python program to insert a new item before the second element in an existing array.
from array import *
num = array('i', [1, 3, 4, 5, 6])
print("Original array: "+str(num))
print("Insert new value 2 before 3:")
num.insert(1, 2)
print("New array: "+str(num))

