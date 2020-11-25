#12. Write a Python program to count the occurrences of each word in a given sentence.
a='the dog barked at the cat last night'
count=dict()
words=a.split()
for word in words:
    if word in count:
        count[word]+=1
    else:
        count[word]=1
print(count)
