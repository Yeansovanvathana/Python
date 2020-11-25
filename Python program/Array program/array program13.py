#13. Write a Python program to convert an array to an ordinary list with the same items.
from array import *
num_array=array('i',[1,2,3,4,5])
print('original array: '+str(num_array))
num_list=num_array.tolist()
print('array to an ordinary list: '+str(num_list))

