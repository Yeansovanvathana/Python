#7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
def not_poor(str):
    s = str.find('not')
    v = str.find('poor')
    if v > s and s > 0 and v > 0:
        str = str.replace(str[s:(v + 4)], 'good')
        return str
    else:
        return str
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))
