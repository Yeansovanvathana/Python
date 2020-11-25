#17. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
def copies_characters(str):
    last_char=(str[-2:])
    return last_char*4
print(copies_characters('Facebook'))
#Or
a='Facebook'
print(a[-2:]*4)
