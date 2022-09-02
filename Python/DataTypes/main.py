x = 5
print(type(x))

str = "Hello World"
print(str)

a = 1j 
print(type(a))

x = ["apple", "banana", "cherry"]
print(x)

x = ("apple", "banana", "cherry")
print(type(x))

x = range(6)
print(x)

x = {"name" : "John", "age" : 36}
print(x)

x = True
print(x)

x = b"Hello"	
print(x)	
x = bytearray(5)
print(x)		
x = memoryview(bytes(5))
print(x)	
x = None

print(x)


x = 1478549    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

import random

print(random.randrange(1, 10))