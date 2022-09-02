from re import S


import sys
sys.path.append('D:/Python/Python/Functions/')

import sumadd as sum

def checkIfNotNumeric(*args):
    retValue = True
    for x in args:
        if not(isinstance(x,(int,float))):
            return False
    return True

def addAllNumerics(*args):
    s=0
    for x in args:
        s+=x
    return S

c = sum.addAllNumerics(2,3,4)
print(c)

myName = "Python"