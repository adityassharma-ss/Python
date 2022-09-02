def printSuccess():
    print("a")
    print("b")
    print("c")

printSuccess()

def printMesssage(msg):
    print(msg)
    
 

printMesssage("this is message")
printMesssage(type("this is message"))

def printMsg(msg1, msg2):
    print(msg1, msg2)
    
printMsg("cat", "mat")


a = int(input("enter a: "))
b = int(input("enter b: "))
def mypow(a,b):
    c = a**b
    print(c)
    
mypow(a,b)

def f(c2,c1,c3):
    print(c1,c2,c3)
    print(c2,c1,c3)
    
f(c1 = "A", c2 = "B", c3 = "C")

def add(x,y):
    c = x+y
    print(c)
    return c
    print(c)
    
    
add(2,3)

def g():
    variable = 5

print(g())

def sumadd(*args):
    sum =0
    for i in range(len(args)):
        sum+=args[i]
    return sum

print(sumadd(1,2,3,4,5))

def f(sum=0):
    print(sum)
    
f()