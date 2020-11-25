#11. Write a Python program to remove the characters which have odd index values of a given string.
a='abcdef'
c=''
b=range(len(a))
for i in b:
    if i%2!=0:
        c+=a[i]
print(c)



