a = int(input())
b = int(input())

if(a>b):
    print(a)
    print("a is greater than b")
elif(b>a):
    print(b)
    print("b is greater than a")
else:
    print('equal')
    

print("a") if a>b else print("=") if a==b else print("b")

a = int(input("enter marks: "))
if(a>86):
    print("A+")
elif(a<=85) and (a>=75):
    print("B")
else:
    print("fail")

