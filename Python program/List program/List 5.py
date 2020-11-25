lis = ['aba', 'abc', 'abb', '232']
x = 0
for i in lis:
    if len(i) > 0 and i[0] == i[-1]:
        x += 1
print(x)