x=str("Hello world")
print(x)
print(type(x))
x=20
print(type(x))
x=20.4
print((type(x)))
x=1j
print(type(x))
x=("apple","book","Ice")
print(type(x))
x=["appel","book","bike"]
print(type(x))
x=range(7)
print(type(x))
x={"name":"John","age":35}
print(type(x))
x={"name","John","book"}
print(type(x))
x = frozenset({'apple','banana','banana'})
print(type(x))
x=False
print(type(x))
x=b"jjjj"
print(type(x))
x=bytearray(5)
print(type(x))
x=memoryview(bytes(5))
print(type(x))
x, y, z = "Orange", "Banana", "Cherry"
print(y)
print(z)
print(x)
#global variable
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is "+x)
myfunc()
print("Python is " + x)
#global variable
import random
print(random.randrange(1,10))
a = """"Lorem ipsum dolor sit amet,consectetur adipiscing elit, sed do eiusmod tempor incidiunt ut labore et dolore magna aliqua."""
print(a)
a="Hello, world!"
print(a[6:8])
b="good evening"
print(b[-5:])
txt="The rain in spain stays mainly in the pain"
x="st" in txt
print(x)
a="Hello"
b="World"
c=a+" "+b
print(c)
age=18
txt="My name is John, and I am {}"
print(txt.format(age))
x=200
print(isinstance(x,int))
x=5
y=2
print(x/y)
x=5
x&=3
print(x)
thislist=["apple","banana","cherry"]
print(thislist)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:6])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:3])
thislist=["apple","banana","cherry"]
thislist[1]="book"
print(thislist)
x=("apple","book","pen")
y=list(x)
y[1]="dog"
x=tuple(y)
print(x)
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
thistuple = ("apple",)
print(type(thistuple))




