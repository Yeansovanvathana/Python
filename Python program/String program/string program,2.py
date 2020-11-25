#2. Write a Python program to count the number of characters (character frequency) in a string.
a='google classroom'
dict={}
for x in a:
    key=dict.keys()
    if x in key:
        dict[x]+=1
    else:
        dict[x]=1
print(dict)
