#4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
a='restart'
b=a[0]
a=a.replace('a','$')
c=b+a[1:]
print(c)
