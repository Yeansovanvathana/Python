#20. Write a Python function to reverses a string if it's length is a multiple of 4.
def reverses_str(str):
    if len(str)%4==0:
        return ''.join(reversed(str))
    return str
print(reverses_str('abcd'))
print(reverses_str('facebook'))
print('not multiple of 4 :',reverses_str('wechat'))

