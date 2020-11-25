#18. Write a Python function to get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string.
def chang_char(str):
    length=len(str)
    if length>3:
        return str[:3]
    elif length<=3:
        return str

print(chang_char('cat'))
print(chang_char('notebook'))
print(chang_char('go'))
