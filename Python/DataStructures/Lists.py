L = [1,3,4.9,"name",3] 
print(type(L))

print(L[1]) 
print(L[1:3])
print(L[::-1])

del L[1]
print(L)

L.append(77)
L = L + ["how", "are", 6, "you"]
print(L)

print(help(L.append))
print(L.pop())

print(L.clear()) 


L3 = [x**2 for x in range(10)]
print(L3)


