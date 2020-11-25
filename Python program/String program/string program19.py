#19. Write a Python program to get the last part of a string before a specified character.
a = 'https://www.facebook.com/odvito-11'
print(a.rsplit('/', 1)[0])
print(a.rsplit('-', 1)[0])

