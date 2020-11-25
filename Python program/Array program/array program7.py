#7. Write a Python program to append items from inerrable to the end of the array.
from array import *
num=array('i',[1,2,3,4,5,6])
print('original array: '+str(num))
num.extend(num)
print('append item to the end of the array:'+str(num))
