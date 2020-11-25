#8. Write a Python function that takes a list of words and returns the length of the longest one.
a=['PHP','Exercise','Backend']
s = [(len(word),word) for word in a]
s.sort()
print('Longest String in list is ',s[-1][1])
