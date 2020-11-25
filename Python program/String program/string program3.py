#3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
a=str(input('enter the simple simple string :'))
length=len(a)
if length >=2:
    n=a[:2]+a[-2:]
else:
    n=''
print('...',n)
