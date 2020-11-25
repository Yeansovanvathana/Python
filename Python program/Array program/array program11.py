#11. Write a Python program to remove a specified item using the index from an array.
from array import*
x=array('i',[1,2,3,4,5])
print('original array'+str(x))
x.pop(0)
print('remove a specified'+str(x))
