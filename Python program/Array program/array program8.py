#8. Write a Python program to convert an array to an array of machine values and return the bytes representation.
from array import *
print('bring to string')
x=array('b',[10,20,30,40,50])
s=x.tobytes()
print(s)
