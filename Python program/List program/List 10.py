lis = ["abc", "ab", "abb", "a"]
n = 2
lis1 = []
for i in lis:
    if len(i) > n:
        lis1.append(i)
print(lis1)
