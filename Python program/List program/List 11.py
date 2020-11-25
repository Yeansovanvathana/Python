def common(lis1, lis2):
    result = False
    for i in lis1:
        for x in lis2:
            if x == i:
                return True
                return result
print(common([1, 2, 3, 4, 5], [6, 7, 8, 9, 5]))
print(common([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))